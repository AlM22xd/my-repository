#Import Flask modules
from flask import Flask, redirect, url_for, render_template


#Create an object named app 
app = Flask(__name__)

# Create a function named home which returns a string 'This is home page for no path, <h1> Welcome Home</h1>' 
# and assign route of no path ('/')
@app.route('/')
def home():
    home_message = ("This is home page for no path, <h1> Welcome Home</h1>")
    message = "This is home page for no path, <h1> Welcome Home</h1>"
    return home_message


# Create a function named about which returns a formatted string '<h1>This is my about page </h1>' 
# and assign to the static route of ('about')
@app.route('/about')
def about():
    about_message = ("<h1> This is my about page </h1>")
    return about_message
# Create a function named error which returns a formatted string '<h1>Either you encountered an error or you are not authorized.</h1>' 
# and assign to the static route of ('error')
@app.route('/error')
def error():
    error_message = ("<h1>Either you encountered an error or you are not authorized.</h1>")
    return error_message

# Create a function named admin which redirect the request to the error path 
# and assign to the route of ('/admin')
@app.route('/admin')
def admin():
    return redirect(url_for("error"))



# Create a function named greet which return formatted inline html string 
# and assign to the dynamic route of ('/<name>')
# HTML:
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Greeting Page</title>
# </head>
# <body>
#     <h1>Hello, { name }!<h1>
#     <h1>Welcome to my Greeting Page</h1>
# </body>
# </html>
@app.route('/<name>')
def greet(name):
    inline_html = f"""  
<!DOCTYPE html>
<html>
<head>
    <title>Greeting Page</title>
</head>
<body>
    <h1>Hello, { name }!<h1>
    <h1>Welcome to my Greeting Page</h1>
</body>
</html>

""" 

    return inline_html



# Create a function named greet_admin which redirect the request to the hello path with param of 'Master Admin!!!!' 
# and assign to the route of ('/greet-admin')
@app.route('/greet-admin')
def greet_admin():
    return redirect(url_for("greet", name="Master Admin!!!!"))
