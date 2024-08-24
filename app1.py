from flask import Flask, render_template

app1 = Flask(__name__)

@app1.route("/", methods=["GET", "POST"])
def index():
    return render_template("finance.html")

if __name__ == "__main__":
    app1.run(port=5001)
