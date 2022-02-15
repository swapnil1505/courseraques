from machinetranslation import translator
from flask import Flask, render_template, request
import json
app = Flask("Web Translator",template_folder='templates')

@app.route("/englishToSpanish")
def englishToSpanish():
    textToTranslate = request.args.get('textToTranslate')
    return translator.englishToFrench(textToTranslate)

@app.route("/spanishToEnglish")
def spanishToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

