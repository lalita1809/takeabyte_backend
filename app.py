from flask import jsonify, request
from flask_cors import CORS
from __init__ import app
from recipe import Recipe

CORS(app, supports_credentials=True, origins='*')  # Allow all origins (*)

@app.route('/save_recipe', methods=['POST'])
def save_recipe():
    data = request.get_json()
    title = data.get('dish')
    ingredients = data.get('ingredients')
    instructions = data.get('instructions')
    time = data.get('time')

    if not title or not ingredients or not instructions:
        return jsonify({"message": "Missing required fields"}), 400

    recipe = Recipe(title=title, ingredients=ingredients, instructions=instructions, time=time)
    created_recipe = recipe.create()

    if created_recipe:
        return jsonify({"message": "Recipe saved successfully"}), 201
    else:
        return jsonify({"message": "Failed to save recipe"}), 500

@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify([{"title": recipe.title, "ingredients": recipe.ingredients, "instructions": recipe.instructions} for recipe in recipes]), 200

# Sample endpoints for other content
@app.route('/bailey')
def get_bailey():
    InfoDb = [{
        "FirstName": "Bailey",
        "LastName": "Leeder",
        "DOB": "June 7",
        "Residence": "San Diego",
        "Email": "baileyleeder101@gmail.com",
        "Owns_Cars": ["none"]
    }]
    return jsonify(InfoDb)

@app.route('/lalita')
def get_lalita():
    InfoDb = [{
        "FirstName": "Lalita",
        "LastName": "Narayanan",
        "DOB": "September 18",
        "Residence": "San Diego",
        "Email": "lalitan34221@stu.powayusd.com",
        "Owns_Cars": ["none"]
    }]
    return jsonify(InfoDb)

@app.route('/joanna')
def get_joanna():
    InfoDb = [{
        "FirstName": "Joanna",
        "LastName": "Hu",
        "DOB": "April 26",
        "Residence": "San Diego",
        "Email": "joanna.y.hu@gmail.com",
        "Owns_Cars": ["none"]
    }]
    return jsonify(InfoDb)

@app.route('/yuva')
def get_yuva():
    InfoDb = [{
        "FirstName": "Yuva",
        "LastName": "Bala",
        "DOB": "February 14",
        "Residence": "San Diego",
        "Email": "yuvabala214@gmail.com",
        "Owns_Cars": ["Tesla-Model-3", "Tesla-Model-X", "Cybertruck"]
    }]
    return jsonify(InfoDb)

@app.route('/ahmad')
def get_ahmad():
    InfoDb = [{
        "FirstName": "Ahmad",
        "LastName": "Imran",
        "DOB": "May 28",
        "Residence": "San Diego",
        "Email": "ahmadimran.2009@outlook.ie",
        "Owns_Cars": ["none"]
    }]
    return jsonify(InfoDb)

@app.route('/nathan')
def get_nathan():
    InfoDb = [{
        "FirstName": "Nathan",
        "LastName": "Tejidor",
        "DOB": "October 7",
        "Residence": "San Diego",
        "Email": "nateji5@gmail.com",
        "Owns_Cars": ["none"]
    }]
    return jsonify(InfoDb)

@app.route('/')
def say_hello():
    html_content = """
    <html>
    <head>
        <title>Hello</title>
    </head>
    <body>
        <h2>Hello, World!</h2>
    </body>
    </html>
    """
    return html_content