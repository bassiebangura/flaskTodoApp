from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bassiebangura:@localhost:5432/mydb1'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Dog(db.Model):
#   __tablename__ = 'dogs'
#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String(), nullable=False)

#   def __repr__(self):
#     return f"<The Dog's ID is: {self.id}, name: {self.name}>"

# db.create_all()
@app.route('/')

def index():
    return render_template('index.html', data=[{
            'description': 'Todo 1'
        }, {
            'description': 'Todo 2'
        }, {
            'description': 'Todo 3'
        }, {
            'description': 'Todo 4'
        }])
