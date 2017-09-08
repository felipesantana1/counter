from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "IamCool"

@app.route('/')

def displayIndex():

    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0

    return render_template('index.html')

@app.route('/count')

def increaseCount():

    session['counter'] += 1

    return redirect('/')

@app.route('/clear')

def clearCount():

    session.pop('counter')
    session['counter'] = 0

    return redirect('/')

app.run(debug=True)