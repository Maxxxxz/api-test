import flask
from flask import request, jsonify

import random
import string
import time
import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return  """
                <h1>Test</h1>
                <p>Testing an API</p>
            """

# Returns a random string between the length of 10 and 100 consisting of all ascii letters.
@app.route('/api/v1/gen', methods=['GET'])
def api_generate():
    # res = []

    # res.append({
    #     'response': ''.join(random.choice(string.ascii_letters) for i in range(random.randint(10, 100)))
    # })

    res = {
        'response': ''.join(random.choice(string.ascii_letters) for i in range(random.randint(10, 100))),
        'timestamp': time.time()
    }

    return jsonify(res)

app.run()