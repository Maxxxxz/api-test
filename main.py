import flask
from flask import request, jsonify

import random
import string
import time
import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

guestbook = []
guestbook.append({"Name": "Michael Cooper", "Signed" : str(time.time())})

@app.route('/', methods=['GET'])
def home():
    return  """
                <h1>Test</h1>
                <p>Testing an API</p>
            """

# Returns a random string between the length of 10 and 100 consisting of all ascii letters.
@app.route('/api/v1/gen', methods=['GET'])
def api_generate():

    res = {
        'response': ''.join(random.choice(string.ascii_letters) for i in range(random.randint(10, 100))),
        'timestamp': time.time()
    }

    return jsonify(res)

@app.route('/api/v1/guestbook/sign', methods=['POST'])
def api_guestbook_sign():
    args = request.args
    print(args)

    try:
        guestbook.append({"Name": args["Name"], "Signed": time.time()})
    except:
        return "Bad Request", 400
    
    return "Post Successful", 201

@app.route('/api/v1/guestbook/view', methods=['GET'])
def api_guestbook_view():
    return jsonify(guestbook)

@app.route('/api/v1/guestbook/remove', methods=['DELETE'])
def api_guestbook_delete():
    args = request.args
    print(args["Name"])
    obj = next( (i for i, person in enumerate(guestbook) if person["Name"] == args["Name"]) , None)
    if obj is None:
        return "Bad Request", 400
    else:
        guestbook.remove(guestbook[0])
        return "Delete Successful", 201

app.run()