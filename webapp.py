from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

dictData = {}
dictProcesses = {}
dictCordinates = {}
addClicks = {}
addWords = {}
ip_ports = {}
connected_devices = []

@app.route('/api/computers/<id>/sendClicks', methods=['POST'])
def sendClicks(id):
    d = request.json
    print(d)
    if id in addClicks:
        addClicks[id].append(d)
    else:
        addClicks[id] = [d]
    return 'Success'

@app.route('/api/computers/<id>/getClicks', methods=['GET'])
def getClicks(id):
    if id in addClicks:
        l = addClicks[id]
        del addClicks[id]
        return jsonify({'clicks': l})
    else:
        return jsonify({'clicks': ['']})

@app.route('/api/computers/<id>/getData', methods=['POST'])
def getData(id):
    data = request.json
    dictData[id] = data
    return "Success"

@app.route('/api/computers/<id>/sendData',  methods=['GET', 'POST'])
def send_data(id):
    if id in dictData:
        data = dictData[id]
        return jsonify(data)
    else:
        return "Node not found"

@app.route('/api/computers/<id>/getProcesses', methods=['POST'])
def getProcesses(id):
    data = request.json
    dictProcesses[id] = data
    return 'Success'

@app.route('/api/computers/<id>/sendProcesses', methods=['POST'])
def sendProcesses(id):
    if id in dictProcesses:
        data = dictProcesses[id]
        return jsonify(data)
    else:
        return 'Node not found'

@app.route('/api/computers/<id>/sendCoordinates', methods=['POST'])
def sendCoordinates(id):
    data = request.json
    dictCordinates[id] = data
    return 'Success'

@app.route('/api/computers/<id>/getCoordinates', methods=['GET'])
def getCoordinates(id):
    if id in dictCordinates:
        data = dictCordinates[id]
        return jsonify(data)
    else:
        return jsonify({'x': 100, 'y': 100})

@app.route('/api/computers/<id>/sendKeys', methods=['POST'])
def sendKeys(id):
    data = request.json
    key = data['key']
    if id in addWords:
        addWords[id].append(key)
        return 'Success'
    else:
        addWords[id] = [key]
        return 'Success'

@app.route('/api/computers/<id>/getKeys', methods=['GET'])
def getKeys(id):
    if id in addWords:
        l = addWords[id]
        del addWords[id]
        return jsonify({'keys': l})
    else:
        return jsonify({'keys':['']})

@app.route('/api/computers/<id>/ipPort', methods=['POST'])
def ipPort(id):
    
    if id in ip_ports:
        del ip_ports[id]
        connected_devices.remove(id)
    connected_devices.append(id)
    ip_ports[id] = request.json
    return 'Success'

@app.route('/api/computers/<id>/getIpPort', methods=['GET'])
def getIpPort(id):
    if id in ip_ports:
        print(ip_ports[id])
        return jsonify(ip_ports[id])
    else:
        print('e')
        return jsonify({'ip': 'not_found', 'port': 'not found'})

@app.route('/api/computers/<ssid>/listOfConnectedDevices', methods=['POST'])
def listOfConnectedDevices(ssid):
    data = request.json
    sendList = []
    for key in ip_ports:
        d = ip_ports[key]
        if ssid == d['ssid']:
            sendList.append(key)
    return jsonify({'list': sendList})

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, threaded=True)