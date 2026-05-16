from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Halo Dunia!</h1>"

@app.route("/rahasia")
def rahasia():
    return """
    <h1>🎉 Halaman Rahasia 🎉</h1>
    <p>Selamat datang di halaman tersembunyi!</p>
    """

app.run()
