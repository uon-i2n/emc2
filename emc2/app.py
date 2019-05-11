# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'dev'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


class HelloForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
    remember = BooleanField('Remember me')
    submit = SubmitField()


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/prepare', methods=['GET', 'POST'])
def prepare():
    return render_template('prepare.html')

@app.route('/services', methods=['GET', 'POST'])
def services():
    return render_template('services.html')

@app.route('/community', methods=['GET', 'POST'])
def community():
    return render_template('community.html')

@app.route('/business', methods=['GET', 'POST'])
def business():
    return render_template('business.html')

