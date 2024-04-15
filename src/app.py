"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planet, Vehicles
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.serialize() for u in users]),200 

@app.route('/people')
def get_people():
    people = People.query.all()
    return jsonify([p.serialize() for p in people]), 200

@app.route('/people/<int:people_id>')
def get_people_by_id(people_id):
    person = People.query.get_or_404(people_id)
    return jsonify(person.serialize()), 200

@app.route('/planets')
def get_planets():
    planets = Planet.query.all()
    return jsonify([p.serialize() for p in planets]), 200

@app.route('/planets/<int:planet_id>')
def get_planet_by_id(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    return jsonify(planet.serialize()), 200

@app.route('/vehicles')
def get_vehicles():
    vehicles = Vehicles.query.all()
    return jsonify(v.serialize() for v in vehicles), 200

@app.route('/vehicles/<int:vehicle_id>')
def get_vehicle_by_id(vehicle_id):
    vehicle = Vehicles.query.get_or_404(vehicle_id)
    return jsonify(vehicle.serialize()), 200

""" @app.route('/favorites')
def get_user_favorites():
    user_id= User.query.get('user_id')
    if not user_id:
        return jsonify([])
    user = User.query.get_or_404(user_id)
    favorites = user.favorites
    return jsonify(f.serialize() for f in favorites), 200

@app.route('/favorites/', methods=['POST'])
def add_favourite_by_id(element_id, type):
    favourite = Favorite.query.get_or_404(element_id, type) """





        
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
