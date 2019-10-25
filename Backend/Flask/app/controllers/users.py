''' controller and routes for users '''
import os
from flask import request, jsonify, make_response
from app import app, mongo
import logger

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))


@app.route('/user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def user():
    '''Methods to GET, ADD, DELETE and PATCH user data.'''
    if request.method == 'GET':
        '''GET User data.
        Required params: _id/username.
        '''
        query = request.args
        data = mongo.db.users.find_one(query)
        if data:
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify({'success': False, 'message': 'User not found.'}))

    data = request.get_json()
    if request.method == 'POST':
        '''
        INSERT User record.
        Required params: email, data (JSON Object with user data).
        '''
        if data.get('name', None) is not None and data.get('email', None) is not None:
            # Check if user already exists
            exist = mongo.db.users.find_one({'email':data.get('email')})
            # If not, create
            if not exist:
                # Create blank patients array
                data['patients'] = []
                res = mongo.db.users.insert_one(data)
                LOG.info("/user POST: User created:" + str(data))
                return jsonify({'success': True, 'message': 'User created successfully!', 'id': res.inserted_id}), 200
            # Otherwise, conflict
            else:
                LOG.debug("/user POST: User already exists.")
                return make_response(jsonify({'success': False, 'message': 'User already exists.'}), 409)
        else:
            LOG.debug("/user POST: Bad request parameters.")
            return jsonify({'success': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'DELETE':
        '''
        DELETE User data.
        Required params: email.
        '''
        if data.get('email', None) is not None:
            db_response = mongo.db.users.delete_one({'email': data['email']})
            if db_response.deleted_count == 1:
                LOG.info("/user DELETE: User deleted:" + str(data))
                response = {'success': True, 'message': 'record deleted'}
            else:
                LOG.info("/user DELETE: No record found for deletion: " + str(data))
                response = {'success': True, 'message': 'no record found'}
            return jsonify(response), 200
        else:
            LOG.debug("/user DELETE: Bad request parameters.")
            return jsonify({'success': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'PATCH':
        '''
        PATCH User data.
        Required params: _id.
        '''
        if data.get('query', {}) != {}:
            mongo.db.users.update_one(
                data['query'], {'$set': data.get('payload', {})})
            return jsonify({'success': True, 'message': 'record updated'}), 200
        else:
            return jsonify({'success': False, 'message': 'Bad request parameters!'}), 400
