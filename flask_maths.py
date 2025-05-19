from flask import Flask

api = Flask(__name__)

@api.route('/')
def selfintro():
    return "<h1>Hi I am Meganathan B  &&  I am from Tamabaram. </h1>"

@api.route('/add/<int:num1>/<int:num2>', methods=['GET'])
def add(num1: int, num2: int):
    return f"<h1>Addition: {num1 + num2}</h1>"

if __name__ == '__main__':
    api.run(
        debug=True,
        host="0.0.0.0",
        port=3010
    )
