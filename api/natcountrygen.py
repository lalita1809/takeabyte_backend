from flask import Blueprint, request, jsonify, Response, g
from flask_restful import Api, Resource
import random
from model.natcountrygen import Dish


# Define the Blueprint for the Dish API
dish_api = Blueprint('dish_api', __name__, url_prefix='/api')
api = Api(dish_api)


# Sample data for countries and their national dishes
dishes = [
  {"country": "Italy", "dish": "Pizza Margherita", "explanation": "Pizza Margherita is a simple yet iconic dish that represents the colors of the Italian flag: red (tomato), white (mozzarella), and green (basil)."},
  {"country": "Japan", "dish": "Sushi", "explanation": "Sushi is a traditional Japanese dish consisting of vinegared rice, raw fish, and vegetables, showcasing Japan's culinary precision."},
  {"country": "India", "dish": "Biryani", "explanation": "Biryani is a flavorful rice dish cooked with spices, meat, and/or vegetables, reflecting India's rich culinary heritage."},
  {"country": "Mexico", "dish": "Tacos", "explanation": "Tacos are a staple of Mexican cuisine, featuring a tortilla filled with various meats, vegetables, and salsas."},
  {"country": "France", "dish": "Coq au Vin", "explanation": "Coq au Vin is a classic French dish of chicken braised with wine, mushrooms, and garlic, representing French culinary sophistication."},
  {"country": "USA", "dish": "Hamburger", "explanation": "The hamburger is a symbol of American fast food culture, consisting of a beef patty in a bun with various toppings."},
  {"country": "Thailand", "dish": "Pad Thai", "explanation": "Pad Thai is a popular Thai street food dish made with stir-fried rice noodles, tamarind, peanuts, and shrimp or tofu."},
  {"country": "Spain", "dish": "Paella", "explanation": "Paella is a Spanish rice dish cooked with saffron, seafood, and vegetables, originating from the region of Valencia."},
  {"country": "Greece", "dish": "Moussaka", "explanation": "Moussaka is a Greek casserole layered with eggplant, minced meat, and béchamel sauce, showcasing Mediterranean flavors."},
  {"country": "China", "dish": "Peking Duck", "explanation": "Peking Duck is a renowned Chinese dish known for its crispy skin and flavorful meat, served with pancakes and hoisin sauce."}
]


class DishAPI:
  class _RandomDish(Resource):
      def get(self):
          """
          Retrieve a random dish from the dataset.
          """
          dish = random.choice(dishes)
          return jsonify(dish)


  # Map the _RandomDish class to the API endpoint for /dish/random
  api.add_resource(_RandomDish, '/dish/natgen1')


class _addDish(Resource):
   def post(self):
        """
        Add a new dish to the dataset.
        """
        data = request.get_json()
        country = data['country']
        dish = data['dish']
        description = data['description']
       #  if not country or not dish or not description:
       #       return jsonify({"error": "Missing required fields."}), 400
        new_dish = Dish(country=country, dish=dish, description=description)
        new_dish.create()
        return jsonify(new_dish.read())
  
api.add_resource(_addDish,'/dish/natgen2')
