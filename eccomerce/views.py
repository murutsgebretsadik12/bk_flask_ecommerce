from flask import Blueprint, render_template
from .models import Product, Cart
from flask_login import login_required, current_user
views = Blueprint('views', __name__)



    
@views.route('/')
def home():

    items = Product.query.filter_by(flash_sale=True).limit(8).all()

    return render_template('home.html', items=items, cart=Cart.query.filter_by(customer_link=current_user.id).all()
                           if current_user.is_authenticated else [])



@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')