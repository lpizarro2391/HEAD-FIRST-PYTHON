import mysql.connector
from flask import Flask, render_template,request,escape
from vsearch import search4letters
from BDcm import UseDatabase


app = Flask(__name__)
#definir las caracteristicas de conexion#
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }

def log_request(req: 'flask_request', res: str) -> None:
    #log details of the web request and the results.#
 #esta declaracion trabaja con la base de datos y regresa un cursor#
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert log
            (phrase, letters, ip, browser_string, results)
            values
            (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                            req.form['letters'],
                            req.remote_addr,
                            req.user_agent.browser,
                            res, ))

@app.route('/search4',methods=['POST'])
def do_search() ->'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results: '
    results = str(search4letters(phrase, letters))
    log_request(request,results)
    return  render_template('results.html',
                            the_phrase=phrase,
                            the_letters=letters,
                            the_title=title,
                            the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                            the_title='Welcome to the search4letters on the web')

@app.route('/viewlog')
def view_the_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL= """select phrase, letters, ip, browser_string, results 
                 from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()

    titles = ('Phrase','Letters','Remote_addr','User_agent','Results')
    return render_template('viewlog.html',
                            the_titles= 'View Log',
                            the_row_titles=titles,
                            the_data=contents,)

app.secret_key = 'YouWillNeverGuessMySecretkey'

if __name__ == '__main__':
    app.run(debug=True)
