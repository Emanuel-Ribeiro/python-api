import datetime
import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'hostname': socket.gethostname()
    })

@app.route('/api/v1/healthz')

def healthz():
    return jsonify({
        'status': 'UP'
    }), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0")
