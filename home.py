from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/choice/", methods=["POST", "GET"])
def makeChoice():
    username = request.form["username"]
    choice = request.form["choice"]
    message = request.form["message"]
    print(username + " " + choice + "\n" + message)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)