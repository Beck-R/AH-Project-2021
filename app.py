from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

dictData = {}

@app.route('/api/computers/<id>/getData', methods=['POST'])
def getData(id):
    try:
        data = request.json
        data = json.loads(data)
        if data != None:
            data.pop("version")
            key = list(data.keys())[0]
            print(key)
            if id not in dictData:
                dictData[id] = {}
            dictData[id][key] = data[key]
            return f"Success! Added key {key} to data for node {id}!"
        return f"Received request, but something might have gone wrong! Please make sure the body is formatted as JSON."
    except Exception as e:
        return formatErr(e)

@app.route('/api/computers/<id>/sendData',  methods=['GET', 'POST'])
def send_data(id):
    try:
        if id in dictData:
            data = dictData[id]
            return jsonify(data)
        else:
            return "Node not found"
    except Exception as e:
        return formatErr(e)

@app.route('/api/computers/all/sendData',  methods=['GET'])
def send_all_data_json():
    try:
        data = dictData
        return jsonify(data)
    except Exception as e:
        return formatErr(e)

def formatErr(e): 
    return f"Error: \n\n {e}"


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080, threaded=True)
