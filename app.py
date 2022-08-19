#!/usr/bin/env python3
"""
This Python Script accepts a .txt file from a user and censors
selected keywords with asterisks.
"""

import traceback
from flask import Flask, render_template, request, redirect
import requests
import PyPDF2

app = Flask(__name__)
KANYE_URI = "https://api.kanye.rest/"


@app.route('/')
def index():
    """Default landing page that renders index template"""
    return render_template('index.html')


@app.route('/edit', methods=["POST"])
def edit():
    """Function attempts to access specified file from path and replace
    given keyword with asterisks"""
    if request.method == 'POST':
        try:
            file_path = request.form['path']
            keyword = request.form['keyword']
            with open(file_path, 'r', encoding="utf-8") as doc:
                file_to_parse = doc.read()

            file_to_parse = file_to_parse.replace(keyword, "*****")
            with open(file_path, 'w', encoding="utf-8") as new_doc:
                new_doc.write(file_to_parse)
            return redirect('/confirmation')
        except FileNotFoundError:
            return traceback.print_exc()


@app.route('/pdfedit', methods=["POST"])
def pdfedit():
    """Function attempts to access specified file from path and replace
    given keyword with asterisks"""
    if request.method == 'POST':
        try:
            file_path = request.form['path']
            keyword = request.form['keyword']
            with open("/static/{file_path}", "w") as new_doc:
                pdf_file_obj = open(file_path, "rb")
                pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
                for x in range(pdf_reader.numPages):
                    page_obj = pdf_reader.getPage(x)
                    page_text = page_obj.extract_text()
                    page_text = page_text.replace(keyword, "*****")
                    new_doc.write(page_text)
                return redirect('/confirmation')
        except FileNotFoundError:
            return traceback.print_exc()


@app.route('/confirmation')
def confirm():
    """This function renders a completion page for the edit"""
    return render_template('confirmation.html')


@app.route('/kanye')
def kanye_quote():
    """Function is a api call to Kanye quotes API"""
    resp = requests.get(KANYE_URI)
    quote = resp.json()["quote"]
    return render_template('index.html', quote=quote)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
