from flask import render_template, Blueprint

hangman = Blueprint('templates',__name__, template_folder='site_templates')

@hangman.route('/')
@hangman.rounte('/home')
def index():
    return render_template('index.html')