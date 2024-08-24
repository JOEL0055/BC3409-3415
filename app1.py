from flask import Flask, render_template, request

app1 = Flask(__name__, template_folder="/Users/joelaiweithai/Downloads/BC3411/html/html_script")

@app1.route("/", methods=["GET", "POST"])
def index():
    return render_template("finance.html")

if __name__ == "__main__":
    # Specify a different port
    app1.run(port=5001)
