from __init__ import app, db
from sqlite3 import IntegrityError
from sqlalchemy import Column, Integer, String, Text


class Dish(db.Model):
  """
  Dish Model


  This model represents a dish with its associated country and description.
  """
  __tablename__ = 'dishes'


  id = db.Column(db.Integer, primary_key=True)
  country = db.Column(db.String(100), nullable=False)  # Country of origin for the dish
  dish = db.Column(db.String(200), nullable=False)  # Name of the dish
  description = db.Column(db.Text, nullable=True)  # Description of the dish


  def __init__(self, country, dish, description=None):
      self.country = country
      self.dish = dish
      self.description = description


  def create(self):
      """
      Add the dish to the database and commit the transaction.
      """
      try:
          db.session.add(self)
          db.session.commit()
      except Exception as e:
          db.session.rollback()
          raise e


  def read(self):
      """
      Retrieve the dish's data as a dictionary.
      """
      return {
          "id": self.id,
          "country": self.country,
          "dish": self.dish,
          "description": self.description
      }


  def update(self, data):
      """
      Update the dish's data with the provided dictionary.
      """
      try:
          self.country = data.get('country', self.country)
          self.dish = data.get('dish', self.dish)
          self.description = data.get('description', self.description)
          db.session.commit()
      except Exception as e:
          db.session.rollback()
          raise e


  def delete(self):
      """
      Remove the dish from the database and commit the transaction.
      """
      try:
          db.session.delete(self)
          db.session.commit()
      except Exception as e:
          db.session.rollback()
          raise e


  @staticmethod
  def restore(data):
      """
      Restore dishes from a list of dictionaries.


      Args:
          data (list): A list of dictionaries containing dish data.


      Returns:
          dict: A dictionary of restored dishes keyed by dish name.
      """
      restored_dishes = {}
      for dish_data in data:
          _ = dish_data.pop('id', None)  # Remove 'id' from dish_data
          dish_name = dish_data.get("dish", None)
          existing_dish = Dish.query.filter_by(dish=dish_name).first()
          if existing_dish:
              existing_dish.update(dish_data)
          else:
              new_dish = Dish(**dish_data)
              new_dish.create()
          restored_dishes[dish_name] = new_dish
      return restored_dishes


def initDishes():
  """
  Initialize the Dish table with default data.
  """
  dishes = [
      Dish("Italy", "Pizza", "A savory dish of Italian origin consisting of a usually round, flattened base of leavened wheat-based dough topped with tomatoes, cheese, and often various other ingredients."),
      Dish("India", "Biryani", "A mixed rice dish originating among the Muslims of the Indian subcontinent, made with spices, rice, and usually some type of meat (chicken, beef, goat, lamb, prawn, or fish)."),
      Dish("Japan", "Sushi", "A Japanese dish consisting of prepared vinegared rice, usually with some sugar and salt, accompanying a variety of ingredients, such as seafood, often raw, and vegetables."),
      Dish("Mexico", "Tacos", "A traditional Mexican food consisting of a small hand-sized corn- or wheat-based tortilla topped with a filling."),
      Dish("France", "Croissant", "A buttery, flaky, French viennoiserie pastry inspired by the shape of the Austrian kipferl."),
      Dish("USA", "Hamburger", "A sandwich consisting of one or more cooked patties of ground meat, usually beef, placed inside a sliced bread roll or bun."),
      Dish("China", "Dim Sum", "A style of Chinese cuisine prepared as small bite-sized portions of food served in small steamer baskets or on small plates."),
      Dish("Spain", "Paella", "A Spanish rice dish originally from Valencia, usually made with rice, saffron, chicken, and seafood."),
      Dish("Thailand", "Pad Thai", "A stir-fry dish made from rice noodles, shrimp, chicken, or tofu, peanuts, a scrambled egg, and bean sprouts."),
      Dish("Greece", "Moussaka", "An eggplant- or potato-based dish, often including ground meat, in the Levant, Middle East, and Balkans, with many local and regional variations."),
  ]


  for dish in dishes:
      try:
          db.session.add(dish)
          db.session.commit()
          print(f"Added Dish: {dish.dish} from {dish.country}")
      except Exception as e:
          db.session.rollback()
          print(f"Error adding dish {dish.dish}: {e}")
