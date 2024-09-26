from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from dotenv import load_dotenv
from flask_migrate import Migrate


# Load environment variables from .env file
load_dotenv() 




db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_database():
    db.create_all()
    print('Database reated')
   

def create_app():
    app = Flask(__name__)
    
     
    
 
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', "postgresql://username:password@hostname/database")
    app.config['DEBUG'] = os.getenv('DEBUG', default=False) 
    
    # Initialize extensions
    db.init_app(app)
    
    login_manager.init_app(app)  # Initialize Flask-Login with the app
    migrate = Migrate(app, db)
    
    
    @login_manager.user_loader
    def load_user(user_id):
        return Customer.query.get(int(user_id))
    
    # @app.errorhandler(404)
    # def page_not_found(error):
    #     return render_template('404.html')
    
     
    from .views import views
    from .auth import auth
    from .admin import admin
    from .models import Customer, Product, Cart, Order
    
    # Register blueprints
    app.register_blueprint(views, url_prefix='/') # localhost:5000/about-us
    app.register_blueprint(auth, url_prefix='/') # localhost:5000/auth/change-password
    app.register_blueprint(admin, url_prefix='/')
    
    with app.app_context():
        create_database    
    
    
    return app
    
 
    