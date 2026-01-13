from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'
    
    serialize_rules = ('-appearances.episode',)
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.Integer)
    
    appearances = db.relationship('Appearance', backref='episode', cascade='all, delete-orphan')

class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'
    
    serialize_rules = ('-appearances.guest',)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)
    
    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')

class Appearance(db.Model, SerializerMixin):
    __tablename__ = 'appearances'
    
    serialize_rules = ('-episode.appearances', '-guest.appearances')
    
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))
    
    @validates('rating')
    def validate_rating(self, key, rating):
        if rating is None or rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        return rating