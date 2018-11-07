# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:05:11 2018

@author: ricar
"""

from flask import Flask, render_template
from data import Eventos


app = Flask(__name__)
Eventos = Eventos()
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html', eventos = Eventos)

@app.route('/evento/<string:id>/')
def evento(id):
    return render_template('evento.html', id=id)

if __name__ == '__main__':
    app.run(debug=True)