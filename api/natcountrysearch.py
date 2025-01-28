import random
from flask import Blueprint, request, jsonify, current_app, g
from flask_restful import Api, Resource
from __init__ import app
from model.natcountrysearch import CountryDish  # Model for the Country object (you would create this model in a separate file)
from api.jwt_authorize import token_required


# Blueprint setup
country_api = Blueprint('country_api', __name__, url_prefix='/api')


# Api setup
api = Api(country_api)




countries_data = [
   {"country": "Italy", "dish": "Pizza", "description": "Pizza is a traditional Italian dish consisting of a usually round, flat base of leavened wheat-based dough topped with tomatoes, cheese, and often various other ingredients."},
   {"country": "Japan", "dish": "Sushi", "description": "Sushi is a Japanese dish of prepared vinegared rice accompanied by various ingredients, such as seafood, vegetables, and occasionally tropical fruits."},
   {"country": "Mexico", "dish": "Tacos", "description": "Tacos are a traditional Mexican dish consisting of a small hand-sized tortilla, typically filled with a variety of ingredients such as beef, chicken, or vegetables."},
   {"country": "India", "dish": "Biryani", "description": "Biryani is a mixed rice dish originating from the Indian subcontinent, made with Indian spices, rice, and typically either meat or vegetables."},
   {"country": "France", "dish": "Baguette", "description": "The Baguette is a long, narrow loaf of French bread that is typically crispy on the outside and soft on the inside."},
   {"country": "China", "dish": "Peking Duck", "description": "Peking Duck is a famous Chinese dish known for its crispy skin and tender meat, often served with pancakes and hoisin sauce."},
   {"country": "United States", "dish": "Hamburger", "description": "The Hamburger is a popular American dish consisting of a ground beef patty served inside a bun, often with cheese, lettuce, and other toppings."},
   {"country": "Thailand", "dish": "Pad Thai", "description": "Pad Thai is a stir-fried rice noodle dish from Thailand, typically made with shrimp or chicken, tofu, peanuts, and a savory sauce."},
   {"country": "Brazil", "dish": "Feijoada", "description": "Feijoada is a traditional Brazilian stew of black beans with pork or beef, often served with rice, greens, and orange slices."},
   {"country": "Greece", "dish": "Moussaka", "description": "Moussaka is a Greek dish made with layers of eggplant, minced meat, and béchamel sauce, baked to perfection."},
   {"country": "South Korea", "dish": "Kimchi", "description": "Kimchi is a staple in Korean cuisine, consisting of fermented vegetables, primarily napa cabbage, and seasoned with chili pepper, garlic, and other spices."},
   {"country": "Spain", "dish": "Paella", "description": "Paella is a traditional Spanish rice dish originating from Valencia, made with saffron, seafood, and a variety of meats."},
   {"country": "Turkey", "dish": "Kebabs", "description": "Kebabs in Turkey typically refer to skewered and grilled meats, often lamb or chicken, served with rice and vegetables."},
   {"country": "Argentina", "dish": "Asado", "description": "Asado is a traditional Argentine barbecue, featuring a variety of meats, including beef, sausages, and ribs, cooked over an open flame."},
   {"country": "Vietnam", "dish": "Pho", "description": "Pho is a Vietnamese soup consisting of broth, rice noodles, herbs, and typically either beef or chicken."},
   {"country": "Egypt", "dish": "Koshari", "description": "Koshari is Egypt’s national dish, made with lentils, rice, macaroni, topped with a tomato sauce and fried onions."},
   {"country": "Morocco", "dish": "Couscous", "description": "Couscous is a staple in Moroccan cuisine, consisting of steamed semolina wheat granules served with a stew of meat and vegetables."},
   {"country": "Russia", "dish": "Borscht", "description": "Borscht is a traditional Eastern European soup made with beets, often served with sour cream and accompanied by bread."},
   {"country": "Australia", "dish": "Meat Pie", "description": "The Meat Pie is a savory pastry filled with minced meat, gravy, mushrooms, onions, and cheese, commonly found in Australian cuisine."},
   {"country": "Peru", "dish": "Ceviche", "description": "Ceviche is a popular Peruvian dish made from raw fish marinated in freshly squeezed lime or lemon juice, mixed with chopped onions, chili, and cilantro."},
   {"country": "Sweden", "dish": "Swedish Meatballs", "description": "Swedish Meatballs are small, tender balls of minced meat (usually beef or pork), served with lingonberry jam and creamy mashed potatoes."}
]


class CountryAPI:
   """
   Define the API CRUD endpoints for the Country model.
   """
   class _RANDOM(Resource):
       def get(self):
           """
           Retrieve a random country's national dish and description.
           """
           # Select a random country from the data
           country_data = random.choice(countries_data)
           # Return the data in JSON format
           return jsonify(country_data)


   class _ADD(Resource):
       @token_required()
       def post(self):
           """
           Add a new country and its national dish.
           """
           # Obtain the request data sent by the client
           data = request.get_json()


           if not data:
               return {'message': 'No input data provided'}, 400
           if 'country' not in data or 'dish' not in data or 'description' not in data:
               return {'message': 'Country, Dish, and Description are required fields'}, 400


           # Create a new country object and save it to the database (using ORM model)
           new_country = CountryDish(country=data['country'], dish=data['dish'], description=data['description'])
           new_country.create()  # Save to the database using ORM method


           return jsonify({"message": "Country and dish added successfully!"})


   class _ALL_COUNTRIES(Resource):
       def get(self):
           """
           Retrieve all countries and their national dishes.
           """
           countries = CountryDish.query.all()  # Query all countries from the database
           json_ready = [country.read() for country in countries]  # Convert each country object to a dictionary
           return jsonify(json_ready)


   class _FILTER(Resource):
       def post(self):
           """
           Retrieve countries by a specific national dish.
           """
           data = request.get_json()


           if data is None or 'dish' not in data:
               return {'message': 'Dish data not found'}, 400


           # Query countries where the dish matches the provided dish name
           countries = CountryDish.query.filter(CountryDish._dish == data['dish']).all()
           json_ready = [country.read() for country in countries]
           return jsonify(json_ready)


   # Register the resources to the API
   api.add_resource(_RANDOM, '/random')
   api.add_resource(_ADD, '/add')
   api.add_resource(_ALL_COUNTRIES, '/countries')
   api.add_resource(_FILTER, '/countries/filter')
