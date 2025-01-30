from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource  # used for REST API building
from __init__ import db
from model.chinese_recipes import Recipe

italian_recipe_api = Blueprint('italian_recipe_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/
api = Api(italian_recipe_api)

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


class italian_recipe_API:
    @staticmethod
    def get_chicken_recipe(name):
        recipes = {
            "Chicken Parmesan": {
                "dish": "Chicken Parmesan",
                "time": 60,
                "ingredients": ["4 boneless chicken breasts", "1 cup breadcrumbs", "1/2 cup grated parmesan", "2 cups tomato sauce", "1 cup shredded mozzarella"],
                "instructions": "Bread and fry chicken in breadcrumbs, top with tomato sauce and shredded mozzarella cheese, bake at 375°F for 20 minutes until golden and bubbly."
            },
            "Chicken Alfredo": {
                "dish": "Chicken Alfredo",
                "time": 30,
                "ingredients": ["4 boneless chicken breasts", "12 oz fettuccine pasta", "1 cup heavy cream", "1/2 cup grated parmesan", "2 tbsp butter"],
                "instructions": "Cook chicken breasts in butter, slice them thinly. Prepare Alfredo sauce with cream and parmesan, toss with cooked fettuccine."
            },
            "Chicken Marsala": {
                "dish": "Chicken Marsala",
                "time": 40,
                "ingredients": ["4 boneless chicken breasts", "1 cup sliced mushrooms", "3/4 cup Marsala wine", "2 tbsp butter", "2 cloves garlic (minced)"],
                "instructions": "Cook chicken breasts in butter, sauté mushrooms and garlic. Deglaze with Marsala wine, reduce sauce, and serve over chicken."
            },
            "Chicken Piccata": {
                "dish": "Chicken Piccata",
                "time": 35,
                "ingredients": ["4 boneless chicken breasts", "1 lemon (sliced)", "2 tbsp capers", "2 tbsp butter", "1/4 cup white wine"],
                "instructions": "Cook chicken in butter until golden, make sauce by adding lemon, capers, white wine, and butter. Simmer and serve."
            },
            "Chicken Cacciatore": {
                "dish": "Chicken Cacciatore",
                "time": 75,
                "ingredients": ["4 chicken thighs", "2 large tomatoes (chopped)", "1 bell pepper (chopped)", "1 onion (chopped)", "1 cup sliced mushrooms"],
                "instructions": "Simmer chicken with tomatoes, bell peppers, onions, mushrooms, and garlic until chicken is tender and sauce has thickened."
            },
            "Chicken Risotto": {
                "dish": "Chicken Risotto",
                "time": 50,
                "ingredients": ["2 boneless chicken breasts", "1 cup arborio rice", "3 cups chicken broth", "1/2 cup grated parmesan", "1/4 cup white wine"],
                "instructions": "Cook chicken, slice thinly. Prepare risotto by simmering arborio rice in chicken broth and wine, stir in parmesan and sliced chicken."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_beef_recipe(name):
        recipes = {
            "Beef Lasagna": {
                "dish": "Beef Lasagna",
                "time": 90,
                "ingredients": ["1 lb ground beef", "12 lasagna noodles", "1 1/2 cups ricotta cheese", "3 cups tomato sauce", "2 cups mozzarella cheese"],
                "instructions": "Layer cooked noodles, beef, ricotta, and tomato sauce in a baking dish, top with mozzarella, and bake at 375°F for 30 minutes."
            },
            "Spaghetti Bolognese": {
                "dish": "Spaghetti Bolognese",
                "time": 60,
                "ingredients": ["1 lb ground beef", "12 oz spaghetti", "2 cups tomato sauce", "1 carrot (chopped)", "1 celery stalk (chopped)", "1 onion (chopped)"],
                "instructions": "Simmer beef with tomato sauce and chopped vegetables, serve over cooked spaghetti."
            },
            "Beef Braciole": {
                "dish": "Beef Braciole",
                "time": 120,
                "ingredients": ["1 lb beef flank steak", "1/2 cup breadcrumbs", "1/4 cup grated parmesan", "2 cups tomato sauce", "2 cloves garlic (minced)"],
                "instructions": "Roll beef with breadcrumbs and cheese, sear, then simmer in tomato sauce until tender."
            },
            "Beef Florentine": {
                "dish": "Beef Florentine",
                "time": 45,
                "ingredients": ["1 lb beef sirloin", "2 cups fresh spinach", "1/2 cup cream", "2 cloves garlic (minced)", "1/2 cup grated parmesan"],
                "instructions": "Cook beef and garlic, add spinach and cream, simmer and serve with parmesan."
            },
            "Beef Ossobuco": {
                "dish": "Beef Ossobuco",
                "time": 120,
                "ingredients": ["2 beef shanks", "2 carrots (chopped)", "2 celery stalks (chopped)", "1 onion (chopped)", "1 1/2 cups tomato sauce"],
                "instructions": "Braise beef shanks with vegetables and tomato sauce in a slow-cooked oven until tender."
            },
            "Beef Risotto": {
                "dish": "Beef Risotto",
                "time": 50,
                "ingredients": ["1 lb beef", "1 cup arborio rice", "3 cups beef broth", "1/2 cup grated parmesan", "1/4 cup red wine"],
                "instructions": "Cook beef, prepare risotto with rice, broth, and red wine, stir in parmesan and beef."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_vegan_recipe(name):
        recipes = {
            "Vegan Spaghetti": {
                "dish": "Vegan Spaghetti",
                "time": 30,
                "ingredients": ["12 oz spaghetti", "2 cups tomato sauce", "2 cloves garlic (minced)", "1/4 cup fresh basil (chopped)", "2 tbsp olive oil"],
                "instructions": "Cook spaghetti, sauté garlic in olive oil, add tomato sauce and basil, mix with pasta."
            },
            "Vegan Lasagna": {
                "dish": "Vegan Lasagna",
                "time": 70,
                "ingredients": ["12 lasagna noodles", "2 cups vegan ricotta", "3 cups tomato sauce", "2 cups fresh spinach", "1 1/2 cups vegan cheese"],
                "instructions": "Layer noodles, ricotta, spinach, and tomato sauce, top with vegan cheese, bake at 375°F for 40 minutes."
            },
            "Vegan Risotto": {
                "dish": "Vegan Risotto",
                "time": 50,
                "ingredients": ["1 cup arborio rice", "3 cups vegetable broth", "1 onion (chopped)", "2 cloves garlic (minced)", "1/4 cup vegan parmesan"],
                "instructions": "Simmer arborio rice in vegetable broth and garlic, stir in vegan parmesan."
            },
            "Vegan Pizza": {
                "dish": "Vegan Pizza",
                "time": 25,
                "ingredients": ["1 pizza dough", "1 cup tomato sauce", "1 1/2 cups vegan cheese", "1 cup assorted vegetables (bell peppers, mushrooms, onions)"],
                "instructions": "Top dough with sauce, vegan cheese, and vegetables, bake at 450°F for 12-15 minutes."
            },
            "Vegan Gnocchi": {
                "dish": "Vegan Gnocchi",
                "time": 40,
                "ingredients": ["1 lb gnocchi", "2 cups tomato sauce", "1/4 cup fresh basil", "2 tbsp olive oil", "1/4 cup vegan parmesan"],
                "instructions": "Cook gnocchi, prepare tomato sauce with basil, mix and top with olive oil and vegan parmesan."
            },
            "Vegan Minestrone": {
                "dish": "Vegan Minestrone",
                "time": 45,
                "ingredients": ["2 cups mixed vegetables (carrots, celery, zucchini)", "1 cup beans", "4 cups tomato broth", "1 cup pasta", "1 tbsp mixed herbs"],
                "instructions": "Simmer vegetables, beans, and pasta in tomato broth with herbs until vegetables are tender."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_fish_recipe(name):
        recipes = {
            "Shrimp Scampi": {
                "dish": "Shrimp Scampi",
                "time": 20,
                "ingredients": ["1 lb shrimp", "4 cloves garlic (minced)", "1/2 cup butter", "1 lemon (juiced)", "2 tbsp parsley (chopped)"],
                "instructions": "Sauté shrimp with garlic and butter, finish with lemon juice and parsley."
            },
            "Linguine with Clams": {
                "dish": "Linguine with Clams",
                "time": 30,
                "ingredients": ["12 oz linguine", "2 cups clams", "3 cloves garlic (minced)", "1/2 cup white wine", "2 tbsp parsley (chopped)"],
                "instructions": "Cook linguine, prepare clam sauce by sautéing garlic, white wine, and clams, serve over pasta."
            },
            "Cioppino": {
                "dish": "Cioppino",
                "time": 45,
                "ingredients": ["1 lb mixed seafood", "4 cups tomato broth", "2 cloves garlic (minced)", "1 onion (chopped)", "1/2 cup white wine"],
                "instructions": "Simmer mixed seafood in tomato broth with garlic, onions, and white wine."
            },
            "Grilled Salmon": {
                "dish": "Grilled Salmon",
                "time": 25,
                "ingredients": ["4 salmon fillets", "1 lemon (sliced)", "2 tbsp olive oil", "2 cloves garlic (minced)", "2 tbsp herbs (rosemary, thyme)"],
                "instructions": "Marinate salmon in olive oil, garlic, and herbs, then grill."
            },
            "Tuna Carpaccio": {
                "dish": "Tuna Carpaccio",
                "time": 15,
                "ingredients": ["1/2 lb tuna", "2 tbsp olive oil", "1 lemon (juiced)", "1 tbsp capers", "1/4 cup arugula"],
                "instructions": "Thinly slice tuna, drizzle with olive oil, lemon juice, capers, and garnish with arugula."
            },
            "Fish Risotto": {
                "dish": "Fish Risotto",
                "time": 50,
                "ingredients": ["1 lb white fish", "1 cup arborio rice", "4 cups fish broth", "1/4 cup white wine", "1/2 cup parmesan"],
                "instructions": "Cook fish, prepare risotto by simmering rice in fish broth and white wine, stir in parmesan and fish."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_lamb_recipe(name):
        recipes = {
            "Lamb Ragu": {
                "dish": "Lamb Ragu",
                "time": 90,
                "ingredients": ["1 lb lamb", "2 cups tomato sauce", "2 cloves garlic (minced)", "1 onion (chopped)", "1/2 cup red wine"],
                "instructions": "Simmer lamb with tomato sauce, garlic, onions, and red wine until tender."
            },
            "Lamb Chops": {
                "dish": "Lamb Chops",
                "time": 25,
                "ingredients": ["4 lamb chops", "2 cloves garlic (minced)", "2 tbsp rosemary (chopped)", "2 tbsp olive oil", "1 lemon (juiced)"],
                "instructions": "Marinate lamb chops with garlic, rosemary, olive oil, and lemon, then grill."
            },
            "Lamb Risotto": {
                "dish": "Lamb Risotto",
                "time": 50,
                "ingredients": ["1 lb lamb", "1 cup arborio rice", "3 cups lamb broth", "1/4 cup white wine", "1/2 cup parmesan"],
                "instructions": "Cook lamb, prepare risotto with rice, lamb broth, and white wine, stir in parmesan."
            },
            "Lamb Osso Buco": {
                "dish": "Lamb Osso Buco",
                "time": 120,
                "ingredients": ["2 lamb shanks", "2 carrots (chopped)", "2 celery stalks (chopped)", "1 onion (chopped)", "2 cups tomato sauce"],
                "instructions": "Braise lamb shanks with vegetables and tomato sauce in a slow-cooked oven until tender."
            },
            "Lamb Meatballs": {
                "dish": "Lamb Meatballs",
                "time": 40,
                "ingredients": ["1 lb ground lamb", "1/2 cup breadcrumbs", "1/4 cup parmesan", "2 cups tomato sauce", "2 tbsp herbs"],
                "instructions": "Form lamb into meatballs, bake, then simmer in tomato sauce."
            },
            "Lamb Lasagna": {
                "dish": "Lamb Lasagna",
                "time": 90,
                "ingredients": ["1 lb ground lamb", "12 lasagna noodles", "1 1/2 cups ricotta", "3 cups tomato sauce", "2 cups mozzarella"],
                "instructions": "Layer lamb, noodles, ricotta, and tomato sauce in a baking dish, top with mozzarella, and bake."
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
    
api.add_resource(SaveRecipe, '/save_recipe')

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

api.add_resource(VeganSpaghetti, '/italian_recipe/VeganSpaghetti')
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