import logging
from sqlalchemy import JSON
from sqlalchemy.exc import IntegrityError
from __init__ import app, db
from model.user import User

class Fridge(db.Model):
    """
    Fridge Model
    Represents grocery stored in a user's fridge, and the quantity that can be made from them.
    """
    __tablename__ = 'fridge'

    id = db.Column(db.Integer, primary_key=True)
    _grocery = db.Column(db.String(255), nullable=False)  # A comma-separated list of grocery
    _quantity = db.Column(db.Integer, nullable=True)  # A list of recipe objects related to the grocery
    _user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, grocery, quantity, user_id=None):
        """
        Initialize a Fridge object.
        Args:
            grocery (str): A comma-separated list of grocery in the fridge.
            user_id (int, optional): ID of the user who owns the fridge entry.
            quantity (list, optional): A list of recipe data that can be made with the grocery.
        """
        self._grocery = grocery
        self._user_id = user_id
        self._quantity = quantity

    def __repr__(self):
        """String representation for debugging."""
        return f"Fridge(id={self.id}, grocery={self._grocery}, user_id={self._user_id})"

    def create(self):
        """Add the fridge entry to the database."""
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            logging.warning(f"Could not create fridge entry with grocery '{self._grocery}' due to {str(e)}.")
            return None
        return self

    def read(self):
        """
        Retrieve the fridge entry's data as a dictionary.
        Returns:
            dict: Fridge entry data with associated quantity.
        """
        user = Fridge.query.get(self._user_id)
        return {
            "id": self.id,
            "grocery": self._grocery,
            "quantity": self._quantity,
            "user_id": user.id if user else None,
        }

    def update(self, data):
        """
        Update the fridge entry with new data.
        Args:
            data (dict): Dictionary containing updated fields.
        """
        self._grocery = data.get('_grocery', self._grocery)
        self._quantity = data.get('_quantity', self._quantity)
        self._user_id = data.get('_user_id', self._user_id)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete(self):
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
            grocery = entry.get("grocery")
            existing_entry = Fridge.query.filter_by(_grocery=grocery).first()
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
            Fridge(grocery='Tomatoes', user_id=1, quantity=5),
            Fridge(grocery='Eggs', user_id=1, quantity=12),
            Fridge(grocery='Cucumber', user_id=1, quantity=4),
        ]
        
        for fridge in fridges:
            try:
                fridge.create()
                print(f"Record created: {repr(fridge)}")
            except IntegrityError:
                db.session.remove()
                print(f"Record already exists or error: {fridge._grocery}")
