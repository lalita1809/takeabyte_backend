from flask import Blueprint, request, jsonify
from model.fridge import Fridge
from model.user import User
from __init__ import db
import logging

fridge_api = Blueprint('fridge_api', __name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Endpoint to add ingredients to the fridge
def add_ingredients():
    try:
        # Log the incoming request data and headers
        logger.debug("Request headers: %s", request.headers)
        logger.debug("Request data: %s", request.data)

        # Get the data from the request
        data = request.get_json()
        if not data:
            logger.error("Invalid JSON data")
            return jsonify({'error': 'Invalid JSON data'}), 400

        # Validate the data (ensure ingredients and user_id are provided)
        ingredients_list = data.get('ingredients')
        user_identifier = data.get('user_id')

        if not ingredients_list:
            logger.error("Ingredients are required")
            return jsonify({'error': 'Ingredients are required'}), 400

        if not user_identifier:
            logger.error("user_id is required")
            return jsonify({'error': 'user_id is required'}), 400

        # Create a new Fridge entry
        new_fridge = Fridge(ingredients=ingredients_list, user_id=user_identifier, recipes=data.get('recipes', []))
        new_fridge.create()
        return jsonify(new_fridge.read()), 201

    except Exception as e:
        logger.exception("An error occurred while adding ingredients")
        return jsonify({'error': str(e)}), 500
    
@fridge_api.route('/fridge/add', methods=['POST'])
@fridge_api.route('/fridge', methods=['GET'])
def get_fridges():
    try:
        fridges = Fridge.query.all()
        return jsonify([fridge.read() for fridge in fridges])
    except Exception as e:
        logger.exception("An error occurred while fetching fridges")
        return jsonify({'error': str(e)}), 500
    
    
