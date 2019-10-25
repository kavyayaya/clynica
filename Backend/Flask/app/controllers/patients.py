''' controller and routes for patients '''
import os
from flask import request, jsonify, make_response
from app import app, mongo
import logger
from bson.json_util import dumps
from bson.objectid import ObjectId

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))

@app.route('/patient', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def patient():
    '''Methods to GET, ADD, DELETE and PATCH patient data.'''
    data = None
    if request.method == 'GET':
        '''GET Patient data.
        Required params: doctor_id, _id
        '''
        query = request.args
        if query.get('doctor_id', None):
            LOG.debug("doctor_id found")
            # Get list of patients of doctor
            doctor_id = ObjectId(query['doctor_id'])
            doctor = mongo.db.users.find_one( { "_id": doctor_id } )
            print(doctor_id)
            print(doctor)
            if doctor:
                LOG.debug("doctor found")
                # Get list of patient _ids
                patients = doctor.get('patients',[])
                # Remove doctor_id from query and push patient _ids
                query = query.to_dict()
                query.pop('doctor_id', None)
                query['_id'] = { '$in': patients }
                print(query)
                # Run query and enumerate results
                data = mongo.db.patients.find(query)
                data = [patient for patient in data]
        if data:
            return make_response(jsonify({'success': True, 'data': data}), 200)
        elif data == []:
            return make_response(jsonify({'success': False, 'message': 'No patients found.'}))
        else:
            return make_response(jsonify({'success': False, 'message': 'Bad request parameters.'}))

    data = request.get_json()
    if request.method == 'POST':
        '''
        INSERT Patient record.
        Required params: doctor_id, data (JSON Object with patient data).
        '''
        if data.get('doctor_id', None) is not None:
            # Get doctor's _id
            doctor_id = ObjectId(data['doctor_id'])
            # Insert to patients and get _id
            res = mongo.db.patients.insert_one(data)
            patient_id = res.inserted_id
            # Push patient _id to doctor's patients list
            doctor = { "_id": doctor_id }
            new_patient = { '$push': {'patients': patient_id} }
            # Push value
            mongo.db.users.update_one(doctor, new_patient)
            LOG.info("/patient POST: patient created:" + str(data))
            return jsonify({'success': True, 'message': 'Patient created successfully!'}), 200
        else:
            LOG.debug("/patient POST: Bad request parameters.")
            return jsonify({'success': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'DELETE':
        '''
        DELETE Patient data.
        Required params: _id.
        '''
        if data.get('_id', None) is not None:
            db_response = mongo.db.patients.delete_one({'_id': ObjectId(data['_id'])})
            if db_response.deleted_count == 1:
                LOG.info("/patient DELETE: Patient deleted:" + str(data))
                response = {'success': True, 'message': 'record deleted'}
            else:
                LOG.info("/patient DELETE: No record found for deletion: " + str(data))
                response = {'success': True, 'message': 'no record found'}
            return jsonify(response), 200
        else:
            LOG.debug("/patient DELETE: Bad request parameters.")
            return jsonify({'success': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'PATCH':
        '''
        PATCH Patient data.
        Required params: _id.
        '''
        if data.get('query', {}) != {}:
            ob_id = {"_id": ObjectId(data['query'].get('_id', {}))}
            mongo.db.patients.update_one(
                ob_id, {'$set': data.get('payload', {})})
            return jsonify({'success': True, 'message': 'record updated'}), 200
        else:
            return jsonify({'success': False, 'message': 'Bad request parameters!'}), 400
