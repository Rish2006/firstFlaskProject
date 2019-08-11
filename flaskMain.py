from flask import Flask
app = Flask(__name__)

@app.route("/homepage")
@app.route("/")
def mainPage():
    return "<h1>Hello World!!</h1>"

@app.route("/about")
def aboutPage():
    return "<h1>About Page</h1>"
if __name__=='__main__':
    app.run(debug=True)