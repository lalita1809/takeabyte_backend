from flask import request, jsonify
from __init__ import app, db
from recipe import Recipe

@app.route('/save_recipe', methods=['POST'])
def save_recipe():
    data = request.get_json()
    new_recipe = Recipe(
        title=data['title'],
        ingredients=data['ingredients'],
        instructions=data['instructions'],
        time=data.get('time')  # Use get to handle optional field
    )
    if new_recipe.create():
        return jsonify({"message": "Recipe saved successfully"}), 201
    else:
        return jsonify({"message": "Error saving recipe"}), 500

@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify([recipe.read() for recipe in recipes])