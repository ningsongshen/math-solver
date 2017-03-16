# March 13, 2017 Ningsong Shen

# When will the others see this?

from flask import Flask, url_for, render_template, request, flash, redirect
from peewee import *
from flask_admin import Admin
import math

FLASK_DEBUG = 1

# Creating a database (just learned!!)
db = SqliteDatabase('ideas.db')

# define the idea model
class Idea(Model):
    # accepts a text field
    text = CharField()
    
# connect to the database
db.connect()


# If the idea model doesn't exist, create it   
# db.create_tables([Idea])


app = Flask(__name__)
admin = Admin(app, name='math-solver') #template_mode='bootstrap3')
app.secret_key = '7eb85145bcc37b282fa25df32c6f92dfb5d1f5f2f6057913'

# homepage, has a form
@app.route('/', methods=['GET', 'POST'])
def index():
    list_ideas = []
    for thing in Idea.select():
        # debuging print(thing.text)
        list_ideas.append(thing.text)
     
    if request.method == 'POST':
        flash('Thanks for your input!')
        idea = request.form['idea']
        add_thing = Idea(text=idea)
        add_thing.save()
        return redirect(url_for('index'))
    return render_template('index.html', ideas=list_ideas)
 
# NOT NEEDED ANYMORE
# # redirect back to home 
# @app.route('/thanks/', methods=['POST'])   
# def thanks():
    # idea = request.form['idea']
    # add_thing = Idea(text=idea)
    # add_thing.save()
    # return render_template('thanks.html')
    
    
    
@app.route('/matrice/', methods=['GET', 'POST'])
def matrice():
    if request.method == 'POST':
        flash('This thing doesn\'t work yet')
        return render_template('matrices.html')
    return(render_template('matrices.html'))
    
@app.route('/midpoint/')
def midpoint():
    return('Calculating midpoints here')
    
@app.route('/pythagorean/', methods=['GET', 'POST'])
def pythagorean():
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = math.sqrt(a**2 + b**2)
            flash('Result: ' + str(c)) 
        except ValueError:
            flash('NOT A NUMBER')
    return render_template('pythagorean.html')
    
    
    
    
    
    