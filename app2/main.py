from flask import Flask, render_template


app = Flask(__name__)
#wtf
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/form-domicilio")
def domicilioForm():
    return render_template("form-domicilio.html")

@app.route("/form-reserva")
def reservaForm():
    return render_template("form-reserva.html")

if __name__ == '__main__':
    app.run(port=5001, debug=True)