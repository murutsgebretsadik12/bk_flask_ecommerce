from flask import Blueprint, render_template

views = Blueprint('views', __name__)



    
@views.route('/')
def home():
    return render_template('home.html')



@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')