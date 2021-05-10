from flask import Flask

app = Flask(__name__)

@app.route('/')
def principal():
    return {'mensaje': 'hola mundo', 'success':True}

if __name__ == '__main__':
    app.run(debug=True)