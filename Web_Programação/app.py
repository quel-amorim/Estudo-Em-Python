from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def iniciar():
    return render_template("index.html")

@app.route("/ds1")
def ds1():
    return render_template("ds1.html")

@app.route("/ds2")
def ds2():
    return render_template("ds2.html")

@app.route("/ds3")
def ds3():
    return render_template("ds3.html")

if __name__ == "__main__":
    app.run(debug=True)
