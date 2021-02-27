from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

dictData = {}

@app.route('/api/computers/<id>/getData', methods=['POST'])
def getData(id):
    try:
        data = request.json
        dictData[id] = data
        return "Success"
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
def send_all_data():
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
