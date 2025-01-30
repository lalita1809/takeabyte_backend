
from flask import Blueprint, request, jsonify
from model.natcountrysearch import CountryDish
from __init__ import db
import logging
import random


country_api = Blueprint('country_api', __name__)


# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Endpoint to add a new country dish
@country_api.route('/api/add', methods=['POST'])
def add_country_dish():
   try:
       logger.debug("Request headers: %s", request.headers)
       logger.debug("Request data: %s", request.data)


       data = request.get_json()
       if not data:
           logger.error("Invalid JSON data")
           return jsonify({'error': 'Invalid JSON data'}), 400


       country = data.get('country')
       dish = data.get('dish')
       description = data.get('description')


       if not country or not dish or not description:
           logger.error("Country, dish, and description are required")
           return jsonify({'error': 'Country, dish, and description are required'}), 400


       new_country_dish = CountryDish(country=country, dish=dish, description=description)
       new_country_dish.create()
       return jsonify(new_country_dish.read()), 201


   except Exception as e:
       logger.exception("An error occurred while adding a country dish")
       return jsonify({'error': str(e)}), 500


# Endpoint to get all country dishes
@country_api.route('/api/countries', methods=['GET'])
def get_country_dishes():
   try:
       country_dishes = CountryDish.query.all()
       return jsonify([country_dish.read() for country_dish in country_dishes])
   except Exception as e:
       logger.exception("An error occurred while fetching country dishes")
       return jsonify({'error': str(e)}), 500


# Endpoint to filter countries by dish
@country_api.route('/api/countries/filter', methods=['GET'])
def filter_country_dishes():
   try:
       dish = request.args.get('dish')
       if not dish:
           return jsonify({'error': 'Dish parameter is required'}), 400
      
       country_dishes = CountryDish.query.filter(CountryDish._dish == dish).all()
       return jsonify([country_dish.read() for country_dish in country_dishes])
   except Exception as e:
       logger.exception("An error occurred while filtering country dishes")
       return jsonify({'error': str(e)}), 500


# Endpoint to update an existing country dish
@country_api.route('/api/countries/update', methods=['PUT'])
def update_country_dish():
   try:
       data = request.get_json()
       country_dish = CountryDish.query.get(data['id'])
       if country_dish is None:
           return jsonify({'message': 'Country dish not found'}), 404


       _country = data.get('country', country_dish._country)
       _dish = data.get('dish', country_dish._dish)
       _description = data.get('description', country_dish._description)


       country_dish.update(country=_country, dish=_dish, description=_description)
       return jsonify(country_dish.read())
   except Exception as e:
       logger.exception("An error occurred while updating country dish")
       return jsonify({'error': str(e)}), 500


# Endpoint to delete a country dish
@country_api.route('/api/countries/delete', methods=['DELETE'])
def delete_country_dish():
   try:
       data = request.get_json()
       country_dish = CountryDish.query.get(data['id'])
       if country_dish is None:
           return jsonify({'message': 'Country dish not found'}), 404


       country_dish.delete()
       return jsonify({"message": "Country dish deleted"})
   except Exception as e:
       logger.exception("An error occurred while deleting country dish")
       return jsonify({'error': str(e)}), 500


# Endpoint to get a random country dish (from the 5 sample data dishes)
@country_api.route('/api/random', methods=['GET'])
def get_random_country_dish():
   try:
       # Query for all country dishes (or you can hard-code 5 sample dishes here if needed)
       country_dishes = CountryDish.query.all()
      
       # Ensure there are at least 5 dishes to randomly select from
       if len(country_dishes) < 5:
           return jsonify({'error': 'Not enough country dishes in the database'}), 400


       # Randomly select one dish from the list
       random_dish = random.choice(country_dishes)
       return jsonify(random_dish.read())


   except Exception as e:
       logger.exception("An error occurred while fetching a random country dish")
       return jsonify({'error': str(e)}), 500