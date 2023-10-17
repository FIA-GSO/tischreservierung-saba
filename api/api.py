import flask
from flask import request   # wird benötigt, um die HTTP-Parameter abzufragen
from flask import jsonify   # übersetzt python-dicts in json

from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db' # Hier wird SQLite verwendet
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Optional, um die Warnung zu unterdrücken

db = SQLAlchemy(app)



app.config["DEBUG"] = True  # Zeigt Fehlerinformationen im Browser, statt nur einer generischen Error-Message

@app.route('/', methods=['GET'])
def home():
    return "<h1>Tischreservierung</h1>"
    

def init_db():
    with app.app_context():
        db.create_all()
        with open('schema.sql', 'r') as f:
            db.executescript(f.read())


if __name__ == '__main__':
    init_db()
    app.run()
