import flask
from flask import request
import json
import github


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/getServerIp', methods=['GET'])
def clientIp():
    with open('server_ip.json', 'r') as openfile:
        serverIp = json.load(openfile)
    return serverIp

@app.route('/serverIp/<ip>', methods=['GET'])
def serverIp(ip):
    json_object = json.dumps(ip)
    with open("server_ip.json", "w") as outfile:
        outfile.write(json_object)
    




app.run()