"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Creates an instance of a pet to adopt"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)

    name = db.Column(db.String(20), 
                     nullable=False)
    
    species = db.Column(db.Text, 
                        nullable=False)

    photo_url = db.Column(db.Text, default='')

    # todo check when working on form for (baby, young, adult, senior)
    age = db.Column(db.Text, 
                    nullable=False)

    notes = db.Column(db.Text)

    # todo check default choices when working on form
    available = db.Column(db.Boolean, nullable=False, default=True) 

    