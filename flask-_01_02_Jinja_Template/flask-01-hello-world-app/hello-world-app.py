from flask import Flask 

app = Flask(__name__)



@app.route("/")
def home():
    return "ZA WARUDO!!!"

@app.route("/bye")
def theend():
    return ("<h1> goodbye, come again!")



if __name__ == '__main__':

    app.run(port=8080)
    # app.run(host= '0.0.0.0', port=8081)

