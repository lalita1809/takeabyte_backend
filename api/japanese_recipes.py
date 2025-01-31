from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource  # used for REST API building
from __init__ import db
from model.chinese_recipes import Recipe

japanese_recipe_api = Blueprint('japanese_recipe_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/
api = Api(japanese_recipe_api)

class SaveRecipe(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return {"message": "No input data provided"}, 400

        try:
            recipe = Recipe(
                name=data.get('title'),
                dish=data.get('title'),
                time=data.get('time'),
                ingredients=data.get('ingredients'),
                instructions=data.get('instructions')
            )
            recipe.create()
            return {"message": "Recipe saved successfully"}, 201
        except Exception as e:
            return {"message": f"An error occurred: {str(e)}"}, 500
class UpdateRecipe(Resource):
    def put(self, recipe_id):
        data = request.get_json()
        if not data:
            return {"message": "No input data provided"}, 400

        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return {"message": "Recipe not found"}, 404

        try:
            recipe.name = data.get('title', recipe.name)
            recipe.dish = data.get('title', recipe.dish)
            recipe.time = data.get('time', recipe.time)
            recipe.ingredients = data.get('ingredients', recipe.ingredients)
            recipe.instructions = data.get('instructions', recipe.instructions)
            
            db.session.commit()

            return {"message": "Recipe updated successfully", "recipe": recipe.read()}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500

class japanese_recipe_API:
    @staticmethod
    def get_chicken_recipe(name):
        recipes = {
            "Chicken Teriyaki": {
                "dish": "Chicken Teriyaki",
                "time": 30,
                "ingredients": ["chicken", "soy sauce", "mirin", "sake", "sugar"],
                "instructions": "Grill or pan-fry chicken, then glaze with teriyaki sauce."
            },
            "Chicken Katsu": {
                "dish": "Chicken Katsu",
                "time": 40,
                "ingredients": ["chicken", "breadcrumbs", "egg", "flour", "tonkatsu sauce"],
                "instructions": "Bread and deep-fry chicken, serve with tonkatsu sauce."
            },
            "Chicken Yakitori": {
                "dish": "Chicken Yakitori",
                "time": 25,
                "ingredients": ["chicken", "soy sauce", "sake", "mirin", "scallions"],
                "instructions": "Grill chicken skewers and glaze with yakitori sauce."
            },
            "Chicken Ramen": {
                "dish": "Chicken Ramen",
                "time": 50,
                "ingredients": ["chicken", "ramen noodles", "broth", "soy sauce", "green onions"],
                "instructions": "Simmer chicken in broth, then serve with ramen noodles."
            },
            "Chicken Karaage": {
                "dish": "Chicken Karaage",
                "time": 35,
                "ingredients": ["chicken", "soy sauce", "garlic", "ginger", "flour"],
                "instructions": "Marinate chicken, coat with flour, and deep fry."
            },
            "Chicken Donburi": {
                "dish": "Chicken Donburi",
                "time": 45,
                "ingredients": ["chicken", "rice", "soy sauce", "egg", "green onions"],
                "instructions": "Cook chicken, serve over rice, and top with a cooked egg."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_beef_recipe(name):
        recipes = {
            "Beef Teriyaki": {
                "dish": "Beef Teriyaki",
                "time": 30,
                "ingredients": ["beef", "soy sauce", "mirin", "sake", "sugar"],
                "instructions": "Grill or pan-fry beef, then glaze with teriyaki sauce."
            },
            "Beef Sukiyaki": {
                "dish": "Beef Sukiyaki",
                "time": 60,
                "ingredients": ["beef", "soy sauce", "sugar", "tofu", "vegetables"],
                "instructions": "Simmer beef with soy sauce, sugar, tofu, and vegetables."
            },
            "Gyudon": {
                "dish": "Gyudon",
                "time": 30,
                "ingredients": ["beef", "rice", "soy sauce", "onions", "mirin"],
                "instructions": "Cook beef and onions in soy sauce, serve over rice."
            },
            "Beef Yakiniku": {
                "dish": "Beef Yakiniku",
                "time": 40,
                "ingredients": ["beef", "soy sauce", "garlic", "sugar", "sesame oil"],
                "instructions": "Grill beef and brush with yakiniku sauce."
            },
            "Beef Shabu-Shabu": {
                "dish": "Beef Shabu-Shabu",
                "time": 35,
                "ingredients": ["beef", "vegetables", "dipping sauce", "tofu", "ponzu"],
                "instructions": "Dip thin slices of beef into hot broth and cook quickly."
            },
            "Beef Tataki": {
                "dish": "Beef Tataki",
                "time": 30,
                "ingredients": ["beef", "soy sauce", "garlic", "scallions", "sesame seeds"],
                "instructions": "Quick-sear beef, then slice thinly and serve with soy sauce."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_vegan_recipe(name):
        recipes = {
            "Vegan Ramen": {
                "dish": "Vegan Ramen",
                "time": 40,
                "ingredients": ["ramen noodles", "vegetable broth", "tofu", "mushrooms", "green onions"],
                "instructions": "Cook ramen noodles in broth, top with tofu and mushrooms."
            },
            "Vegan Sushi": {
                "dish": "Vegan Sushi",
                "time": 50,
                "ingredients": ["sushi rice", "nori", "avocado", "cucumber", "carrot"],
                "instructions": "Roll sushi with nori, rice, and veggies."
            },
            "Vegan Tempura": {
                "dish": "Vegan Tempura",
                "time": 30,
                "ingredients": ["vegetables", "tempura batter", "oil", "soy sauce"],
                "instructions": "Dip vegetables in tempura batter and deep fry."
            },
            "Vegan Gyoza": {
                "dish": "Vegan Gyoza",
                "time": 40,
                "ingredients": ["dumpling wrappers", "tofu", "cabbage", "garlic", "soy sauce"],
                "instructions": "Stuff gyoza wrappers with tofu and cabbage, steam or fry."
            },
            "Vegan Donburi": {
                "dish": "Vegan Donburi",
                "time": 35,
                "ingredients": ["rice", "tofu", "soy sauce", "vegetables", "ginger"],
                "instructions": "Serve tofu and vegetables over rice with soy sauce."
            },
            "Vegan Miso Soup": {
                "dish": "Vegan Miso Soup",
                "time": 20,
                "ingredients": ["miso paste", "tofu", "seaweed", "green onions", "broth"],
                "instructions": "Simmer tofu, seaweed, and green onions in miso broth."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_fish_recipe(name):
        recipes = {
            "Grilled Salmon": {
                "dish": "Grilled Salmon",
                "time": 30,
                "ingredients": ["salmon", "soy sauce", "mirin", "sake", "sesame seeds"],
                "instructions": "Grill salmon and glaze with soy sauce and mirin."
            },
            "Saba Shioyaki": {
                "dish": "Saba Shioyaki",
                "time": 25,
                "ingredients": ["mackerel", "salt", "lemon"],
                "instructions": "Salt mackerel and grill, serve with lemon."
            },
            "Unagi Donburi": {
                "dish": "Unagi Donburi",
                "time": 35,
                "ingredients": ["eel", "rice", "soy sauce", "mirin", "sake"],
                "instructions": "Grill eel and serve over rice with sauce."
            },
            "Tuna Tataki": {
                "dish": "Tuna Tataki",
                "time": 20,
                "ingredients": ["tuna", "soy sauce", "garlic", "sesame seeds", "green onions"],
                "instructions": "Quick-sear tuna and serve with soy sauce."
            },
            "Fish Karaage": {
                "dish": "Fish Karaage",
                "time": 30,
                "ingredients": ["fish fillets", "flour", "soy sauce", "garlic", "ginger"],
                "instructions": "Coat fish in flour and fry, serve with soy sauce."
            },
            "Fish Miso Soup": {
                "dish": "Fish Miso Soup",
                "time": 25,
                "ingredients": ["fish", "miso paste", "tofu", "seaweed", "broth"],
                "instructions": "Simmer fish, tofu, and seaweed in miso broth."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_lamb_recipe(name):
        recipes = {
            "Braised Lamb Shanks": {
                "dish": "Braised Lamb Shanks",
                "time": 90,
                "ingredients": ["lamb shanks", "garlic", "onions", "wine", "soy sauce"],
                "instructions": "Braise lamb shanks in wine, soy sauce, and aromatics."
            },
            "Lamb Katsu": {
                "dish": "Lamb Katsu",
                "time": 45,
                "ingredients": ["lamb", "breadcrumbs", "egg", "flour", "tonkatsu sauce"],
                "instructions": "Bread and deep-fry lamb, serve with tonkatsu sauce."
            },
            "Lamb Teriyaki": {
                "dish": "Lamb Teriyaki",
                "time": 30,
                "ingredients": ["lamb", "soy sauce", "mirin", "sake", "sugar"],
                "instructions": "Grill or pan-fry lamb, then glaze with teriyaki sauce."
            },
            "Lamb Donburi": {
                "dish": "Lamb Donburi",
                "time": 45,
                "ingredients": ["lamb", "rice", "soy sauce", "egg", "green onions"],
                "instructions": "Cook lamb, serve over rice, and top with a cooked egg."
            },
            "Lamb Ramen": {
                "dish": "Lamb Ramen",
                "time": 50,
                "ingredients": ["lamb", "ramen noodles", "broth", "soy sauce", "green onions"],
                "instructions": "Simmer lamb in broth, serve with ramen noodles."
            },
            "Lamb Yakiniku": {
                "dish": "Lamb Yakiniku",
                "time": 40,
                "ingredients": ["lamb", "soy sauce", "garlic", "sugar", "sesame oil"],
                "instructions": "Grill lamb and brush with yakiniku sauce."
            }
        }
        return recipes.get(name)


    class _ChickenTeriyaki(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_chicken_recipe("Chicken Teriyaki")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChickenKatsu(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_chicken_recipe("Chicken Katsu")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChickenYakitori(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_chicken_recipe("Chicken Yakitori")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChickenRamen(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_chicken_recipe("Chicken Ramen")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChickenKaraage(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_chicken_recipe("Chicken Karaage")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChickenDonburi(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_chicken_recipe("Chicken Donburi")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefTeriyaki(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_beef_recipe("Beef Teriyaki")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefSukiyaki(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_beef_recipe("Beef Sukiyaki")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _Gyudon(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_beef_recipe("Gyudon")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefYakiniku(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_beef_recipe("Beef Yakiniku")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefShabuShabu(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_beef_recipe("Beef Shabu-Shabu")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefTataki(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_beef_recipe("Beef Tataki")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganRamen(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_vegan_recipe("Vegan Ramen")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganSushi(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_vegan_recipe("Vegan Sushi")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganTempura(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_vegan_recipe("Vegan Tempura")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganGyoza(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_vegan_recipe("Vegan Gyoza")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganDonburi(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_vegan_recipe("Vegan Donburi")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganMisoSoup(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_vegan_recipe("Vegan Miso Soup")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _GrilledSalmon(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_fish_recipe("Grilled Salmon")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _SabaShioyaki(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_fish_recipe("Saba Shioyaki")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _UnagiDonburi(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_fish_recipe("Unagi Donburi")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _TunaTataki(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_fish_recipe("Tuna Tataki")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _FishKaraage(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_fish_recipe("Fish Karaage")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _FishMisoSoup(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_fish_recipe("Fish Miso Soup")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BraisedLambShanks(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_lamb_recipe("Braised Lamb Shanks")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambKatsu(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_lamb_recipe("Lamb Katsu")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambTeriyaki(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_lamb_recipe("Lamb Teriyaki")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambDonburi(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_lamb_recipe("Lamb Donburi")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambRamen(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_lamb_recipe("Lamb Ramen")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambYakiniku(Resource):
        def get(self):
            recipe = japanese_recipe_API.get_lamb_recipe("Lamb Yakiniku")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404
        
api.add_resource(SaveRecipe, '/save_recipe')
api.add_resource(UpdateRecipe, '/edit_recipe/<int:recipe_id>')
        
api.add_resource(japanese_recipe_API._ChickenTeriyaki, '/japanese_recipe/ChickenTeriyaki')
api.add_resource(japanese_recipe_API._ChickenKatsu, '/japanese_recipe/ChickenKatsu')
api.add_resource(japanese_recipe_API._ChickenYakitori, '/japanese_recipe/ChickenYakitori')
api.add_resource(japanese_recipe_API._ChickenRamen, '/japanese_recipe/ChickenRamen')
api.add_resource(japanese_recipe_API._ChickenKaraage, '/japanese_recipe/ChickenKaraage')
api.add_resource(japanese_recipe_API._ChickenDonburi, '/japanese_recipe/ChickenDonburi')

api.add_resource(japanese_recipe_API._BeefTeriyaki, '/japanese_recipe/BeefTeriyaki')
api.add_resource(japanese_recipe_API._BeefSukiyaki, '/japanese_recipe/BeefSukiyaki')
api.add_resource(japanese_recipe_API._Gyudon, '/japanese_recipe/Gyudon')
api.add_resource(japanese_recipe_API._BeefYakiniku, '/japanese_recipe/BeefYakiniku')
api.add_resource(japanese_recipe_API._BeefShabuShabu, '/japanese_recipe/BeefShabuShabu')
api.add_resource(japanese_recipe_API._BeefTataki, '/japanese_recipe/BeefTataki')

api.add_resource(japanese_recipe_API._VeganRamen, '/japanese_recipe/VeganRamen')
api.add_resource(japanese_recipe_API._VeganSushi, '/japanese_recipe/VeganSushi')
api.add_resource(japanese_recipe_API._VeganTempura, '/japanese_recipe/VeganTempura')
api.add_resource(japanese_recipe_API._VeganGyoza, '/japanese_recipe/VeganGyoza')
api.add_resource(japanese_recipe_API._VeganDonburi, '/japanese_recipe/VeganDonburi')
api.add_resource(japanese_recipe_API._VeganMisoSoup, '/japanese_recipe/VeganMisoSoup')

api.add_resource(japanese_recipe_API._GrilledSalmon, '/japanese_recipe/GrilledSalmon')
api.add_resource(japanese_recipe_API._SabaShioyaki, '/japanese_recipe/SabaShioyaki')
api.add_resource(japanese_recipe_API._UnagiDonburi, '/japanese_recipe/UnagiDonburi')
api.add_resource(japanese_recipe_API._TunaTataki, '/japanese_recipe/TunaTataki')
api.add_resource(japanese_recipe_API._FishKaraage, '/japanese_recipe/FishKaraage')
api.add_resource(japanese_recipe_API._FishMisoSoup, '/japanese_recipe/FishMisoSoup')

api.add_resource(japanese_recipe_API._BraisedLambShanks, '/japanese_recipe/BraisedLambShanks')
api.add_resource(japanese_recipe_API._LambKatsu, '/japanese_recipe/LambKatsu')
api.add_resource(japanese_recipe_API._LambTeriyaki, '/japanese_recipe/LambTeriyaki')
api.add_resource(japanese_recipe_API._LambDonburi, '/japanese_recipe/LambDonburi')
api.add_resource(japanese_recipe_API._LambRamen, '/japanese_recipe/LambRamen')
api.add_resource(japanese_recipe_API._LambYakiniku, '/japanese_recipe/LambYakiniku')

# Instantiate the japanese_recipe_API to register the endpoints
japanese_recipe_api_instance = japanese_recipe_API()