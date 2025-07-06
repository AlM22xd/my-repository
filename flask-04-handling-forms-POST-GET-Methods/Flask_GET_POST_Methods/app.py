# Import Flask modules
from flask import Flask, render_template

import math
# Create an object named app

app = Flask(__name__)


# create a function named "lcm" which calculates a least common multiple values of two numbers. 
def lcm (a, b):
    return math.lcm(a, b)

# Create a function named `index` which uses template file named `index.html` 
# send two numbers as template variable to the app.py and assign route of no path ('/') 
@app.route('/')
def index():
    return render_template("index.html", method=["GET"])




# calculate sum of them using "lcm" function, then sent the result to the 
# "result.hmtl" file and assign route of path ('/calc'). 
# When the user comes directly "/calc" path, "Since this is a GET request, LCM has not been calculated" string returns to them with "result.html" file



# Add a statement to run the Flask application which can be debugged.
