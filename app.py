from flask import Flask
from models import db
from controllers.userController import usersBp
from controllers.postController import postsBp

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:''@localhost/test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

# Register blueprints
app.register_blueprint(usersBp, url_prefix='/users')
app.register_blueprint(postsBp, url_prefix='/posts')

if __name__ == '__main__':
    app.run(debug=True)
