# country_dish.py
import logging
from sqlalchemy import Text, JSON
from sqlalchemy.exc import IntegrityError
from __init__ import app, db


class CountryDish(db.Model):
   """
   CountryDish Model
  
   The CountryDish class represents a country's national dish along with a description.
  
   Attributes:
       id (db.Column): The primary key, an integer representing the unique identifier for the dish.
       _country (db.Column): A string representing the name of the country.
       _dish (db.Column): A string representing the name of the national dish.
       _description (db.Column): A string representing the description of the national dish.
   """
   __tablename__ = 'country_dishes'


   id = db.Column(db.Integer, primary_key=True)
   _country = db.Column(db.String(255), nullable=False)
   _dish = db.Column(db.String(255), nullable=False)
   _description = db.Column(db.String(500), nullable=False)


   def __init__(self, country, dish, description):
       """
       Constructor, 1st step in object creation.
      
       Args:
           country (str): The name of the country.
           dish (str): The name of the national dish.
           description (str): The description of the national dish.
       """
       self._country = country
       self._dish = dish
       self._description = description


   def __repr__(self):
       """
       The __repr__ method is used to represent the object in string format.
       Called by the repr(country_dish) built-in function.
      
       Returns:
           str: A text representation of how to create the object.
       """
       return f"CountryDish(id={self.id}, country={self._country}, dish={self._dish}, description={self._description})"


   def create(self):
       """
       Creates a new country dish record in the database.
      
       Returns:
           CountryDish: The created country dish object, or None on error.
       """
       try:
           db.session.add(self)
           db.session.commit()
       except IntegrityError as e:
           db.session.rollback()
           logging.warning(f"IntegrityError: Could not create country dish for '{self._country}' due to {str(e)}.")
           return None
       return self
      
   def read(self):
       """
       The read method retrieves the object data from the object's attributes and returns it as a dictionary.
      
       Returns:
           dict: A dictionary containing the country dish data.
       """
       data = {
           "id": self.id,
           "country": self._country,
           "dish": self._dish,
           "description": self._description
       }
       return data


   def update(self):
       """
       Updates the country dish object with new data.
      
       Args:
           country (str): The updated country name.
           dish (str): The updated dish name.
           description (str): The updated description.
      
       Returns:
           CountryDish: The updated country dish object, or None on error.
       """
       self._country = self._country
       self._dish = self._dish
       self._description = self._description


       try:
           db.session.commit()
       except IntegrityError:
           db.session.rollback()
           logging.warning(f"IntegrityError: Could not update country dish for '{self._country}' due to missing data.")
           return None
       return self
  
   def delete(self):
       """
       The delete method removes the object from the database and commits the transaction.
      
       Uses:
           The db ORM methods to delete and commit the transaction.
      
       Raises:
           Exception: An error occurred when deleting the object from the database.
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
       Bulk restore or insert data into the database.


       Args:
           data (list): A list of dictionaries representing the country dish data.
       """
       for dish_data in data:
           _ = dish_data.pop('id', None)  # Remove 'id' from dish_data if present
           country = dish_data.get("country", None)
           dish = CountryDish.query.filter_by(_country=country).first()
           if dish:
               dish.update(dish_data)
           else:
               dish = CountryDish(**dish_data)
               dish.create()


def initCountryDishes():
   """
   The initCountryDishes function creates the CountryDish table and adds tester data to the table.
  
   Uses:
       The db ORM methods to create the table.
  
   Instantiates:
       CountryDish objects with tester data.
  
   Raises:
       IntegrityError: An error occurred when adding the tester data to the table.
   """       
   with app.app_context():
       """Create database and tables"""
       db.create_all()
       """Tester data for table"""
       country_dishes = [
           CountryDish(country='Italy', dish='Pizza', description='Pizza is a traditional Italian dish consisting of a usually round, flat base of leavened wheat-based dough topped with tomatoes, cheese, and often various other ingredients.'),
           CountryDish(country='Japan', dish='Sushi', description='Sushi is a Japanese dish of prepared vinegared rice accompanied by various ingredients, such as seafood, vegetables, and occasionally tropical fruits.'),
           CountryDish(country='Mexico', dish='Tacos', description='Tacos are a traditional Mexican dish consisting of a small hand-sized tortilla, typically filled with a variety of ingredients such as beef, chicken, or vegetables.'),
           CountryDish(country='India', dish='Biryani', description='Biryani is a mixed rice dish originating from the Indian subcontinent, made with Indian spices, rice, and typically either meat or vegetables.'),
           CountryDish(country='France', dish='Baguette', description='The Baguette is a long, narrow loaf of French bread that is typically crispy on the outside and soft on the inside.')
       ]
      
       for dish in country_dishes:
           try:
               dish.create()
               print(f"Record created: {repr(dish)}")
           except IntegrityError:
               '''fails with bad or duplicate data'''
               db.session.remove()
               print(f"Records exist, duplicate or error: {dish._country} - {dish._dish}")


