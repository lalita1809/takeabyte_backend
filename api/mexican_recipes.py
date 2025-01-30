from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource  # used for REST API building
from __init__ import db
from model.chinese_recipes import Recipe


mexican_recipe_api = Blueprint('mexican_recipe_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/
api = Api(mexican_recipe_api)

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


class mexican_recipe_API:
    @staticmethod
    def get_chicken_recipe(name):
        recipes = {
            "Chicken Enchiladas": {
                "dish": "Chicken Enchiladas",
                "time": 60,
                "ingredients": ["chicken", "tortillas", "cheese", "salsa", "spices"],
                "instructions": "Roll chicken in tortillas, top with cheese and salsa, bake."
            },
            "Chicken Tacos": {
                "dish": "Chicken Tacos",
                "time": 30,
                "ingredients": ["chicken", "taco shells", "lettuce", "cheese", "sour cream"],
                "instructions": "Fill taco shells with chicken, lettuce, cheese, and sour cream."
            },
            "Chicken Fajitas": {
                "dish": "Chicken Fajitas",
                "time": 25,
                "ingredients": ["chicken", "bell peppers", "onions", "fajita seasoning"],
                "instructions": "Sauté chicken, bell peppers, and onions with fajita seasoning."
            },
            "Pollo Asado": {
                "dish": "Pollo Asado",
                "time": 50,
                "ingredients": ["chicken", "citrus", "garlic", "spices"],
                "instructions": "Marinate chicken in citrus and spices, then grill."
            },
            "Chicken Quesadillas": {
                "dish": "Chicken Quesadillas",
                "time": 20,
                "ingredients": ["chicken", "cheese", "flour tortillas", "salsa"],
                "instructions": "Grill tortillas with cheese and chicken, serve with salsa."
            },
            "Chicken Tamales": {
                "dish": "Chicken Tamales",
                "time": 120,
                "ingredients": ["chicken", "masa", "corn husks", "salsa"],
                "instructions": "Fill masa with chicken, wrap in corn husks, steam."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_beef_recipe(name):
        recipes = {
            "Beef Enchiladas": {
                "dish": "Beef Enchiladas",
                "time": 60,
                "ingredients": ["beef", "tortillas", "cheese", "salsa", "spices"],
                "instructions": "Roll beef in tortillas, top with cheese and salsa, bake."
            },
            "Beef Tacos": {
                "dish": "Beef Tacos",
                "time": 30,
                "ingredients": ["beef", "taco shells", "lettuce", "cheese", "sour cream"],
                "instructions": "Fill taco shells with beef, lettuce, cheese, and sour cream."
            },
            "Beef Fajitas": {
                "dish": "Beef Fajitas",
                "time": 25,
                "ingredients": ["beef", "bell peppers", "onions", "fajita seasoning"],
                "instructions": "Sauté beef, bell peppers, and onions with fajita seasoning."
            },
            "Beef Burritos": {
                "dish": "Beef Burritos",
                "time": 30,
                "ingredients": ["beef", "tortillas", "rice", "beans", "cheese"],
                "instructions": "Roll beef, rice, beans, and cheese in tortillas."
            },
            "Beef Tostadas": {
                "dish": "Beef Tostadas",
                "time": 20,
                "ingredients": ["beef", "tostada shells", "lettuce", "cheese", "sour cream"],
                "instructions": "Top tostada shells with beef, lettuce, cheese, and sour cream."
            },
            "Carne Asada": {
                "dish": "Carne Asada",
                "time": 40,
                "ingredients": ["beef", "lime", "garlic", "spices"],
                "instructions": "Marinate beef in lime, garlic, and spices, then grill."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_vegan_recipe(name):
        recipes = {
            "Vegan Tacos": {
                "dish": "Vegan Tacos",
                "time": 20,
                "ingredients": ["taco shells", "lettuce", "avocado", "salsa", "beans"],
                "instructions": "Fill taco shells with lettuce, avocado, salsa, and beans."
            },
            "Vegan Burritos": {
                "dish": "Vegan Burritos",
                "time": 25,
                "ingredients": ["tortillas", "beans", "rice", "lettuce", "salsa"],
                "instructions": "Roll beans, rice, lettuce, and salsa in tortillas."
            },
            "Vegan Enchiladas": {
                "dish": "Vegan Enchiladas",
                "time": 50,
                "ingredients": ["tortillas", "beans", "vegan cheese", "salsa"],
                "instructions": "Roll beans and vegan cheese in tortillas, top with salsa and bake."
            },
            "Vegan Quesadillas": {
                "dish": "Vegan Quesadillas",
                "time": 20,
                "ingredients": ["flour tortillas", "vegan cheese", "salsa", "avocado"],
                "instructions": "Grill tortillas with vegan cheese, serve with salsa and avocado."
            },
            "Vegan Fajitas": {
                "dish": "Vegan Fajitas",
                "time": 25,
                "ingredients": ["bell peppers", "onions", "fajita seasoning", "tortillas"],
                "instructions": "Sauté bell peppers and onions with fajita seasoning, serve with tortillas."
            },
            "Vegan Tamales": {
                "dish": "Vegan Tamales",
                "time": 120,
                "ingredients": ["masa", "salsa", "corn husks", "vegan filling"],
                "instructions": "Fill masa with vegan filling, wrap in corn husks, steam."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_fish_recipe(name):
        recipes = {
            "Fish Tacos": {
                "dish": "Fish Tacos",
                "time": 20,
                "ingredients": ["fish", "taco shells", "cabbage", "salsa", "lime"],
                "instructions": "Fill taco shells with fish, cabbage, salsa, and a squeeze of lime."
            },
            "Crispy Fish Tacos": {
                "dish": "Crispy Fish Tacos",
                "time": 30,
                "ingredients": ["fish", "corn tortillas", "cabbage", "salsa", "lime"],
                "instructions": "Fry fish, place in corn tortillas, top with cabbage and salsa."
            },
            "Grilled Fish Burritos": {
                "dish": "Grilled Fish Burritos",
                "time": 30,
                "ingredients": ["fish", "tortillas", "rice", "beans", "salsa"],
                "instructions": "Grill fish and roll with rice, beans, and salsa in tortillas."
            },
            "Fish Veracruz": {
                "dish": "Fish Veracruz",
                "time": 45,
                "ingredients": ["fish", "tomatoes", "olives", "onions", "peppers"],
                "instructions": "Cook fish with tomatoes, olives, onions, and peppers."
            },
            "Fish Ceviche": {
                "dish": "Fish Ceviche",
                "time": 30,
                "ingredients": ["fish", "lime", "tomato", "onions", "cilantro"],
                "instructions": "Marinate fish in lime juice, mix with tomatoes, onions, and cilantro."
            },
            "Fish Fajitas": {
                "dish": "Fish Fajitas",
                "time": 25,
                "ingredients": ["fish", "bell peppers", "onions", "fajita seasoning", "tortillas"],
                "instructions": "Cook fish with bell peppers and onions, serve with tortillas."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_lamb_recipe(name):
        recipes = {
            "Lamb Tacos": {
                "dish": "Lamb Tacos",
                "time": 30,
                "ingredients": ["lamb", "taco shells", "onions", "cilantro", "salsa"],
                "instructions": "Cook lamb, fill taco shells with lamb, onions, cilantro, and salsa."
            },
            "Lamb Burritos": {
                "dish": "Lamb Burritos",
                "time": 25,
                "ingredients": ["lamb", "tortillas", "beans", "rice", "cheese"],
                "instructions": "Roll lamb, beans, rice, and cheese in tortillas."
            },
            "Lamb Fajitas": {
                "dish": "Lamb Fajitas",
                "time": 25,
                "ingredients": ["lamb", "bell peppers", "onions", "fajita seasoning", "tortillas"],
                "instructions": "Sauté lamb, bell peppers, and onions with fajita seasoning, serve with tortillas."
            },
            "Lamb Enchiladas": {
                "dish": "Lamb Enchiladas",
                "time": 60,
                "ingredients": ["lamb", "tortillas", "cheese", "salsa"],
                "instructions": "Roll lamb in tortillas, top with cheese and salsa, bake."
            },
            "Braised Lamb Shank": {
                "dish": "Braised Lamb Shank",
                "time": 120,
                "ingredients": ["lamb shank", "tomato", "onions", "spices"],
                "instructions": "Braised lamb shank in tomato and spices."
            },
            "Lamb Quesadillas": {
                "dish": "Lamb Quesadillas",
                "time": 20,
                "ingredients": ["lamb", "cheese", "flour tortillas", "salsa"],
                "instructions": "Grill tortillas with lamb and cheese, serve with salsa."
            }
        }
        return recipes.get(name)


    class _ChickenEnchiladas(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_chicken_recipe("Chicken Enchiladas")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChickenTacos(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_chicken_recipe("Chicken Tacos")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChickenFajitas(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_chicken_recipe("Chicken Fajitas")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _PolloAsado(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_chicken_recipe("Pollo Asado")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChickenQuesadillas(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_chicken_recipe("Chicken Quesadillas")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChickenTamales(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_chicken_recipe("Chicken Tamales")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefEnchiladas(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_beef_recipe("Beef Enchiladas")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefTacos(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_beef_recipe("Beef Tacos")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefFajitas(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_beef_recipe("Beef Fajitas")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefBurritos(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_beef_recipe("Beef Burritos")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefTostadas(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_beef_recipe("Beef Tostadas")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _CarneAsada(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_beef_recipe("Carne Asada")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganTacos(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_vegan_recipe("Vegan Tacos")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganBurritos(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_vegan_recipe("Vegan Burritos")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganEnchiladas(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_vegan_recipe("Vegan Enchiladas")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganQuesadillas(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_vegan_recipe("Vegan Quesadillas")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganFajitas(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_vegan_recipe("Vegan Fajitas")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganTamales(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_vegan_recipe("Vegan Tamales")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _FishTacos(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_fish_recipe("Fish Tacos")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _CrispyFishTacos(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_fish_recipe("Crispy Fish Tacos")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _GrilledFishBurritos(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_fish_recipe("Grilled Fish Burritos")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _FishVeracruz(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_fish_recipe("Fish Veracruz")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _FishCeviche(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_fish_recipe("Fish Ceviche")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _FishFajitas(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_fish_recipe("Fish Fajitas")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambTacos(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_lamb_recipe("Lamb Tacos")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambBurritos(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_lamb_recipe("Lamb Burritos")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambFajitas(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_lamb_recipe("Lamb Fajitas")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambEnchiladas(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_lamb_recipe("Lamb Enchiladas")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BraisedLambShank(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_lamb_recipe("Braised Lamb Shank")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambQuesadillas(Resource):
        def get(self):
            recipe = mexican_recipe_API.get_lamb_recipe("Lamb Quesadillas")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404
        
api.add_resource(SaveRecipe, '/save_recipe')
        
api.add_resource(mexican_recipe_API._ChickenEnchiladas, '/mexican_recipe/ChickenEnchiladas')
api.add_resource(mexican_recipe_API._ChickenTacos, '/mexican_recipe/ChickenTacos')
api.add_resource(mexican_recipe_API._ChickenFajitas, '/mexican_recipe/ChickenFajitas')
api.add_resource(mexican_recipe_API._PolloAsado, '/mexican_recipe/PolloAsado')
api.add_resource(mexican_recipe_API._ChickenQuesadillas, '/mexican_recipe/ChickenQuesadillas')
api.add_resource(mexican_recipe_API._ChickenTamales, '/mexican_recipe/ChickenTamales')

api.add_resource(mexican_recipe_API._BeefEnchiladas, '/mexican_recipe/BeefEnchiladas')
api.add_resource(mexican_recipe_API._BeefTacos, '/mexican_recipe/BeefTacos')
api.add_resource(mexican_recipe_API._BeefFajitas, '/mexican_recipe/BeefFajitas')
api.add_resource(mexican_recipe_API._BeefBurritos, '/mexican_recipe/BeefBurritos')
api.add_resource(mexican_recipe_API._BeefTostadas, '/mexican_recipe/BeefTostadas')
api.add_resource(mexican_recipe_API._CarneAsada, '/mexican_recipe/CarneAsada')

api.add_resource(mexican_recipe_API._VeganTacos, '/mexican_recipe/VeganTacos')
api.add_resource(mexican_recipe_API._VeganBurritos, '/mexican_recipe/VeganBurritos')
api.add_resource(mexican_recipe_API._VeganEnchiladas, '/mexican_recipe/VeganEnchiladas')
api.add_resource(mexican_recipe_API._VeganQuesadillas, '/mexican_recipe/VeganQuesadillas')
api.add_resource(mexican_recipe_API._VeganFajitas, '/mexican_recipe/VeganFajitas')
api.add_resource(mexican_recipe_API._VeganTamales, '/mexican_recipe/VeganTamales')

api.add_resource(mexican_recipe_API._FishTacos, '/mexican_recipe/FishTacos')
api.add_resource(mexican_recipe_API._CrispyFishTacos, '/mexican_recipe/CrispyFishTacos')
api.add_resource(mexican_recipe_API._GrilledFishBurritos, '/mexican_recipe/GrilledFishBurritos')
api.add_resource(mexican_recipe_API._FishVeracruz, '/mexican_recipe/FishVeracruz')
api.add_resource(mexican_recipe_API._FishCeviche, '/mexican_recipe/FishCeviche')
api.add_resource(mexican_recipe_API._FishFajitas, '/mexican_recipe/FishFajitas')

api.add_resource(mexican_recipe_API._LambTacos, '/mexican_recipe/LambTacos')
api.add_resource(mexican_recipe_API._LambBurritos, '/mexican_recipe/LambBurritos')
api.add_resource(mexican_recipe_API._LambFajitas, '/mexican_recipe/LambFajitas')
api.add_resource(mexican_recipe_API._LambEnchiladas, '/mexican_recipe/LambEnchiladas')
api.add_resource(mexican_recipe_API._BraisedLambShank, '/mexican_recipe/BraisedLambShank')
api.add_resource(mexican_recipe_API._LambQuesadillas, '/mexican_recipe/LambQuesadillas')

# Instantiate the mexican_recipe_API to register the endpoints
mexican_recipe_api_instance = mexican_recipe_API()