from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayfairCipher
from cipher.vigenere import VigenereCipher
from cipher.rail_fence import RailFenceCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Initialize ciphers
caesar = CaesarCipher()
playfair = PlayfairCipher()
vigenere = VigenereCipher()
rail_fence = RailFenceCipher()
transposition = TranspositionCipher()

# Home redirects to Caesar as a default
@app.route("/")
def index():
    return render_template("caesar.html")

# --- Caesar ---
@app.route("/caesar")
def caesar_home():
    return render_template("caesar.html")

@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form["plainText"]
    key = int(request.form["key"])
    result = caesar.encrypt(text, key)
    return render_template("caesar.html", encryptedText=result, plainText=text, key=key)

@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form["cipherText"]
    key = int(request.form["key"])
    result = caesar.decrypt(text, key)
    return render_template("caesar.html", decryptedText=result, cipherText=text, key=key)

# --- Playfair ---
@app.route("/playfair")
def playfair_home():
    return render_template("playfair.html")

@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["plainText"]
    key = request.form["key"]
    result = playfair.encrypt(text, key)
    return render_template("playfair.html", encryptedText=result, plainText=text, key=key)

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form["cipherText"]
    key = request.form["key"]
    result = playfair.decrypt(text, key)
    return render_template("playfair.html", decryptedText=result, cipherText=text, key=key)

# --- Vigenere ---
@app.route("/vigenere")
def vigenere_home():
    return render_template("vigenere.html")

@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form["plainText"]
    key = request.form["key"]
    result = vigenere.encrypt(text, key)
    return render_template("vigenere.html", encryptedText=result, plainText=text, key=key)

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form["cipherText"]
    key = request.form["key"]
    result = vigenere.decrypt(text, key)
    return render_template("vigenere.html", decryptedText=result, cipherText=text, key=key)

# --- Rail Fence ---
@app.route("/railfence")
def railfence_home():
    return render_template("rail_fence.html")

@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form["plainText"]
    key = int(request.form["key"])
    result = rail_fence.encrypt(text, key)
    return render_template("rail_fence.html", encryptedText=result, plainText=text, key=key)

@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form["cipherText"]
    key = int(request.form["key"])
    result = rail_fence.decrypt(text, key)
    return render_template("rail_fence.html", decryptedText=result, cipherText=text, key=key)

# --- Transposition ---
@app.route("/transposition")
def transposition_home():
    return render_template("transposition.html")

@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    text = request.form["plainText"]
    key = request.form["key"]
    result = transposition.encrypt(text, key)
    return render_template("transposition.html", encryptedText=result, plainText=text, key=key)

@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    text = request.form["cipherText"]
    key = request.form["key"]
    result = transposition.decrypt(text, key)
    return render_template("transposition.html", decryptedText=result, cipherText=text, key=key)

if __name__ == "__main__":
    app.run(debug=True, port=5050)
