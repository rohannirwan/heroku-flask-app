from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/cloneTest')
def clone_test():
    return 'Hello to clone!!'

if __name__ == '__main__':
    app.run()