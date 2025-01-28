import logging
from sqlalchemy import JSON
from sqlalchemy.exc import IntegrityError
from __init__ import app, db
from model.user import User

class Fridge(db.Model):
    """
    Fridge Model
    Represents ingredients stored in a user's fridge, and the recipes that can be made from them.
    """
    __tablename__ = 'fridge'

    id = db.Column(db.Integer, primary_key=True)
    _ingredients = db.Column(db.String(255), nullable=False)  # A comma-separated list of ingredients
    _recipes = db.Column(JSON, nullable=True)  # A list of recipe objects related to the ingredients
    _user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, ingredients, user_id=None, recipes=None):
        """
        Initialize a Fridge object.
        Args:
            ingredients (str): A comma-separated list of ingredients in the fridge.
            user_id (int, optional): ID of the user who owns the fridge entry.
            recipes (list, optional): A list of recipe data that can be made with the ingredients.
        """
        self._ingredients = ingredients
        self._user_id = user_id
        self._recipes = recipes or []

    def __repr__(self):
        """String representation for debugging."""
        return f"Fridge(id={self.id}, ingredients={self._ingredients}, user_id={self._user_id})"

    def create(self):
        """Add the fridge entry to the database."""
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            logging.warning(f"Could not create fridge entry with ingredients '{self._ingredients}' due to {str(e)}.")
            return None
        return self

    def read(self):
        """
        Retrieve the fridge entry's data as a dictionary.
        Returns:
            dict: Fridge entry data with associated recipes.
        """
        user = User.query.get(self._user_id)
        return {
            "id": self.id,
            "ingredients": self._ingredients,
            "recipes": self._recipes,
            "user_id": user.id if user else None,
        }

    def update(self, data):
        """
        Update the fridge entry with new data.
        Args:
            data (dict): Dictionary containing updated fields.
        """
        self._ingredients = data.get('_ingredients', self._ingredients)
        self._recipes = data.get('_recipes', self._recipes)
        self._user_id = data.get('_user_id', self._user_id)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete(self):
        """Delete the fridge entry from the database."""
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def restore(data):
        """
        Restore or update fridge entries from a data list.
        Args:
            data (list): List of dictionaries containing fridge data.
        """
        for entry in data:
            entry.pop('id', None)  # Remove 'id' if present
            ingredients = entry.get("ingredients")
            existing_entry = Fridge.query.filter_by(_ingredients=ingredients).first()
            if existing_entry:
                existing_entry.update(entry)
            else:
                new_entry = Fridge(**entry)
                new_entry.create()


def initFridge():
    """
    Initialize the Fridge table and add sample data to the table.
    """
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        
        """Sample data for fridge entries"""
        fridges = [
            Fridge(ingredients='chicken, garlic, lemon', user_id=1, recipes=[]),
            Fridge(ingredients='tomato, mozzarella, basil', user_id=1, recipes=[]),
            Fridge(ingredients='potato, cheese, butter', user_id=2, recipes=[]),
        ]
        
        for fridge in fridges:
            try:
                fridge.create()
                print(f"Record created: {repr(fridge)}")
            except IntegrityError:
                db.session.remove()
                print(f"Record already exists or error: {fridge._ingredients}")
