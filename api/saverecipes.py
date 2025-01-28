from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Define the Recipe model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    time = db.Column(db.Integer, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the route to save a recipe
@app.route('/save_recipe', methods=['POST'])
def save_recipe():
    data = request.get_json()
    new_recipe = Recipe(
        title=data['title'],
        ingredients=data['ingredients'],
        instructions=data['instructions'],
        time=data['time']
    )
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({"message": "Recipe saved successfully"}), 201

# Define the route to get all recipes
@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify([{
        'title': recipe.title,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions,
        'time': recipe.time
    } for recipe in recipes])