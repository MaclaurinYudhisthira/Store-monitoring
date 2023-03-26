from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import view
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)

with app.app_context():
    db.create_all()

# Register Blueprint
app.register_blueprint(view)

if __name__ == '__main__':
    app.run(debug=True)