from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from core.scanner.Scanner import lookup, dorking, omega
from core.etc.drop_downlist import Form, choices

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scan')
def page1():
    return render_template('page1.html')


@app.route('/whois')
def whois():
    return render_template('typebars/whois.html')


@app.route('/googledork')
def googledork():
    form = Form()
    return render_template('typebars/googledorks.html', form=form)


@app.route('/both')
def both():
    form = Form()
    return render_template('typebars/both.html', form=form)


# result of whois scan
@app.route('/whois', methods=['POST'])
def scan1():
    hostname = request.form['hostname']
    x_response, y_response = lookup(hostname)
    return render_template("results/whois_result.html", x_res=x_response, y_res=y_response, length = len(x_response))


# result of google dorks
@app.route('/googledork', methods=['POST'])
def scan2():
    hostname = request.form['hostname']
    form = Form()
    choice_made = form.dorksList.data
    pos = choices.index(choice_made)
    response = dorking(hostname, pos)
    return render_template("results/dork_result.html", response=response)


# result of both scans
@app.route('/both', methods=['POST'])
def scan3():
    hostname = request.form['hostname']
    form = Form()
    choice_made = form.dorksList.data
    pos = choices.index(choice_made)
    x_response, y_response, gdork_response = omega(hostname, pos)
    return render_template("results/both_result.html", x_res=x_response, y_res=y_response, length=len(x_response), g_response=gdork_response)
