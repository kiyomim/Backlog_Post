from flask import Flask, render_template, request

# Flaskオブジェクトの生成
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    iro = ["red", "blue", "yellow", "green"]
    return render_template("index.html", name=name, iro=iro)

@app.route("/index", methods=["post"])
def post():
    name = request.form["name"]
    iro = ["red", "blue", "yellow", "green"]
    return render_template("index.html", name=name, iro=iro)

if __name__ == "__main__":
    app.run(debug=True)