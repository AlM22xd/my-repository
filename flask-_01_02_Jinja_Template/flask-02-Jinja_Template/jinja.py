from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome"


@app.route("/head")
def head():
    render_template("index.html")
    return render_template("index.html", number1=123, number2=777)        

@app.route("/sum")
def sum():

    val1 = 55
    val2 = 125
    mysum = val1 + val2
    return render_template("body.html", value1 = val1, value2 = val2, sum = mysum)


if __name__== "__main__":
    app.run(host="0.0.0.0")