from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:message>')
def say(message):
    return f"Hi {message}!"

@app.route('/repeat/<int:number>/<string:message>')
def repeat(number, message):
    return message * int(number) 

@app.errorhandler(404)
def not_found_handler(e):
    return "Sorry! No response. Try again."
if __name__ == "__main__":
    app.run(debug = True, port = 5000)

