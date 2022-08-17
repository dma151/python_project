"""• You’ve been hired as an entry level coder for the IMF, an elite, top-secret 
    espionage and covert operations agency that handles dangerous and highly 
    sensitive international missions that have been deemed "impossible". Your mission, 
    should you choose to accept it, is to write a program that can scan top-secret 
    documents and replace any/all instances of words (or phrases) that the user 
    inputs with asterisks. Be sure only the new file remains when you’re done."""

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/edit', methods=["POST"])
def edit():
    if request.method == 'POST':
        try:
            file_path = request.form['path']
            keyword = request.form['keyword']
            with open(file_path, 'r') as doc:
                file_to_parse = doc.read()

            file_to_parse = file_to_parse.replace(keyword, "*****")
            with open(file_path, 'w') as new_doc:
                new_doc.write(file_to_parse)
            
            return redirect('/')
        except:
            return("something went wrong")
if __name__ == "__main__":
    app.run(debug=True)