# Python Project: DocSlasher

### Prompt
You’ve been hired as an entry level coder for the IMF, an elite, top-secret espionage and covert operations agency that handles dangerous and highly sensitive international missions that have been deemed "impossible". Your mission, should you choose to accept it, is to write a program that can scan top-secret documents and replace any/all instances of words (or phrases) that the user inputs with asterisks. Be sure only the new file remains when you’re done.

## Motivation

This prompt was chosen because I as a coder have always been interested in the deconstruction and construction of things, including code. As the prompt suggests, a file is put into the code, scanned for keywords, and outputted as a new file with some edits made.

## Framework Used

Flask
Python3
Pylint

## How to Use

- Copy the repo
- Give permission to the app.py script to run the shebang,
    - i.e. chmod 744 app.py or chmod u+x app.py
- Run the program ./app.py
- Currently flask uses port 5000 so check on http://127.0.0.1:5000 and test away

## Future Adaptations

- Give the program the ability to parse .pdf and .doc files
    - Current MVP only works with .txt files
    - There is a branch attempting to work with .pdf but is in the works
- Better UI
    - A preview of the document and a before/after panel look

