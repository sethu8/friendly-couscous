from flask import Flask, render_template, request

app = Flask(__name__)

def decode_message(secret):

    if not secret.strip():
        return ""

    first_word = secret.strip().split()[0]
    shift = len(first_word)

    decoded = ""

    for ch in secret:

        if ch == " ":
            decoded += " "

        elif ch.isupper():
            decoded += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))

        elif ch.islower():
            decoded += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))

        else:
            decoded += ch

    return decoded


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":
        secret = request.form["secret"]
        result = decode_message(secret)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
