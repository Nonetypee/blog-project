from flask import Flask
from flask.templating import render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",islem=11)


@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)

