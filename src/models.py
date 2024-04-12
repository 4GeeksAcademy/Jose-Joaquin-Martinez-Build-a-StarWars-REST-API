from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = relationship('Favorite', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class People (db.Model):
    people_id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(50), nullable=False, unique=True)
    height =db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(15))
    skin_color=db.Column(db.String(15))
    eye_color=db.Column(db.String(15))
    birth_year=db.Column(db.String(20))
    gender=db.Column(db.String(20))
    homeworld=db.Column(db.String(30))

class Planet (db.Model):
    planet_id= db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(50), unique=True, nullable=False)
    diameter=db.Column(db.Integer)
    rotation_period=db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity= db.Column(db.Integer)
    population =db.Column(db.Integer)
    climate= db.Column(db.String(50))
    terrain= db.Column (db.String(50))
    surface_water = db.Column(db.Integer)

class Vehicles (db.Model):
    vehicle_id= db.Column(db.Integer, primary_key=True)
    vehicle_name = db.Column(db.String(80), unique=True, nullable=False)
    cargo_capacity= db.Column(db.Integer)
    cost_in_credits= db.Column(db.Integer)
    created= db.Column(db.String(80))
    crew = db.Column(db.Integer)
    length = db.Column(db.Integer)
    manufacturer=db.Column(db.String(80))
    model = db.Column(db.String(80))
    passengers= db.Column(db.Integer)
    vehicle_class= db.Column(db.String(50))
    
class Favorite (db.Model):
    favourite_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(User.user_id))
    character_id = db.Column(db.Integer, ForeignKey(People.people_id))
    planet_id = db.Column(db.Integer, ForeignKey(Planet.planet_id))
    vehicle_id = db.Column(db.Integer, ForeignKey(Vehicles.vehicle_id))
    favourite_type = db.Column (db.String(10), nullable=False)
