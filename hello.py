# March 13, 2017 Ningsong Shen

# When will the others see this?

from flask import Flask, url_for, render_template, request
from peewee import *

# Creating a database (just learned!!)
db = SqliteDatabase('ideas.db')

# define the idea model
class Idea(Model):
    # accepts a text field
    text = CharField()
    
# connect to the database
db.connect()


# If the idea model doesn't exist, create it
if Idea.table_exists == False:    
    db.create_tables([Idea])


app = Flask(__name__)

# homepage, has a form
@app.route('/', methods=['GET', 'POST'])
def index():
    list_ideas = []
    for thing in Idea.select():
        # debuging print(thing.text)
        list_ideas.append(thing.text)
    return render_template('index.html', ideas=list_ideas)
 
# redirect back to home 
@app.route('/thanks/', methods=['POST'])   
def thanks():
    idea = request.form['idea']
    add_thing = Idea(text=idea)
    add_thing.save()
    return render_template('thanks.html')
    
    
    
@app.route('/matrice/')
def matrice():
    return('Calculating matrices here')
    
@app.route('/midpoint/')
def midpoint():
    return('Calculating midpoints here')