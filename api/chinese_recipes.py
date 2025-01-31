from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource # used for REST API building
from __init__ import db
from model.chinese_recipes import Recipe

chinese_recipe_api = Blueprint('chinese_recipe_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/
api = Api(chinese_recipe_api)

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

class chinese_recipe_API:
    @staticmethod
    def get_chicken_recipe(name):
        recipes = {
            "Kung Pao Chicken": {
                "dish": "Kung Pao Chicken",
                "time": 30,
                "ingredients": "Chicken breast (500g), Dried red chilies (10-12)  Peanuts (50g),Soy sauce (2 tbsp),Rice vinegar (1 tbsp),Sugar (1 tsp), Cornstarch (1 tsp), Garlic (3 cloves) Ginger (1-inch piece),Spring onions (2 stalks)",
                "instructions":
                "Cut chicken into small cubes and marinate with soy sauce and cornstarch for 10 minutes. Heat oil in a wok, fry dried chilies and peanuts until fragrant. Add garlic and ginger, stir-fry for 30 seconds. Add chicken and stir-fry until golden brown. Mix soy sauce, rice vinegar, sugar, and stir into the wok. Add spring onions and stir-fry for 2 more minutes before serving.",
            },
             "Orange Chicken": {
                "dish": "Orange Chicken",
                "time": 40,
                "ingredients": "Chicken breast (500g), Orange juice (1/2 cup), Soy sauce (2 tbsp), Vinegar (1 tbsp), Brown sugar (1/4 cup), Cornstarch (1 tbsp), Garlic (3 cloves), Ginger (1-inch piece), Orange zest (1 tsp), Vegetable oil (2 tbsp)",
                "instructions": "Fry chicken until crispy. Combine orange juice, soy sauce, vinegar, sugar, and cornstarch in a bowl. Stir-fry garlic and ginger, add sauce mixture, and cook until thickened. Coat chicken in the sauce. Serve with steamed rice.",
            },
            "Lemon Chicken": {
                "dish": "Lemon Chicken",
                "time": 35,
                "ingredients": "Chicken breast (500g), Lemon juice (1/4 cup), Soy sauce (2 tbsp), Rice vinegar (1 tbsp), Cornstarch (1 tsp), Garlic (2 cloves), Ginger (1-inch piece), Vegetable oil (2 tbsp)",
                "instructions": "Fry chicken until crispy. Combine lemon juice, soy sauce, rice vinegar, and cornstarch. Stir-fry garlic and ginger, add sauce, and cook until thickened. Coat chicken in the sauce. Serve with rice.",
            },
            "Crispy Sweet and Sour Chicken": {
                "dish": "Crispy Sweet and Sour Chicken",
                "time": 45,
                "ingredients": "Chicken breast (500g), Pineapple chunks (1 cup), Red bell pepper (1), Onion (1), Soy sauce (2 tbsp), Rice vinegar (1 tbsp), Brown sugar (2 tbsp), Ketchup (1/4 cup), Cornstarch (1 tbsp), Vegetable oil (for frying)",
                "instructions": "Coat chicken in cornstarch and fry until crispy. Stir-fry vegetables in a pan. Combine soy sauce, vinegar, brown sugar, ketchup, and cornstarch to make the sauce. Pour sauce over vegetables, add pineapple, then toss in fried chicken. Serve hot.",
            },
            "Chicken with Cashews": {
                "dish": "Chicken with Cashews",
                "time": 30,
                "ingredients": "Chicken breast (500g), Cashew nuts (50g), Soy sauce (2 tbsp), Oyster sauce (1 tbsp), Rice vinegar (1 tbsp), Garlic (2 cloves), Ginger (1-inch piece), Green onions (2 stalks), Vegetable oil (2 tbsp)",
                "instructions": "Marinate chicken in soy sauce, oyster sauce, and rice vinegar. Stir-fry garlic and ginger, then add chicken and cook until browned. Add cashews and stir-fry for 1 more minute. Garnish with spring onions. Serve with steamed rice.",
            },
            "Szechuan Chicken": {
                "dish": "Szechuan Chicken",
                "time": 35,
                "ingredients": "Chicken breast (500g), Szechuan peppercorns (1 tsp), Dried red chilies (6-8), Soy sauce (2 tbsp), Rice vinegar (1 tbsp), Sugar (1 tsp), Garlic (3 cloves), Ginger (1-inch piece), Vegetable oil (2 tbsp)",
                "instructions": "Marinate chicken with soy sauce, vinegar, and sugar. Heat oil in a wok, fry Szechuan peppercorns and chilies until fragrant. Add garlic and ginger, then stir-fry chicken. Cook until the sauce thickens. Serve with rice.",
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_beef_recipe(name):
        recipes = {
             "Beef with Broccoli": {
                "dish": "Beef with Broccoli",
                "time": 30,
                "ingredients": "Beef (300g, sliced thinly against the grain), Broccoli (200g, cut into florets), Soy sauce (2 tbsp), Oyster sauce (2 tbsp), Hoisin sauce (1 tbsp), Cornstarch (1 tsp), Garlic (3 cloves, minced), Ginger (1-inch piece, minced), Vegetable oil (2 tbsp), Water (1/2 cup)",
                "instructions": "Marinate beef in 1 tbsp soy sauce, 1 tbsp oyster sauce, cornstarch, and 1 tsp water for 10 minutes. Heat oil in a wok, stir-fry garlic and ginger for 30 seconds. Add beef and cook until browned. Add broccoli and stir-fry for 2 minutes. Mix remaining soy sauce, oyster sauce, hoisin sauce, and water. Pour over beef and broccoli, cook for another 2 minutes until the sauce thickens. Serve with rice.",
            },
            "Mongolian Beef": {
                "dish": "Mongolian Beef",
                "time": 30,
                "ingredients": "Beef (400g, sliced thinly), Green onions (4, chopped), Soy sauce (1/4 cup), Brown sugar (1/4 cup), Cornstarch (2 tbsp), Vegetable oil (3 tbsp), Garlic (2 cloves, minced), Ginger (1-inch piece, minced), Water (1/2 cup)",
                "instructions": "Coat beef in cornstarch and let sit for 10 minutes. Heat oil in a wok, stir-fry beef until golden brown. Remove beef and set aside. In the same pan, add garlic and ginger, stir-fry for 30 seconds. Add soy sauce, brown sugar, and water, simmer for 2 minutes. Return beef to the pan, toss with sauce, and cook for another 2-3 minutes. Garnish with green onions. Serve with steamed rice.",
            },
            "Beef with Black Bean Sauce": {
                "dish": "Beef with Black Bean Sauce",
                "time": 30,
                "ingredients": "Beef (300g, sliced thinly), Black bean paste (2 tbsp), Soy sauce (1 tbsp), Oyster sauce (2 tbsp), Bell peppers (2, sliced), Onion (1, sliced), Garlic (3 cloves, minced), Ginger (1-inch piece, minced), Vegetable oil (2 tbsp), Cornstarch (1 tsp), Water (1/4 cup)",
                "instructions": "Marinate beef in soy sauce, oyster sauce, cornstarch, and 1 tbsp water for 10 minutes. Heat oil in a wok, stir-fry garlic and ginger for 30 seconds. Add beef and cook until browned. Add bell peppers and onion, stir-fry for another 3 minutes. Stir in black bean paste and water, cook for another 2 minutes. Serve with rice.",
            },
            "Beef and Peppers Stir Fry": {
                "dish": "Beef and Peppers Stir Fry",
                "time": 20,
                "ingredients": "Beef (300g, thinly sliced), Bell peppers (2, sliced), Onion (1, sliced), Soy sauce (2 tbsp), Rice vinegar (1 tbsp), Sugar (1 tsp), Cornstarch (1 tsp), Garlic (2 cloves, minced), Ginger (1-inch piece, minced), Vegetable oil (2 tbsp), Rice (for serving)",
                "instructions": "Marinate beef in soy sauce, rice vinegar, sugar, and cornstarch for 10 minutes. Heat oil in a wok, stir-fry garlic and ginger for 30 seconds. Add beef and cook until browned. Add bell peppers and onion, stir-fry for 3 minutes. Pour in a bit of water to deglaze the wok, stir-fry for another 2 minutes. Serve with steamed rice.",
            },
            "Chinese Spicy Beef": {
                "dish": "Chinese Spicy Beef",
                "time": 25,
                "ingredients": "Beef (300g, sliced thinly), Dried red chilies (6-8), Soy sauce (1 tbsp), Rice vinegar (1 tbsp), Garlic (3 cloves, minced), Ginger (1-inch piece, minced), Szechuan peppercorns (1 tsp), Chili paste (1 tsp), Vegetable oil (2 tbsp), Cornstarch (1 tsp)",
                "instructions": "Marinate beef with soy sauce, rice vinegar, and cornstarch for 10 minutes. Heat oil in a wok, stir-fry dried chilies and Szechuan peppercorns until fragrant. Add garlic and ginger, stir-fry for another 30 seconds. Add beef and cook until browned. Stir in chili paste and cook for 1 more minute. Serve with rice or noodles.",
            },  
            "Beef with Mushrooms": {
                "dish": "Beef with Mushrooms",
                "time": 30,
                "ingredients": "Beef (300g, sliced thinly), Mushrooms (200g, sliced), Soy sauce (2 tbsp), Oyster sauce (1 tbsp), Garlic (3 cloves, minced), Ginger (1-inch piece, minced), Green onions (2 stalks, chopped), Vegetable oil (2 tbsp)",
                "instructions": "Stir-fry beef until browned. Add garlic and ginger, then mushrooms. Stir-fry until mushrooms are soft. Add soy sauce and oyster sauce, cook until thickened. Garnish with green onions.",
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_vegan_recipe(name):
        recipes = {
            "Mapo Tofu": {
                "dish": "Mapo Tofu",
                "time": 30,
                "ingredients": "Tofu (300g, firm), Doubanjiang (2 tbsp), Soy sauce (2 tbsp), Rice vinegar (1 tbsp), Garlic (3 cloves), Ginger (1-inch piece), Sichuan peppercorns (1 tsp), Cornstarch (1 tsp), Green onions (2 stalks)",
                "instructions": "Stir-fry garlic, ginger, and Sichuan peppercorns. Add tofu and cook until golden. Stir in doubanjiang, soy sauce, and vinegar. Add cornstarch mixture to thicken.",
            },
            "Vegan Kung Pao Tofu": {
                "dish": "Vegan Kung Pao Tofu",
                "time": 30,
                "ingredients": "Tofu (300g), Soy sauce (2 tbsp), Rice vinegar (1 tbsp), Cornstarch (1 tsp), Peanuts (50g), Dried chilies (6-8), Garlic (3 cloves), Ginger (1-inch piece), Spring onions (2 stalks)",
                "instructions": "Marinate tofu in soy sauce, vinegar, and cornstarch. Stir-fry chilies, garlic, and ginger. Add tofu and cook until golden. Add peanuts and spring onions, stir-fry for 2 more minutes.",
            },
            "Vegan Sweet and Sour Tofu": {
                "dish": "Vegan Sweet and Sour Tofu",
                "time": 35,
                "ingredients": "Tofu (300g), Pineapple chunks (1 cup), Red bell pepper (1), Onion (1), Soy sauce (2 tbsp), Rice vinegar (1 tbsp), Brown sugar (2 tbsp), Cornstarch (1 tbsp), Vegetable oil (for frying)",
                "instructions": "Fry tofu until crispy. Stir-fry vegetables, add pineapple, and make a sweet-and-sour sauce with soy sauce, vinegar, sugar, and cornstarch. Coat tofu in sauce.",
            },
            "Vegan Hot and Sour Soup": {
                "dish": "Vegan Hot and Sour Soup",
                "time": 30,
                "ingredients": "Tofu (200g), Mushrooms (100g), Bamboo shoots (50g), Soy sauce (2 tbsp), Rice vinegar (2 tbsp), Chili paste (1 tsp), Cornstarch (1 tsp), Vegetable broth (500ml), Sichuan peppercorns (1 tsp)",
                "instructions": "Boil vegetable broth with soy sauce, vinegar, chili paste, and peppercorns. Add mushrooms, bamboo shoots, tofu, and simmer. Thicken with cornstarch.",
            },
            "Vegan Fried Rice": {
                "dish": "Vegan Fried Rice",
                "time": 20,
                "ingredients": "Cooked rice (2 cups), Soy sauce (2 tbsp), Peas (1/2 cup), Carrots (1/2 cup, diced), Onion (1), Garlic (2 cloves), Green onions (2 stalks), Vegetable oil (2 tbsp)",
                "instructions": "Stir-fry onion, garlic, peas, carrots, and rice. Add soy sauce and stir-fry until crispy. Garnish with spring onions.",
            },
            "Vegan Stir Fry with Tofu": {
                "dish": "Vegan Stir Fry with Tofu",
                "time": 25,
                "ingredients": "Tofu (300g, cubed), Soy sauce (2 tbsp), Bell peppers (2), Onion (1), Garlic (3 cloves), Ginger (1-inch piece), Vegetable oil (2 tbsp)",
                "instructions": "Stir-fry tofu until crispy, then set aside. Stir-fry vegetables, add tofu back in, and stir-fry with soy sauce.",
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_fish_recipe(name):
        recipes = {
            "Fish in Black Bean Sauce": {
                "dish": "Fish in Black Bean Sauce",
                "time": 30,
                "ingredients": "White fish fillets (400g), Black bean paste (2 tbsp), Soy sauce (1 tbsp), Oyster sauce (1 tbsp), Garlic (3 cloves), Ginger (1-inch piece), Spring onions (2 stalks), Cornstarch (1 tsp)",
                "instructions": "Marinate fish in soy sauce and cornstarch. Stir-fry garlic and ginger, add fish and cook until golden. Stir in black bean paste and cook until thickened.",
            },
            "Steamed Fish with Ginger and Soy Sauce": {
                "dish": "Steamed Fish with Ginger and Soy Sauce",
                "time": 25,
                "ingredients": "Whole fish (500g), Soy sauce (3 tbsp), Ginger (1-inch piece), Spring onions (2 stalks), Rice wine (2 tbsp), Sesame oil (1 tsp)",
                "instructions": "Place fish on a plate, drizzle with soy sauce and rice wine. Steam for 15-20 minutes. Garnish with ginger, spring onions, and sesame oil.",
            },
            "Fish Tofu Soup": {
                "dish": "Fish Tofu Soup",
                "time": 30,
                "ingredients": "White fish fillets (300g), Tofu (200g), Ginger (1-inch piece), Garlic (2 cloves), Spring onions (2 stalks), Soy sauce (2 tbsp), Vegetable broth (500ml)",
                "instructions": "Simmer vegetable broth with ginger, garlic, and soy sauce. Add fish and tofu, simmer until cooked. Garnish with spring onions.",
            },
            "Crispy Fish Fillets": {
                "dish": "Crispy Fish Fillets",
                "time": 25,
                "ingredients": "Fish fillets (400g), Cornstarch (1/2 cup), Soy sauce (1 tbsp), Garlic (2 cloves), Ginger (1-inch piece), Green onions (2 stalks)",
                "instructions": "Coat fish fillets in cornstarch and fry until crispy. Stir-fry garlic and ginger, add soy sauce and green onions, and pour over crispy fish.",
            },
            "Fish with Soy and Garlic Sauce": {
                "dish": "Fish with Soy and Garlic Sauce",
                "time": 30,
                "ingredients": "Fish fillets (300g), Soy sauce (3 tbsp), Garlic (4 cloves), Ginger (1-inch piece), Green onions (2 stalks), Vegetable oil (2 tbsp)",
                "instructions": "Fry fish fillets until golden. Stir-fry garlic and ginger, add soy sauce, and pour over fish. Garnish with spring onions.",
            },
            "Fish and Eggplant Stir Fry": {
                "dish": "Fish and Eggplant Stir Fry",
                "time": 35,
                "ingredients": "Fish fillets (300g), Eggplant (2), Soy sauce (2 tbsp), Oyster sauce (1 tbsp), Garlic (3 cloves), Ginger (1-inch piece), Cornstarch (1 tsp)",
                "instructions": "Stir-fry fish and eggplant. Add soy sauce, oyster sauce, and garlic. Cook until eggplant is tender.",
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_lamb_recipe(name):
        recipes = {
            "Braised Lamb with Soy Sauce": {
                "dish": "Braised Lamb with Soy Sauce",
                "time": 60,
                "ingredients": "Lamb (500g), Soy sauce (3 tbsp), Rice wine (2 tbsp), Garlic (3 cloves), Ginger (1-inch piece), Star anise (1), Spring onions (2 stalks), Brown sugar (1 tbsp)",
                "instructions": "Brown lamb and braise with soy sauce, rice wine, sugar, and ginger for 60 minutes.",
            },
            "Lamb Stir Fry with Peppers": {
                "dish": "Lamb Stir Fry with Peppers",
                "time": 30,
                "ingredients": "Lamb (300g), Bell peppers (2), Soy sauce (2 tbsp), Hoisin sauce (1 tbsp), Garlic (3 cloves), Ginger (1-inch piece), Spring onions (2 stalks)",
                "instructions": "Stir-fry lamb until browned. Add garlic, ginger, and bell peppers. Stir in soy sauce and hoisin sauce, cook for 2 more minutes.",
            },
            "Lamb with Black Bean Sauce": {
                "dish": "Lamb with Black Bean Sauce",
                "time": 40,
                "ingredients": "Lamb (300g), Black bean paste (2 tbsp), Soy sauce (1 tbsp), Oyster sauce (2 tbsp), Bell peppers (2), Garlic (3 cloves), Ginger (1-inch piece), Cornstarch (1 tsp)",
                "instructions": "Stir-fry lamb, add garlic, ginger, and black bean paste. Stir in soy sauce, oyster sauce, and cook until thickened.",
            },
            "Szechuan Lamb": {
                "dish": "Szechuan Lamb",
                "time": 35,
                "ingredients": "Lamb (300g), Soy sauce (2 tbsp), Szechuan peppercorns (1 tsp), Garlic (3 cloves), Ginger (1-inch piece), Dried chilies (6-8)",
                "instructions": "Stir-fry lamb with garlic, ginger, and Szechuan peppercorns. Add soy sauce and cook until lamb is cooked through.",
            },
            "Lamb with Vegetables Stir Fry": {
                "dish": "Lamb with Vegetables Stir Fry",
                "time": 30,
                "ingredients": "Lamb (300g), Zucchini (1), Bell peppers (2), Soy sauce (2 tbsp), Cornstarch (1 tsp), Garlic (3 cloves), Ginger (1-inch piece), Vegetable oil (2 tbsp)",
                "instructions": "Stir-fry lamb, garlic, and ginger. Add vegetables, soy sauce, and cornstarch, cook until thickened.",
            },
            "Lamb Curry": {
                "dish": "Lamb Curry",
                "time": 50,
                "ingredients": "Lamb (500g), Curry powder (1 tbsp), Garlic (3 cloves), Ginger (1-inch piece), Onion (1), Tomatoes (2), Coconut milk (1 cup), Soy sauce (1 tbsp)",
                "instructions": "Brown lamb and cook with garlic, ginger, onion, and curry powder. Add tomatoes and coconut milk, simmer for 40 minutes.",
            }
        }
        return recipes.get(name)
      
      

    class _KungPaoChicken(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_chicken_recipe("Kung Pao Chicken")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _OrangeChicken(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_chicken_recipe("Orange Chicken")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LemonChicken(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_chicken_recipe("Lemon Chicken")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _CrispySweetAndSourChicken(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_chicken_recipe("Crispy Sweet and Sour Chicken")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChickenWithCashews(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_chicken_recipe("Chicken with Cashews")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _SzechuanChicken(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_chicken_recipe("Szechuan Chicken")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefWithBroccoli(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_beef_recipe("Beef with Broccoli")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _MongolianBeef(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_beef_recipe("Mongolian Beef")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefWithBlackBeanSauce(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_beef_recipe("Beef with Black Bean Sauce")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BeefAndPeppersStirFry(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_beef_recipe("Beef and Peppers Stir Fry")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _ChineseSpicyBeef(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_beef_recipe("Chinese Spicy Beef")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _MapoTofu(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_vegan_recipe("Mapo Tofu")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganKungPaoTofu(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_vegan_recipe("Vegan Kung Pao Tofu")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganSweetAndSourTofu(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_vegan_recipe("Vegan Sweet and Sour Tofu")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganHotAndSourSoup(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_vegan_recipe("Vegan Hot and Sour Soup")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganFriedRice(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_vegan_recipe("Vegan Fried Rice")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _VeganStirFryWithTofu(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_vegan_recipe("Vegan Stir Fry with Tofu")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _FishInBlackBeanSauce(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_fish_recipe("Fish in Black Bean Sauce")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _SteamedFishWithGingerAndSoySauce(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_fish_recipe("Steamed Fish with Ginger and Soy Sauce")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _FishTofuSoup(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_fish_recipe("Fish Tofu Soup")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _CrispyFishFillets(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_fish_recipe("Crispy Fish Fillets")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _FishWithSoyAndGarlicSauce(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_fish_recipe("Fish with Soy and Garlic Sauce")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _FishAndEggplantStirFry(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_fish_recipe("Fish and Eggplant Stir Fry")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _BraisedLambWithSoySauce(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_lamb_recipe("Braised Lamb with Soy Sauce")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambStirFryWithPeppers(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_lamb_recipe("Lamb Stir Fry with Peppers")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambWithBlackBeanSauce(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_lamb_recipe("Lamb with Black Bean Sauce")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _SzechuanLamb(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_lamb_recipe("Szechuan Lamb")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambWithVegetablesStirFry(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_lamb_recipe("Lamb with Vegetables Stir Fry")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404

    class _LambCurry(Resource):
        def get(self):
            recipe = chinese_recipe_API.get_lamb_recipe("Lamb Curry")
            if recipe:
                return jsonify(recipe)
            return {"Data not found"}, 404
        
api.add_resource(SaveRecipe, '/save_recipe')
api.add_resource(UpdateRecipe, '/api/chinese_recipe/edit_recipe/<int:recipe_id>')

        
api.add_resource(chinese_recipe_API._KungPaoChicken, '/chinese_recipe/KungPaoChicken')
api.add_resource(chinese_recipe_API._OrangeChicken, '/chinese_recipe/OrangeChicken')
api.add_resource(chinese_recipe_API._LemonChicken, '/chinese_recipe/LemonChicken')
api.add_resource(chinese_recipe_API._CrispySweetAndSourChicken, '/chinese_recipe/CrispySweetAndSourChicken')
api.add_resource(chinese_recipe_API._ChickenWithCashews, '/chinese_recipe/ChickenWithCashews')
api.add_resource(chinese_recipe_API._SzechuanChicken, '/chinese_recipe/SzechuanChicken')

api.add_resource(chinese_recipe_API._BeefWithBroccoli, '/chinese_recipe/BeefWithBroccoli')
api.add_resource(chinese_recipe_API._MongolianBeef, '/chinese_recipe/MongolianBeef')
api.add_resource(chinese_recipe_API._BeefWithBlackBeanSauce, '/chinese_recipe/BeefWithBlackBeanSauce')
api.add_resource(chinese_recipe_API._BeefAndPeppersStirFry, '/chinese_recipe/BeefAndPeppersStirFry')
api.add_resource(chinese_recipe_API._ChineseSpicyBeef, '/chinese_recipe/ChineseSpicyBeef')

api.add_resource(chinese_recipe_API._MapoTofu, '/chinese_recipe/MapoTofu')
api.add_resource(chinese_recipe_API._VeganKungPaoTofu, '/chinese_recipe/VeganKungPaoTofu')
api.add_resource(chinese_recipe_API._VeganSweetAndSourTofu, '/chinese_recipe/VeganSweetAndSourTofu')
api.add_resource(chinese_recipe_API._VeganHotAndSourSoup, '/chinese_recipe/VeganHotAndSourSoup')
api.add_resource(chinese_recipe_API._VeganFriedRice, '/chinese_recipe/VeganFriedRice')
api.add_resource(chinese_recipe_API._VeganStirFryWithTofu, '/chinese_recipe/VeganStirFryWithTofu')

api.add_resource(chinese_recipe_API._FishInBlackBeanSauce, '/chinese_recipe/FishInBlackBeanSauce')
api.add_resource(chinese_recipe_API._SteamedFishWithGingerAndSoySauce, '/chinese_recipe/SteamedFishWithGingerAndSoySauce')
api.add_resource(chinese_recipe_API._FishTofuSoup, '/chinese_recipe/FishTofuSoup')
api.add_resource(chinese_recipe_API._CrispyFishFillets, '/chinese_recipe/CrispyFishFillets')
api.add_resource(chinese_recipe_API._FishWithSoyAndGarlicSauce, '/chinese_recipe/FishWithSoyAndGarlicSauce')
api.add_resource(chinese_recipe_API._FishAndEggplantStirFry, '/chinese_recipe/FishAndEggplantStirFry')

api.add_resource(chinese_recipe_API._BraisedLambWithSoySauce, '/chinese_recipe/BraisedLambWithSoySauce')
api.add_resource(chinese_recipe_API._LambStirFryWithPeppers, '/chinese_recipe/LambStirFryWithPeppers')
api.add_resource(chinese_recipe_API._LambWithBlackBeanSauce, '/chinese_recipe/LambWithBlackBeanSauce')
api.add_resource(chinese_recipe_API._SzechuanLamb, '/chinese_recipe/SzechuanLamb')
api.add_resource(chinese_recipe_API._LambWithVegetablesStirFry, '/chinese_recipe/LambWithVegetablesStirFry')
api.add_resource(chinese_recipe_API._LambCurry, '/chinese_recipe/LambCurry')

# Instantiate the StudentAPI to register the endpoints
chinese_recipe_api_instance = chinese_recipe_API()


    