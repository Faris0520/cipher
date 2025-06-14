from flask import Flask, render_template, request
from cipher import caesar_encrypt, caesar_decrypt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = ""
    if request.method == "POST":
        text = request.form["text"]
        shift = int(request.form["shift"])
        action = request.form["action"]
        if action == "encrypt":
            hasil = caesar_encrypt(text, shift)
        elif action == "decrypt":
            hasil = caesar_decrypt(text, shift)
    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
