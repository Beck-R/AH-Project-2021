from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

dictData = {}

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

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080, threaded=True)
