from flask import Flask, url_for, render_template, request
app = Flask(__name__)


ideas = ['matrices', 'pythagorean theorem']

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', ideas=ideas)
   
@app.route('/thanks/', methods=['POST'])   
def thanks():
    idea = request.form['idea']
    ideas.append(idea)
    return render_template('thanks.html')