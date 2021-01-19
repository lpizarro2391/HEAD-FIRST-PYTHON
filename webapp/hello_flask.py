from flask import Flask

from vsearch import search4letters

app = Flask('_hello_flask_')

@app.route('/')

def hello() -> str:
    return 'Hello World from Flask!'

@app.route('/search4')

def do_search() -> str:
    return str(search4letters('life,the universe, and everthing eiry!'))

app.run()
