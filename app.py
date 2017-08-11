from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import json
import requests
 
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

def getExchangeRates():
    rates = []
    response = requests.get('http://api.fixer.io/latest')
    rdata = json.loads(response.text, parse_float=float)
 
    rates.append( rdata['rates']['USD'] )
    rates.append( rdata['rates']['GBP'] )
    rates.append( rdata['rates']['HKD'] )
    rates.append( rdata['rates']['AUD'] )
    return rates

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/products")
def products():
    return render_template('products.html')
 
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/order_confirm", methods=['GET', 'POST'])
def order_confirm():
    return render_template('order_confirm.html', color=request.form['color'], quant=request.form['quant'], size=request.form['size'], model=request.form['model'], price=request.form['price'])

@app.route("/chart")
def chart():
    rates = getExchangeRates()
    return render_template('chart.html',**locals())
 
if __name__ == "__main__":
    app.run()
