from flask import Flask
app = Flask(__name__)
def make_bold(function):
    def wrapper_function():
        text = function()
        return f"<b>{text}</b>"
    return wrapper_function
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route("/bye")
@make_bold
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run(debug=True)
