from flask import Flask, render_template, request
import requests
from datetime import date

app = Flask(__name__)
@app.context_processor
def get_current_year():
    return {'today': date.today().strftime('%d-%m-%Y')}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acerca_de')
def acerca_de():
    return render_template('acercaDe.html')

@app.route('/users/')
def users():
    #print(request) VER LOS RESULTADOS QUE  TRAR
    #print(request.__dict__) 
    #print(request.query_string)
    cant = request.args.get('cant' , 3 , type=int)
    response = requests.get(f'https://randomuser.me/api/?results={cant}').json()
    usuarios = response['results']
    return render_template('users.html' , usuarios = usuarios)
