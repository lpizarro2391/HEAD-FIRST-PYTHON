from flask import Flask, render_template

from vsearch import search4letters

app = Flask('_hello_flask_')

@app.route('/')

def hello() -> str:
    return 'Hello World from Flask!'

@app.route('/search4')

def do_search() -> str:
    return str(search4letters('life,the universe, and everthing eiry!'))

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                            the_title='Welcome to the search4letters on the web')


app.run()
