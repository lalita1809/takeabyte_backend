from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource  # used for REST API building
from __init__ import db
from model.chinese_recipes import Recipe

thai_recipe_api = Blueprint('thai_recipe_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/
api = Api(thai_recipe_api)

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

class thai_recipe_API:
    @staticmethod
    def get_chicken_recipe(name):
        recipes = {
            "Pad Thai Chicken": {
                "dish": "Pad Thai Chicken",
                "time": 30,
                "ingredients": ["chicken", "rice noodles", "peanuts", "lime", "spices", "egg"],
                "instructions": "Stir-fry chicken, add noodles, peanuts, and spices."
            },
            "Thai Green Curry Chicken": {
                "dish": "Thai Green Curry Chicken",
                "time": 50,
                "ingredients": ["chicken", "coconut milk", "green curry paste", "bamboo shoots", "basil"],
                "instructions": "Cook chicken in curry paste and coconut milk. Add vegetables."
            },
            "Thai Basil Chicken": {
                "dish": "Thai Basil Chicken",
                "time": 25,
                "ingredients": ["chicken", "basil", "garlic", "chilies", "soy sauce"],
                "instructions": "Stir-fry chicken with garlic, basil, and chilies."
            },
            "Thai Red Curry Chicken": {
                "dish": "Thai Red Curry Chicken",
                "time": 50,
                "ingredients": ["chicken", "coconut milk", "red curry paste", "vegetables"],
                "instructions": "Cook chicken in red curry paste with coconut milk and vegetables."
            },
            "Thai Lemon Chicken": {
                "dish": "Thai Lemon Chicken",
                "time": 35,
                "ingredients": ["chicken", "lemongrass", "garlic", "lime", "fish sauce"],
                "instructions": "Marinate chicken with lemongrass and garlic, then grill or stir-fry."
            },
            "Thai Chicken Satay": {
                "dish": "Thai Chicken Satay",
                "time": 40,
                "ingredients": ["chicken", "peanut butter", "curry powder", "coconut milk", "skewers"],
                "instructions": "Marinate chicken in spices, thread onto skewers, and grill. Serve with peanut sauce."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_beef_recipe(name):
        recipes = {
            "Pad Thai Beef": {
                "dish": "Pad Thai Beef",
                "time": 30,
                "ingredients": ["beef", "rice noodles", "peanuts", "lime", "spices", "egg"],
                "instructions": "Stir-fry beef, add noodles, peanuts, and spices."
            },
            "Thai Beef Salad": {
                "dish": "Thai Beef Salad",
                "time": 20,
                "ingredients": ["beef", "lettuce", "cilantro", "lime", "fish sauce"],
                "instructions": "Grill beef, slice thin, and toss with fresh vegetables and dressing."
            },
            "Thai Red Curry Beef": {
                "dish": "Thai Red Curry Beef",
                "time": 50,
                "ingredients": ["beef", "coconut milk", "red curry paste", "vegetables"],
                "instructions": "Cook beef in red curry paste with coconut milk and vegetables."
            },
            "Thai Basil Beef": {
                "dish": "Thai Basil Beef",
                "time": 25,
                "ingredients": ["beef", "basil", "garlic", "chilies", "soy sauce"],
                "instructions": "Stir-fry beef with garlic, basil, and chilies."
            },
            "Thai Beef Skewers": {
                "dish": "Thai Beef Skewers",
                "time": 35,
                "ingredients": ["beef", "soy sauce", "ginger", "garlic", "lemongrass"],
                "instructions": "Marinate beef in soy sauce and ginger, thread onto skewers, and grill."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_vegan_recipe(name):
        recipes = {
            "Vegan Pad Thai": {
                "dish": "Vegan Pad Thai",
                "time": 30,
                "ingredients": ["tofu", "rice noodles", "peanuts", "lime", "spices"],
                "instructions": "Stir-fry tofu, add noodles, peanuts, and spices."
            },
            "Vegan Thai Green Curry": {
                "dish": "Vegan Thai Green Curry",
                "time": 50,
                "ingredients": ["tofu", "coconut milk", "green curry paste", "bamboo shoots", "basil"],
                "instructions": "Cook tofu in curry paste and coconut milk. Add vegetables."
            },
            "Vegan Thai Basil Stir-fry": {
                "dish": "Vegan Thai Basil Stir-fry",
                "time": 25,
                "ingredients": ["tofu", "basil", "garlic", "chilies", "soy sauce"],
                "instructions": "Stir-fry tofu with garlic, basil, and chilies."
            },
            "Vegan Thai Red Curry": {
                "dish": "Vegan Thai Red Curry",
                "time": 50,
                "ingredients": ["tofu", "coconut milk", "red curry paste", "vegetables"],
                "instructions": "Cook tofu in red curry paste with coconut milk and vegetables."
            },
            "Vegan Thai Salad": {
                "dish": "Vegan Thai Salad",
                "time": 20,
                "ingredients": ["lettuce", "carrot", "cucumber", "cilantro", "lime", "peanut sauce"],
                "instructions": "Toss fresh vegetables with cilantro and peanut sauce."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_fish_recipe(name):
        recipes = {
            "Thai Fish Curry": {
                "dish": "Thai Fish Curry",
                "time": 50,
                "ingredients": ["fish", "coconut milk", "red curry paste", "vegetables", "lime"],
                "instructions": "Cook fish in curry paste with coconut milk and vegetables."
            },
            "Thai Steamed Fish with Lime and Garlic": {
                "dish": "Thai Steamed Fish with Lime and Garlic",
                "time": 30,
                "ingredients": ["whole fish", "lime", "garlic", "fish sauce", "spring onions"],
                "instructions": "Steam fish with lime, garlic, and fish sauce."
            },
            "Thai Fish Cakes": {
                "dish": "Thai Fish Cakes",
                "time": 25,
                "ingredients": ["fish", "green curry paste", "basil", "fish sauce"],
                "instructions": "Mix fish with curry paste, form into cakes, and fry."
            },
            "Crispy Thai Fish Fillets": {
                "dish": "Crispy Thai Fish Fillets",
                "time": 20,
                "ingredients": ["fish fillets", "cornstarch", "soy sauce", "garlic"],
                "instructions": "Fry fish fillets, toss in soy sauce and garlic."
            },
            "Grilled Thai Fish Skewers": {
                "dish": "Grilled Thai Fish Skewers",
                "time": 35,
                "ingredients": ["fish", "lemongrass", "lime", "soy sauce", "garlic"],
                "instructions": "Marinate fish in lemongrass and soy sauce, thread onto skewers, and grill."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_lamb_recipe(name):
        recipes = {
            "Thai Braised Lamb": {
                "dish": "Thai Braised Lamb",
                "time": 60,
                "ingredients": ["lamb", "coconut milk", "green curry paste", "vegetables"],
                "instructions": "Cook lamb with green curry paste and coconut milk."
            },
            "Thai Lamb Skewers": {
                "dish": "Thai Lamb Skewers",
                "time": 35,
                "ingredients": ["lamb", "ginger", "garlic", "lemongrass", "soy sauce"],
                "instructions": "Marinate lamb in soy sauce, ginger, and garlic, thread onto skewers, and grill."
            },
            "Thai Lamb Red Curry": {
                "dish": "Thai Lamb Red Curry",
                "time": 50,
                "ingredients": ["lamb", "coconut milk", "red curry paste", "vegetables"],
                "instructions": "Cook lamb in red curry paste with coconut milk and vegetables."
            },
            "Crying Tiger Lamb": {
                "dish": "Crying Tiger Lamb",
                "time": 40,
                "ingredients": ["lamb", "spices", "lime", "fish sauce"],
                "instructions": "Grill marinated lamb and serve with a tangy dipping sauce."
            },
            "Thai Massaman Lamb Curry": {
                "dish": "Thai Massaman Lamb Curry",
                "time": 70,
                "ingredients": ["lamb", "coconut milk", "cinnamon", "star anise", "potato", "chicken broth"],
                "instructions": "Cook lamb with Massaman curry paste, coconut milk, and spices."
            },
            "Thai Basil and Lemongrass Rack of Lamb": {
                "dish": "Thai Basil and Lemongrass Rack of Lamb",
                "time": 90,
                "ingredients": ["lamb racks", "basil", "lemongrass", "garlic", "soy sauce"],
                "instructions": "Marinate lamb racks with basil, lemongrass, and garlic, then grill."
            }
        }
        return recipes.get(name)


    class _PadThaiChicken(Resource):
        def get(self):
            recipe = thai_recipe_API.get_chicken_recipe("Pad Thai Chicken")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiGreenCurryChicken(Resource):
        def get(self):
            recipe = thai_recipe_API.get_chicken_recipe("Thai Green Curry Chicken")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiBasilChicken(Resource):
        def get(self):
            recipe = thai_recipe_API.get_chicken_recipe("Thai Basil Chicken")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiRedCurryChicken(Resource):
        def get(self):
            recipe = thai_recipe_API.get_chicken_recipe("Thai Red Curry Chicken")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiLemonChicken(Resource):
        def get(self):
            recipe = thai_recipe_API.get_chicken_recipe("Thai Lemon Chicken")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiChickenSatay(Resource):
        def get(self):
            recipe = thai_recipe_API.get_chicken_recipe("Thai Chicken Satay")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _PadThaiBeef(Resource):
        def get(self):
            recipe = thai_recipe_API.get_beef_recipe("Pad Thai Beef")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiBeefSalad(Resource):
        def get(self):
            recipe = thai_recipe_API.get_beef_recipe("Thai Beef Salad")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiRedCurryBeef(Resource):
        def get(self):
            recipe = thai_recipe_API.get_beef_recipe("Thai Red Curry Beef")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiBasilBeef(Resource):
        def get(self):
            recipe = thai_recipe_API.get_beef_recipe("Thai Basil Beef")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiBeefSkewers(Resource):
        def get(self):
            recipe = thai_recipe_API.get_beef_recipe("Thai Beef Skewers")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganPadThai(Resource):
        def get(self):
            recipe = thai_recipe_API.get_vegan_recipe("Vegan Pad Thai")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganThaiGreenCurry(Resource):
        def get(self):
            recipe = thai_recipe_API.get_vegan_recipe("Vegan Thai Green Curry")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganThaiBasilStirfry(Resource):
        def get(self):
            recipe = thai_recipe_API.get_vegan_recipe("Vegan Thai Basil Stir-fry")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganThaiRedCurry(Resource):
        def get(self):
            recipe = thai_recipe_API.get_vegan_recipe("Vegan Thai Red Curry")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganThaiSalad(Resource):
        def get(self):
            recipe = thai_recipe_API.get_vegan_recipe("Vegan Thai Salad")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiFishCurry(Resource):
        def get(self):
            recipe = thai_recipe_API.get_fish_recipe("Thai Fish Curry")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiSteamedFish(Resource):
        def get(self):
            recipe = thai_recipe_API.get_fish_recipe("Thai Steamed Fish with Lime and Garlic")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiFishCakes(Resource):
        def get(self):
            recipe = thai_recipe_API.get_fish_recipe("Thai Fish Cakes")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _CrispyThaiFishFillets(Resource):
        def get(self):
            recipe = thai_recipe_API.get_fish_recipe("Crispy Thai Fish Fillets")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _GrilledThaiFishSkewers(Resource):
        def get(self):
            recipe = thai_recipe_API.get_fish_recipe("Grilled Thai Fish Skewers")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiBraisedLamb(Resource):
        def get(self):
            recipe = thai_recipe_API.get_lamb_recipe("Thai Braised Lamb")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiLambSkewers(Resource):
        def get(self):
            recipe = thai_recipe_API.get_lamb_recipe("Thai Lamb Skewers")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiLambRedCurry(Resource):
        def get(self):
            recipe = thai_recipe_API.get_lamb_recipe("Thai Lamb Red Curry")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _CryingTigerLamb(Resource):
        def get(self):
            recipe = thai_recipe_API.get_lamb_recipe("Crying Tiger Lamb")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiMassamanLambCurry(Resource):
        def get(self):
            recipe = thai_recipe_API.get_lamb_recipe("Thai Massaman Lamb Curry")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ThaiBasilAndLemongrassRackofLamb(Resource):
        def get(self):
            recipe = thai_recipe_API.get_lamb_recipe("Thai Basil and Lemongrass Rack of Lamb")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404
        
api.add_resource(SaveRecipe, '/save_recipe')
api.add_resource(UpdateRecipe, '/edit_recipe/<int:recipe_id>')
        
api.add_resource(thai_recipe_API._PadThaiChicken, '/thai_recipe/PadThaiChicken')
api.add_resource(thai_recipe_API._ThaiGreenCurryChicken, '/thai_recipe/ThaiGreenCurryChicken')
api.add_resource(thai_recipe_API._ThaiBasilChicken, '/thai_recipe/ThaiBasilChicken')
api.add_resource(thai_recipe_API._ThaiRedCurryChicken, '/thai_recipe/ThaiRedCurryChicken')
api.add_resource(thai_recipe_API._ThaiLemonChicken, '/thai_recipe/ThaiLemonChicken')
api.add_resource(thai_recipe_API._ThaiChickenSatay, '/thai_recipe/ThaiChickenSatay')

api.add_resource(thai_recipe_API._PadThaiBeef, '/thai_recipe/PadThaiBeef')
api.add_resource(thai_recipe_API._ThaiBeefSalad, '/thai_recipe/ThaiBeefSalad')
api.add_resource(thai_recipe_API._ThaiRedCurryBeef, '/thai_recipe/ThaiRedCurryBeef')
api.add_resource(thai_recipe_API._ThaiBasilBeef, '/thai_recipe/ThaiBasilBeef')
api.add_resource(thai_recipe_API._ThaiBeefSkewers, '/thai_recipe/ThaiBeefSkewers')

api.add_resource(thai_recipe_API._VeganPadThai, '/thai_recipe/VeganPadThai')
api.add_resource(thai_recipe_API._VeganThaiGreenCurry, '/thai_recipe/VeganThaiGreenCurry')
api.add_resource(thai_recipe_API._VeganThaiBasilStirfry, '/thai_recipe/VeganThaiBasilStirfry')
api.add_resource(thai_recipe_API._VeganThaiRedCurry, '/thai_recipe/VeganThaiRedCurry')
api.add_resource(thai_recipe_API._VeganThaiSalad, '/thai_recipe/VeganThaiSalad')

api.add_resource(thai_recipe_API._ThaiFishCurry, '/thai_recipe/ThaiFishCurry')
api.add_resource(thai_recipe_API._ThaiSteamedFish, '/thai_recipe/ThaiSteamedFish')
api.add_resource(thai_recipe_API._ThaiFishCakes, '/thai_recipe/ThaiFishCakes')
api.add_resource(thai_recipe_API._CrispyThaiFishFillets, '/thai_recipe/CrispyThaiFishFillets')
api.add_resource(thai_recipe_API._GrilledThaiFishSkewers, '/thai_recipe/GrilledThaiFishSkewers')

api.add_resource(thai_recipe_API._ThaiBraisedLamb, '/thai_recipe/ThaiBraisedLamb')
api.add_resource(thai_recipe_API._ThaiLambSkewers, '/thai_recipe/ThaiLambSkewers')
api.add_resource(thai_recipe_API._ThaiLambRedCurry, '/thai_recipe/ThaiLambRedCurry')
api.add_resource(thai_recipe_API._CryingTigerLamb, '/thai_recipe/CryingTigerLamb')
api.add_resource(thai_recipe_API._ThaiMassamanLambCurry, '/thai_recipe/ThaiMassamanLambCurry')
api.add_resource(thai_recipe_API._ThaiBasilAndLemongrassRackofLamb, '/thai_recipe/ThaiBasilAndLemongrassRackofLamb')

# Instantiate the thai_recipe_API to register the endpoints
thai_recipe_api_instance = thai_recipe_API()