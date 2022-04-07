from flask import Flask, redirect, url_for, render_template, request
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = "party_app"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class users(db.Model):
    def __init__(self,name,arrival,bringing):
        self.name = name
        self.arrival = arrival
        self.bringing = bringing

    _id = db.Column("id",db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    arrival = db.Column(db.String(100))
    bringing = db.Column(db.String(100))

    

@app.route("/", methods=["POST","GET"] )
def main():
    if request.method == "POST":
        #gets info from form
        guest_name = request.form["nm"]
        guest_arrival = request.form["arrival"]
        guest_brings = request.form["bringing"]
        #adds info to database
        guest = users(guest_name,guest_arrival,guest_brings)
        db.session.add(guest)
        db.session.commit()

        return render_template('home.html',guests = users.query.all())
    else:
        return render_template('home.html',guests = users.query.all())

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)