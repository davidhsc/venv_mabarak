from flask import Flask

app = Flask(__name__)

@app.route('/')
def principal():
    return {'mensaje': 'hola mundo', 'success':True}

@app.route('/api')
def checkapi():
    return {'mensaje': 'API LISTA', 'success':True}

@app.route('/api/saludo')
def checkapisaludo():
    return {'mensaje': 'API, HOLA MUNDO', 'success':True}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')