from flask import Flask
from flask import request
import requests
import socket
import json
import time

app = Flask(__name__)
from requests.auth import HTTPBasicAuth

identif = 'Hello World - Moon-V01-Temp'


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












