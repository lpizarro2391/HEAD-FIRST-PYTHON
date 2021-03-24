import mysql.connector
from flask import Flask, render_template,request,escape
from vsearch import search4letters
from BDcm import UseDatabase

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
	#definir las caracteristicas de conexion#
    dbconfig = {'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB', }

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    
 #esta declaracion trabaja con la base de datos y regresa un cursor#
    with UseDatabase(dbconfig) as cursor:
        _SQL = """insert log
            (phrase, letters, ip, browser_string, results)
            values
            (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                            req.form['letters'],
                            req.remote_addr,
                            req.user_agent.browser,
                            res, ))
        conn.commit()
        cursor.close()
        conn.close()

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
    contents= []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data','Remote_addr','User_agent','Results')
    return render_template('viewlog.html',
                            the_titles= 'View Log',
                            the_row_titles=titles,
                            the_data=contents,)
app.run(debug=True)
