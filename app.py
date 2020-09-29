# Hello Universe Project
# This is : Moon 
# Moon will be acting like a API service , delivering basic functionalities 
# and calling other services if neeeded
# ***********************************************
# 2020-09-18  V01
# 2020-09-29  V02
# 2020-09-29  V02 comments
# ***********************************************
from flask import Flask
from flask import request
import requests
import socket
import json
import time

app = Flask(__name__)
from requests.auth import HTTPBasicAuth

identif = 'Hello World - Moon-V02'

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/')
def hello_world():
    return identif

@app.route('/api/v01/id')
def id():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return 'Identif :' + identif + ' - Server :' + hostname + ' in:' + ip_address + ' at:' + current_time + ' !'

@app.route('/api/v01/kill')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'












