from flask import Flask
from random import randrange
app = Flask(__name__)
current_number=randrange(10)

@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"



# def make_bold(function):
#     def wrapper_function():
#         text = function()
#         return f"<b>{text}</b>"
#     return wrapper_function

# def make_emphasis(function):
#     def wrapper():
#         return "<em>" + function() + "</em>"
#     return wrapper

# def make_underlined(function):
#     def wrapper_function():
#         text = function()
#         return f"<u>{text}</u>"
#     return wrapper_function


# @app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underlined
# def say_bye():
#     return "Bye"

@app.route("/<int:number>")
def guss (number):
    if number==current_number:
      return "<p>You got it!!</p>" \
             "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif number < current_number:
        return "<p>Too low!!</p>" \
             "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    

    else:
        return "<p>Too high!!</p>" \
             "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    

      

      
if __name__ == "__main__":
    app.run(debug=True)


