from flask import (Flask, jsonify, make_response, render_template, request, send_file)
from werkzeug import secure_filename

app = Flask("__name__")
app.debug = True

@app.route('/', methods=["GET", "POST"])
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int('5500'), debug=True)
