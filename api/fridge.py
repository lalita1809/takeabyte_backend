from flask import Blueprint, request, jsonify
from model.fridge import Fridge
from model.user import User
from __init__ import db
import logging

fridge_api = Blueprint('fridge_api', __name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Endpoint to add grocery to the fridge
@fridge_api.route('/fridge/add', methods=['POST'])
def add_grocery():
    try:
        # Log the incoming request data and headers
        logger.debug("Request headers: %s", request.headers)
        logger.debug("Request data: %s", request.data)

        # Get the data from the request
        data = request.get_json()
        if not data:
            logger.error("Invalid JSON data")
            return jsonify({'error': 'Invalid JSON data'}), 400

        # Validate the data (ensure grocery and user_id are provided)
        grocery = data.get('grocery')
        user_identifier = 1
        quantity = data.get('quantity')

        if not grocery:
            logger.error("grocery are required")
            return jsonify({'error': 'grocery are required'}), 400

        # Create a new Fridge entry
        new_fridge = Fridge(grocery=grocery, user_id=user_identifier, quantity=data.get('quantity'))
        new_fridge.create()
        return jsonify(new_fridge.read()), 201

    except Exception as e:
        logger.exception("An error occurred while adding grocery")
        return jsonify({'error': str(e)}), 500
  


@fridge_api.route('/api/fridge', methods=['GET'])
def get_fridges():
    try:
        fridges = Fridge.query.all()
        return jsonify([fridge.read() for fridge in fridges])
    except Exception as e:
        logger.exception("An error occurred while fetching fridges")
        return jsonify({'error': str(e)}), 500
    

@fridge_api.route('/fridge/delete', methods=['DELETE'])
def delete_fridges():

    try:
        data = request.get_json()
        # Find the current post from the database table(s)
        fridge = Fridge.query.get(data['id'])
        if fridge is None:
            return {'message': 'Fridges not found'}, 404
        # Delete the post using the ORM method defined in the model
        fridge.delete()
        # Return response
        return jsonify({"message": "Grocery deleted"})
    except Exception as e:
        logger.exception("An error occurred while fetching fridges")
        return jsonify({'error': str(e)}), 500

@fridge_api.route('/fridge/update', methods=['PUT'])
def update_fridges():

    try:
        data = request.get_json()
        # Find the current post from the database table(s)
        fridge = Fridge.query.get(data['id'])
        fridge._quantity = data['quantity']
        if fridge is None:
            return {'message': 'Fridges not found'}, 404
        # Delete the post using the ORM method defined in the model
        fridge.update(data)
        # Return response
        return jsonify({"message": "Grocery update"})
    except Exception as e:
        logger.exception("An error occurred while fetching fridges")
        return jsonify({'error': str(e)}), 500
