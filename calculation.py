
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Calculation"


@app.route('/calc/<int:num1>/<int:num2>', methods=['GET'])
def calculate(num1, num2):
    try:
        add = num1 + num2
        sub = num1 - num2
        mul = num1 * num2
        div = num1 / num2 if num2 != 0 else "undefined (division by zero)"
        
        return f"""
        <h1>Results:</h1>
        <p>{add}</p>
        <p>{sub}</p>
        <p> {mul}</p>
        <p>{div}</p>
        """
    except Exception as e:
        return f"<h1>{e}</h1>"

if __name__ == "__main__":
    app.run(
        debug=True,
        port=3010,
        host="0.0.0.0"
    )