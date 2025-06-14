from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contatti")
def contatti():
    return render_template("contatti.html")

@app.route("/calcoli", methods=["GET", "POST"])
def calcoli():
    risultato = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            risultato = num1 + num2
        except:
            risultato = "Errore nei dati"
    return render_template("calcoli.html", risultato=risultato)

if __name__ == "__main__":
    app.run()
