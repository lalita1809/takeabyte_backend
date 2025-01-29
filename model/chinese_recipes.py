# model/chinese_recipes.py
import logging
from sqlalchemy import JSON
from sqlalchemy.exc import IntegrityError
from __init__ import app, db

class Recipe(db.Model):
    """
    Recipe Model
    
    The Recipe class represents an individual recipe.
    
    Attributes:
        id (db.Column): The primary key, an integer representing the unique identifier for the recipe.
        _name (db.Column): A string representing the name of the recipe.
        _dish (db.Column): A string representing the dish name.
        _time (db.Column): An integer representing the cooking time in minutes.
        _ingredients (db.Column): A string representing the ingredients of the recipe.
        _instructions (db.Column): A string representing the cooking instructions.
    """
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), nullable=False, unique=True)
    _dish = db.Column(db.String(255), nullable=False)
    _time = db.Column(db.Integer, nullable=False)
    _ingredients = db.Column(db.Text, nullable=False)
    _instructions = db.Column(db.Text, nullable=False)

    def __init__(self, name, dish, time, ingredients, instructions):
        self._name = name
        self._dish = dish
        self._time = time
        self._ingredients = ingredients
        self._instructions = instructions

    def __repr__(self):
        return f"Recipe(id={self.id}, name={self._name}, dish={self._dish}, time={self._time}, ingredients={self._ingredients}, instructions={self._instructions})"

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            logging.warning(f"IntegrityError: Could not create recipe with name '{self._name}' due to {str(e)}.")
            return None
        return self

    def read(self):
        return {
            "id": self.id,
            "name": self._name,
            "dish": self._dish,
            "time": self._time,
            "ingredients": self._ingredients,
            "instructions": self._instructions
        }

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, f"_{key}"):
                setattr(self, f"_{key}", value)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            logging.warning(f"IntegrityError: Could not update recipe with name '{self._name}'.")
            return None
        return self

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def restore(data):
        for recipe_data in data:
            _ = recipe_data.pop('id', None)
            name = recipe_data.get("name", None)
            recipe = Recipe.query.filter_by(_name=name).first()
            if recipe:
                recipe.update(recipe_data)
            else:
                recipe = Recipe(**recipe_data)
                recipe.create()

def initRecipes():
    with app.app_context():
        db.create_all()
        recipes = [
            Recipe(name="Kung Pao Chicken", dish="Kung Pao Chicken", time=30, ingredients="Chicken breast (500g), Dried red chilies (10-12), Peanuts (50g), Soy sauce (2 tbsp), Rice vinegar (1 tbsp), Sugar (1 tsp), Cornstarch (1 tsp), Garlic (3 cloves), Ginger (1-inch piece), Spring onions (2 stalks)", instructions="Cut chicken into small cubes and marinate with soy sauce and cornstarch for 10 minutes. Heat oil in a wok, fry dried chilies and peanuts until fragrant. Add garlic and ginger, stir-fry for 30 seconds. Add chicken and stir-fry until golden brown. Mix soy sauce, rice vinegar, sugar, and stir into the wok. Add spring onions and stir-fry for 2 more minutes before serving."),
            Recipe(name="Orange Chicken", dish="Orange Chicken", time=40, ingredients="Chicken breast (500g), Orange juice (1/2 cup), Soy sauce (2 tbsp), Vinegar (1 tbsp), Brown sugar (1/4 cup), Cornstarch (1 tbsp), Garlic (3 cloves), Ginger (1-inch piece), Orange zest (1 tsp), Vegetable oil (2 tbsp)", instructions="Fry chicken until crispy. Combine orange juice, soy sauce, vinegar, sugar, and cornstarch in a bowl. Stir-fry garlic and ginger, add sauce mixture, and cook until thickened. Coat chicken in the sauce. Serve with steamed rice."),
            # Add more sample recipes as needed
        ]
        
        for recipe in recipes:
            try:
                recipe.create()
                print(f"Record created: {repr(recipe)}")
            except IntegrityError:
                db.session.remove()
                print(f"Records exist, duplicate name, or error: {recipe._name}")
                
def save_recipe(name, dish, time, ingredients, instructions):
    new_recipe = Recipe(name=name, dish=dish, time=time, ingredients=ingredients, instructions=instructions)
    return new_recipe.create()