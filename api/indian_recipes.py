from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource  # used for REST API building
from __init__ import db
from model.chinese_recipes import Recipe

indian_recipe_api = Blueprint('indian_recipe_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/
api = Api(indian_recipe_api)


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

class indian_recipe_API:
    @staticmethod
    def get_chicken_recipe(name):
        recipes = {
            "Butter Chicken": {
                "dish": "Butter Chicken",
                "time": 60,
                "ingredients": ["chicken", "butter", "cream", "tomato", "spices"],
                "instructions": "Cook chicken in a creamy tomato sauce with spices."
            },
            "Chicken Tikka Masala": {
                "dish": "Chicken Tikka Masala",
                "time": 50,
                "ingredients": ["chicken", "yogurt", "spices", "tomato", "onion"],
                "instructions": "Grill marinated chicken and simmer in a spicy tomato sauce."
            },
            "Chicken Korma": {
                "dish": "Chicken Korma",
                "time": 70,
                "ingredients": ["chicken", "cream", "yogurt", "cashews", "spices"],
                "instructions": "Cook chicken in a rich and creamy cashew gravy."
            },
            "Chicken Vindaloo": {
                "dish": "Chicken Vindaloo",
                "time": 60,
                "ingredients": ["chicken", "vinegar", "spices", "potatoes"],
                "instructions": "Cook chicken in a spicy, tangy vinegar-based sauce."
            },
            "Chicken Saag": {
                "dish": "Chicken Saag",
                "time": 55,
                "ingredients": ["chicken", "spinach", "onions", "garlic", "spices"],
                "instructions": "Cook chicken with spinach and spices."
            },
            "Chicken Biryani": {
                "dish": "Chicken Biryani",
                "time": 90,
                "ingredients": ["chicken", "rice", "yogurt", "spices", "saffron"],
                "instructions": "Cook marinated chicken with rice and aromatic spices."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_beef_recipe(name):
        recipes = {
            "Beef Curry": {
                "dish": "Beef Curry",
                "time": 60,
                "ingredients": ["beef", "onions", "garlic", "tomato", "spices"],
                "instructions": "Cook beef in a rich, spiced tomato gravy."
            },
            "Beef Vindaloo": {
                "dish": "Beef Vindaloo",
                "time": 70,
                "ingredients": ["beef", "vinegar", "spices", "potatoes"],
                "instructions": "Cook beef in a tangy, spicy gravy with potatoes."
            },
            "Beef Keema": {
                "dish": "Beef Keema",
                "time": 50,
                "ingredients": ["beef", "peas", "onions", "garlic", "spices"],
                "instructions": "Cook minced beef with peas and spices."
            },
            "Beef Rogan Josh": {
                "dish": "Beef Rogan Josh",
                "time": 90,
                "ingredients": ["beef", "yogurt", "garlic", "onions", "spices"],
                "instructions": "Slow-cook beef in a yogurt-based gravy with aromatic spices."
            },
            "Beef Biryani": {
                "dish": "Beef Biryani",
                "time": 100,
                "ingredients": ["beef", "rice", "yogurt", "spices", "onions"],
                "instructions": "Cook marinated beef with rice and fragrant spices."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_vegan_recipe(name):
        recipes = {
            "Chana Masala": {
                "dish": "Chana Masala",
                "time": 45,
                "ingredients": ["chickpeas", "tomato", "onion", "spices"],
                "instructions": "Cook chickpeas in a spicy, tangy tomato gravy."
            },
            "Aloo Gobi": {
                "dish": "Aloo Gobi",
                "time": 40,
                "ingredients": ["potatoes", "cauliflower", "onions", "garlic", "spices"],
                "instructions": "Cook potatoes and cauliflower with spices."
            },
            "Baingan Bharta": {
                "dish": "Baingan Bharta",
                "time": 50,
                "ingredients": ["eggplant", "tomato", "onions", "garlic", "spices"],
                "instructions": "Roast eggplant and cook with tomato and spices."
            },
            "Vegan Tikka Masala": {
                "dish": "Vegan Tikka Masala",
                "time": 55,
                "ingredients": ["tofu", "tomato", "onions", "spices", "cream"],
                "instructions": "Cook tofu in a creamy, spiced tomato sauce."
            },
            "Vegan Biryani": {
                "dish": "Vegan Biryani",
                "time": 90,
                "ingredients": ["tofu", "rice", "spices", "onions", "saffron"],
                "instructions": "Cook tofu with rice and aromatic spices."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_fish_recipe(name):
        recipes = {
            "Fish Curry": {
                "dish": "Fish Curry",
                "time": 50,
                "ingredients": ["fish", "coconut milk", "tomato", "spices"],
                "instructions": "Cook fish in a creamy coconut curry sauce."
            },
            "Goan Fish Curry": {
                "dish": "Goan Fish Curry",
                "time": 60,
                "ingredients": ["fish", "tamarind", "coconut milk", "spices"],
                "instructions": "Cook fish in a tangy, spicy coconut-based gravy."
            },
            "Fish Tikka": {
                "dish": "Fish Tikka",
                "time": 40,
                "ingredients": ["fish", "yogurt", "spices", "lemon"],
                "instructions": "Marinate fish in yogurt and spices, then grill."
            },
            "Fish Fry": {
                "dish": "Fish Fry",
                "time": 30,
                "ingredients": ["fish", "spices", "flour", "oil"],
                "instructions": "Coat fish in spices and fry until crispy."
            },
            "Masala Fish": {
                "dish": "Masala Fish",
                "time": 50,
                "ingredients": ["fish", "onions", "tomato", "garlic", "spices"],
                "instructions": "Cook fish with a spicy, flavorful gravy."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_lamb_recipe(name):
        recipes = {
            "Lamb Curry": {
                "dish": "Lamb Curry",
                "time": 60,
                "ingredients": ["lamb", "onions", "tomato", "spices", "garlic"],
                "instructions": "Cook lamb in a spiced tomato gravy."
            },
            "Lamb Rogan Josh": {
                "dish": "Lamb Rogan Josh",
                "time": 90,
                "ingredients": ["lamb", "yogurt", "garlic", "spices", "onions"],
                "instructions": "Slow-cook lamb in a yogurt-based sauce with aromatic spices."
            },
            "Lamb Korma": {
                "dish": "Lamb Korma",
                "time": 70,
                "ingredients": ["lamb", "cream", "yogurt", "cashews", "spices"],
                "instructions": "Cook lamb in a rich, creamy cashew gravy."
            },
            "Lamb Keema": {
                "dish": "Lamb Keema",
                "time": 50,
                "ingredients": ["lamb", "peas", "onions", "garlic", "spices"],
                "instructions": "Cook minced lamb with peas and spices."
            },
            "Lamb Biryani": {
                "dish": "Lamb Biryani",
                "time": 100,
                "ingredients": ["lamb", "rice", "yogurt", "spices", "onions"],
                "instructions": "Cook marinated lamb with rice and aromatic spices."
            }
        }
        return recipes.get(name)


    class _ButterChicken(Resource):
        def get(self):
            recipe = indian_recipe_API.get_chicken_recipe("Butter Chicken")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChickenTikkaMasala(Resource):
        def get(self):
            recipe = indian_recipe_API.get_chicken_recipe("Chicken Tikka Masala")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChickenKorma(Resource):
        def get(self):
            recipe = indian_recipe_API.get_chicken_recipe("Chicken Korma")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChickenVindaloo(Resource):
        def get(self):
            recipe = indian_recipe_API.get_chicken_recipe("Chicken Vindaloo")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChickenSaag(Resource):
        def get(self):
            recipe = indian_recipe_API.get_chicken_recipe("Chicken Saag")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChickenBiryani(Resource):
        def get(self):
            recipe = indian_recipe_API.get_chicken_recipe("Chicken Biryani")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefCurry(Resource):
        def get(self):
            recipe = indian_recipe_API.get_beef_recipe("Beef Curry")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefVindaloo(Resource):
        def get(self):
            recipe = indian_recipe_API.get_beef_recipe("Beef Vindaloo")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefKeema(Resource):
        def get(self):
            recipe = indian_recipe_API.get_beef_recipe("Beef Keema")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefRoganJosh(Resource):
        def get(self):
            recipe = indian_recipe_API.get_beef_recipe("Beef Rogan Josh")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefBiryani(Resource):
        def get(self):
            recipe = indian_recipe_API.get_beef_recipe("Beef Biryani")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChanaMasala(Resource):
        def get(self):
            recipe = indian_recipe_API.get_vegan_recipe("Chana Masala")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _AlooGobi(Resource):
        def get(self):
            recipe = indian_recipe_API.get_vegan_recipe("Aloo Gobi")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BainganBharta(Resource):
        def get(self):
            recipe = indian_recipe_API.get_vegan_recipe("Baingan Bharta")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganTikkaMasala(Resource):
        def get(self):
            recipe = indian_recipe_API.get_vegan_recipe("Vegan Tikka Masala")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganBiryani(Resource):
        def get(self):
            recipe = indian_recipe_API.get_vegan_recipe("Vegan Biryani")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _FishCurry(Resource):
        def get(self):
            recipe = indian_recipe_API.get_fish_recipe("Fish Curry")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _GoanFishCurry(Resource):
        def get(self):
            recipe = indian_recipe_API.get_fish_recipe("Goan Fish Curry")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _FishTikka(Resource):
        def get(self):
            recipe = indian_recipe_API.get_fish_recipe("Fish Tikka")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _FishFry(Resource):
        def get(self):
            recipe = indian_recipe_API.get_fish_recipe("Fish Fry")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _MasalaFish(Resource):
        def get(self):
            recipe = indian_recipe_API.get_fish_recipe("Masala Fish")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambCurry(Resource):
        def get(self):
            recipe = indian_recipe_API.get_lamb_recipe("Lamb Curry")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambRoganJosh(Resource):
        def get(self):
            recipe = indian_recipe_API.get_lamb_recipe("Lamb Rogan Josh")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambKorma(Resource):
        def get(self):
            recipe = indian_recipe_API.get_lamb_recipe("Lamb Korma")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambKeema(Resource):
        def get(self):
            recipe = indian_recipe_API.get_lamb_recipe("Lamb Keema")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambBiryani(Resource):
        def get(self):
            recipe = indian_recipe_API.get_lamb_recipe("Lamb Biryani")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404
        
api.add_resource(SaveRecipe, '/save_recipe')
        
api.add_resource(indian_recipe_API._ButterChicken, '/indian_recipe/ButterChicken')
api.add_resource(indian_recipe_API._ChickenTikkaMasala, '/indian_recipe/ChickenTikkaMasala')
api.add_resource(indian_recipe_API._ChickenKorma, '/indian_recipe/ChickenKorma')
api.add_resource(indian_recipe_API._ChickenVindaloo, '/indian_recipe/ChickenVindaloo')
api.add_resource(indian_recipe_API._ChickenSaag, '/indian_recipe/ChickenSaag')
api.add_resource(indian_recipe_API._ChickenBiryani, '/indian_recipe/ChickenBiryani')

api.add_resource(indian_recipe_API._BeefCurry, '/indian_recipe/BeefCurry')
api.add_resource(indian_recipe_API._BeefVindaloo, '/indian_recipe/BeefVindaloo')
api.add_resource(indian_recipe_API._BeefKeema, '/indian_recipe/BeefKeema')
api.add_resource(indian_recipe_API._BeefRoganJosh, '/indian_recipe/BeefRoganJosh')
api.add_resource(indian_recipe_API._BeefBiryani, '/indian_recipe/BeefBiryani')

api.add_resource(indian_recipe_API._ChanaMasala, '/indian_recipe/ChanaMasala')
api.add_resource(indian_recipe_API._AlooGobi, '/indian_recipe/AlooGobi')
api.add_resource(indian_recipe_API._BainganBharta, '/indian_recipe/BainganBharta')
api.add_resource(indian_recipe_API._VeganTikkaMasala, '/indian_recipe/VeganTikkaMasala')
api.add_resource(indian_recipe_API._VeganBiryani, '/indian_recipe/VeganBiryani')

api.add_resource(indian_recipe_API._FishCurry, '/indian_recipe/FishCurry')
api.add_resource(indian_recipe_API._GoanFishCurry, '/indian_recipe/GoanFishCurry')
api.add_resource(indian_recipe_API._FishTikka, '/indian_recipe/FishTikka')
api.add_resource(indian_recipe_API._FishFry, '/indian_recipe/FishFry')
api.add_resource(indian_recipe_API._MasalaFish, '/indian_recipe/MasalaFish')

api.add_resource(indian_recipe_API._LambCurry, '/indian_recipe/LambCurry')
api.add_resource(indian_recipe_API._LambRoganJosh, '/indian_recipe/LambRoganJosh')
api.add_resource(indian_recipe_API._LambKorma, '/indian_recipe/LambKorma')
api.add_resource(indian_recipe_API._LambKeema, '/indian_recipe/LambKeema')
api.add_resource(indian_recipe_API._LambBiryani, '/indian_recipe/LambBiryani')

# Instantiate the indian_recipe_API to register the endpoints
indian_recipe_api_instance = indian_recipe_API()