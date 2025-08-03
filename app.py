from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route("/hello")
def hello_page():
    return "Hello from test page"

@app.route("/test", methods=["GET", "POST"])
def test_page():
    message = "Click the button below"
    if request.method == "POST":
        message = "You clicked the button!"
    return render_template("test.html", message=message)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
