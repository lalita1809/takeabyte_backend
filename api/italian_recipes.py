from flask import Blueprint, jsonify
from flask_restful import Api, Resource  # used for REST API building

italian_recipe_api = Blueprint('italian_recipe_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/
api = Api(italian_recipe_api)

class italian_recipe_API:
    @staticmethod
    def get_chicken_recipe(name):
        recipes = {
            "Chicken Parmesan": {
                "dish": "Chicken Parmesan",
                "time": 60,
                "ingredients": ["chicken", "breadcrumbs", "parmesan", "tomato sauce", "mozzarella"],
                "instructions": "Bread and fry chicken, top with tomato sauce and cheese, bake."
            },
            "Chicken Alfredo": {
                "dish": "Chicken Alfredo",
                "time": 30,
                "ingredients": ["chicken", "fettuccine", "cream", "parmesan", "butter"],
                "instructions": "Cook chicken, prepare Alfredo sauce with cream and parmesan, mix with pasta."
            },
            "Chicken Marsala": {
                "dish": "Chicken Marsala",
                "time": 40,
                "ingredients": ["chicken", "mushrooms", "marsala wine", "butter", "garlic"],
                "instructions": "Cook chicken with mushrooms and garlic, deglaze with Marsala wine."
            },
            "Chicken Piccata": {
                "dish": "Chicken Piccata",
                "time": 35,
                "ingredients": ["chicken", "lemon", "capers", "butter", "white wine"],
                "instructions": "Cook chicken, make sauce with lemon, capers, butter, and white wine."
            },
            "Chicken Cacciatore": {
                "dish": "Chicken Cacciatore",
                "time": 75,
                "ingredients": ["chicken", "tomatoes", "bell peppers", "onions", "mushrooms"],
                "instructions": "Simmer chicken with tomatoes, bell peppers, onions, and mushrooms."
            },
            "Chicken Risotto": {
                "dish": "Chicken Risotto",
                "time": 50,
                "ingredients": ["chicken", "arborio rice", "chicken broth", "parmesan", "white wine"],
                "instructions": "Cook chicken, prepare risotto with arborio rice, chicken broth, and parmesan."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_beef_recipe(name):
        recipes = {
            "Beef Lasagna": {
                "dish": "Beef Lasagna",
                "time": 90,
                "ingredients": ["beef", "lasagna noodles", "ricotta", "tomato sauce", "mozzarella"],
                "instructions": "Layer beef, noodles, ricotta, and tomato sauce, top with mozzarella, bake."
            },
            "Spaghetti Bolognese": {
                "dish": "Spaghetti Bolognese",
                "time": 60,
                "ingredients": ["beef", "spaghetti", "tomato sauce", "carrots", "celery", "onions"],
                "instructions": "Simmer beef with tomato sauce and vegetables, serve over spaghetti."
            },
            "Beef Braciole": {
                "dish": "Beef Braciole",
                "time": 120,
                "ingredients": ["beef", "breadcrumbs", "parmesan", "tomato sauce", "garlic"],
                "instructions": "Roll beef with breadcrumbs and cheese, simmer in tomato sauce."
            },
            "Beef Florentine": {
                "dish": "Beef Florentine",
                "time": 45,
                "ingredients": ["beef", "spinach", "cream", "garlic", "parmesan"],
                "instructions": "Cook beef, prepare Florentine sauce with spinach, cream, and parmesan."
            },
            "Beef Ossobuco": {
                "dish": "Beef Ossobuco",
                "time": 120,
                "ingredients": ["beef shanks", "carrots", "celery", "onions", "tomato sauce"],
                "instructions": "Braise beef shanks with vegetables and tomato sauce."
            },
            "Beef Risotto": {
                "dish": "Beef Risotto",
                "time": 50,
                "ingredients": ["beef", "arborio rice", "beef broth", "parmesan", "red wine"],
                "instructions": "Cook beef, prepare risotto with arborio rice, beef broth, and parmesan."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_vegan_recipe(name):
        recipes = {
            "Vegan Spaghetti": {
                "dish": "Vegan Spaghetti",
                "time": 30,
                "ingredients": ["spaghetti", "tomato sauce", "garlic", "basil", "olive oil"],
                "instructions": "Cook spaghetti, prepare tomato sauce with garlic and basil."
            },
            "Vegan Lasagna": {
                "dish": "Vegan Lasagna",
                "time": 70,
                "ingredients": ["lasagna noodles", "vegan ricotta", "tomato sauce", "spinach", "vegan cheese"],
                "instructions": "Layer noodles, vegan ricotta, tomato sauce, spinach, and vegan cheese, bake."
            },
            "Vegan Risotto": {
                "dish": "Vegan Risotto",
                "time": 50,
                "ingredients": ["arborio rice", "vegetable broth", "onions", "garlic", "vegan parmesan"],
                "instructions": "Prepare risotto with arborio rice, vegetable broth, and vegan parmesan."
            },
            "Vegan Pizza": {
                "dish": "Vegan Pizza",
                "time": 25,
                "ingredients": ["pizza dough", "tomato sauce", "vegan cheese", "vegetables"],
                "instructions": "Top pizza dough with tomato sauce, vegan cheese, and vegetables, bake."
            },
            "Vegan Gnocchi": {
                "dish": "Vegan Gnocchi",
                "time": 40,
                "ingredients": ["gnocchi", "tomato sauce", "basil", "olive oil", "vegan parmesan"],
                "instructions": "Cook gnocchi, prepare tomato sauce with basil and olive oil."
            },
            "Vegan Minestrone": {
                "dish": "Vegan Minestrone",
                "time": 45,
                "ingredients": ["vegetables", "beans", "tomato broth", "pasta", "herbs"],
                "instructions": "Simmer vegetables, beans, and pasta in tomato broth."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_fish_recipe(name):
        recipes = {
            "Shrimp Scampi": {
                "dish": "Shrimp Scampi",
                "time": 20,
                "ingredients": ["shrimp", "garlic", "butter", "lemon", "parsley"],
                "instructions": "Sauté shrimp with garlic and butter, finish with lemon and parsley."
            },
            "Linguine with Clams": {
                "dish": "Linguine with Clams",
                "time": 30,
                "ingredients": ["linguine", "clams", "garlic", "white wine", "parsley"],
                "instructions": "Cook linguine, prepare clam sauce with garlic, white wine, and parsley."
            },
            "Cioppino": {
                "dish": "Cioppino",
                "time": 45,
                "ingredients": ["mixed seafood", "tomato broth", "garlic", "onions", "wine"],
                "instructions": "Simmer mixed seafood in tomato broth with garlic, onions, and wine."
            },
            "Grilled Salmon": {
                "dish": "Grilled Salmon",
                "time": 25,
                "ingredients": ["salmon", "lemon", "olive oil", "garlic", "herbs"],
                "instructions": "Marinate salmon in olive oil, garlic, and herbs, grill."
            },
            "Tuna Carpaccio": {
                "dish": "Tuna Carpaccio",
                "time": 15,
                "ingredients": ["tuna", "olive oil", "lemon", "capers", "arugula"],
                "instructions": "Thinly slice tuna, dress with olive oil, lemon, capers, and arugula."
            },
            "Fish Risotto": {
                "dish": "Fish Risotto",
                "time": 50,
                "ingredients": ["fish", "arborio rice", "fish broth", "white wine", "parmesan"],
                "instructions": "Cook fish, prepare risotto with arborio rice, fish broth, and parmesan."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_lamb_recipe(name):
        recipes = {
            "Lamb Ragu": {
                "dish": "Lamb Ragu",
                "time": 90,
                "ingredients": ["lamb", "tomato sauce", "garlic", "onions", "red wine"],
                "instructions": "Simmer lamb with tomato sauce, garlic, onions, and red wine."
            },
            "Lamb Chops": {
                "dish": "Lamb Chops",
                "time": 25,
                "ingredients": ["lamb chops", "garlic", "rosemary", "olive oil", "lemon"],
                "instructions": "Marinate lamb chops with garlic, rosemary, and olive oil, grill."
            },
            "Lamb Risotto": {
                "dish": "Lamb Risotto",
                "time": 50,
                "ingredients": ["lamb", "arborio rice", "lamb broth", "parmesan", "white wine"],
                "instructions": "Cook lamb, prepare risotto with arborio rice, lamb broth, and parmesan."
            },
            "Lamb Osso Buco": {
                "dish": "Lamb Osso Buco",
                "time": 120,
                "ingredients": ["lamb shanks", "carrots", "celery", "onions", "tomato sauce"],
                "instructions": "Braise lamb shanks with vegetables and tomato sauce."
            },
            "Lamb Meatballs": {
                "dish": "Lamb Meatballs",
                "time": 40,
                "ingredients": ["ground lamb", "breadcrumbs", "parmesan", "tomato sauce", "herbs"],
                "instructions": "Form lamb into meatballs, bake, simmer in tomato sauce."
            },
            "Lamb Lasagna": {
                "dish": "Lamb Lasagna",
                "time": 90,
                "ingredients": ["ground lamb", "lasagna noodles", "ricotta", "tomato sauce", "mozzarella"],
                "instructions": "Layer lamb, noodles, ricotta, and tomato sauce, top with mozzarella, bake."
            }
        }
        return recipes.get(name)


# Chicken Recipes
class ChickenParmesan(Resource):
    def get(self):
        recipe = italian_recipe_API.get_chicken_recipe("Chicken Parmesan")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class ChickenAlfredo(Resource):
    def get(self):
        recipe = italian_recipe_API.get_chicken_recipe("Chicken Alfredo")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class ChickenMarsala(Resource):
    def get(self):
        recipe = italian_recipe_API.get_chicken_recipe("Chicken Marsala")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class ChickenPiccata(Resource):
    def get(self):
        recipe = italian_recipe_API.get_chicken_recipe("Chicken Piccata")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class ChickenCacciatore(Resource):
    def get(self):
        recipe = italian_recipe_API.get_chicken_recipe("Chicken Cacciatore")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class ChickenRisotto(Resource):
    def get(self):
        recipe = italian_recipe_API.get_chicken_recipe("Chicken Risotto")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

# Beef Recipes
class BeefLasagna(Resource):
    def get(self):
        recipe = italian_recipe_API.get_beef_recipe("Beef Lasagna")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class SpaghettiBolognese(Resource):
    def get(self):
        recipe = italian_recipe_API.get_beef_recipe("Spaghetti Bolognese")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class BeefBraciole(Resource):
    def get(self):
        recipe = italian_recipe_API.get_beef_recipe("Beef Braciole")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class BeefFlorentine(Resource):
    def get(self):
        recipe = italian_recipe_API.get_beef_recipe("Beef Florentine")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class BeefOssobuco(Resource):
    def get(self):
        recipe = italian_recipe_API.get_beef_recipe("Beef Ossobuco")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class BeefRisotto(Resource):
    def get(self):
        recipe = italian_recipe_API.get_beef_recipe("Beef Risotto")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

# Vegan Recipes
class VeganSpaghetti(Resource):
    def get(self):
        recipe = italian_recipe_API.get_vegan_recipe("Vegan Spaghetti")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class VeganLasagna(Resource):
    def get(self):
        recipe = italian_recipe_API.get_vegan_recipe("Vegan Lasagna")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class VeganRisotto(Resource):
    def get(self):
        recipe = italian_recipe_API.get_vegan_recipe("Vegan Risotto")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class VeganPizza(Resource):
    def get(self):
        recipe = italian_recipe_API.get_vegan_recipe("Vegan Pizza")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class VeganGnocchi(Resource):
    def get(self):
        recipe = italian_recipe_API.get_vegan_recipe("Vegan Gnocchi")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class VeganMinestrone(Resource):
    def get(self):
        recipe = italian_recipe_API.get_vegan_recipe("Vegan Minestrone")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

# Fish Recipes
class ShrimpScampi(Resource):
    def get(self):
        recipe = italian_recipe_API.get_fish_recipe("Shrimp Scampi")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class LinguineWithClams(Resource):
    def get(self):
        recipe = italian_recipe_API.get_fish_recipe("Linguine with Clams")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class Cioppino(Resource):
    def get(self):
        recipe = italian_recipe_API.get_fish_recipe("Cioppino")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class GrilledSalmon(Resource):
    def get(self):
        recipe = italian_recipe_API.get_fish_recipe("Grilled Salmon")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class TunaCarpaccio(Resource):
    def get(self):
        recipe = italian_recipe_API.get_fish_recipe("Tuna Carpaccio")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class FishRisotto(Resource):
    def get(self):
        recipe = italian_recipe_API.get_fish_recipe("Fish Risotto")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

# Lamb Recipes
class LambRagu(Resource):
    def get(self):
        recipe = italian_recipe_API.get_lamb_recipe("Lamb Ragu")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class LambChops(Resource):
    def get(self):
        recipe = italian_recipe_API.get_lamb_recipe("Lamb Chops")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class LambRisotto(Resource):
    def get(self):
        recipe = italian_recipe_API.get_lamb_recipe("Lamb Risotto")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class LambOssoBuco(Resource):
    def get(self):
        recipe = italian_recipe_API.get_lamb_recipe("Lamb Osso Buco")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class LambMeatballs(Resource):
    def get(self):
        recipe = italian_recipe_API.get_lamb_recipe("Lamb Meatballs")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

class LambLasagna(Resource):
    def get(self):
        recipe = italian_recipe_API.get_lamb_recipe("Lamb Lasagna")
        if recipe:
            return jsonify(recipe)
        return {"Data not found"}, 404

# Register API resources
api.add_resource(ChickenParmesan, '/italian_recipe/ChickenParmesan')
api.add_resource(ChickenAlfredo, '/italian_recipe/ChickenAlfredo')
api.add_resource(ChickenMarsala, '/italian_recipe/ChickenMarsala')
api.add_resource(ChickenPiccata, '/italian_recipe/ChickenPiccata')
api.add_resource(ChickenCacciatore, '/italian_recipe/ChickenCacciatore')
api.add_resource(ChickenRisotto, '/italian_recipe/ChickenRisotto')

api.add_resource(BeefLasagna, '/italian_recipe/BeefLasagna')
api.add_resource(SpaghettiBolognese, '/italian_recipe/SpaghettiBolognese')
api.add_resource(BeefBraciole, '/italian_recipe/BeefBraciole')
api.add_resource(BeefFlorentine, '/italian_recipe/BeefFlorentine')
api.add_resource(BeefOssobuco, '/italian_recipe/BeefOssobuco')
api.add_resource(BeefRisotto, '/italian_recipe/BeefRisotto')

api.add_resource(VeganLasagna, '/italian_recipe/VeganLasagna')
api.add_resource(VeganRisotto, '/italian_recipe/VeganRisotto')
api.add_resource(VeganPizza, '/italian_recipe/VeganPizza')
api.add_resource(VeganGnocchi, '/italian_recipe/VeganGnocchi')
api.add_resource(VeganMinestrone, '/italian_recipe/VeganMinestrone')

api.add_resource(ShrimpScampi, '/italian_recipe/ShrimpScampi')
api.add_resource(LinguineWithClams, '/italian_recipe/LinguineWithClams')
api.add_resource(Cioppino, '/italian_recipe/Cioppino')
api.add_resource(GrilledSalmon, '/italian_recipe/GrilledSalmon')
api.add_resource(TunaCarpaccio, '/italian_recipe/TunaCarpaccio')
api.add_resource(FishRisotto, '/italian_recipe/FishRisotto')

api.add_resource(LambRagu, '/italian_recipe/LambRagu')
api.add_resource(LambChops, '/italian_recipe/LambChops')
api.add_resource(LambRisotto, '/italian_recipe/LambRisotto')
api.add_resource(LambOssoBuco, '/italian_recipe/LambOssoBuco')
api.add_resource(LambMeatballs, '/italian_recipe/LambMeatballs')
api.add_resource(LambLasagna, '/italian_recipe/LambLasagna')

italian_recipe_api_instance = italian_recipe_API()