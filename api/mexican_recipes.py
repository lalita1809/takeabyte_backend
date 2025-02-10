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


class mexican_recipe_API:
    @staticmethod
    def get_chicken_recipe(name):
        recipes = {
            "Chicken Enchiladas": {
                "dish": "Chicken Enchiladas",
                "time": 60,
                "ingredients": ["500g chicken breast, shredded", "8 corn tortillas", "1 cup shredded cheese", "1 cup salsa", "1 tsp cumin", "1 tsp chili powder", "1/2 tsp garlic powder", "1/2 tsp onion powder", "Salt and pepper to taste"],
                "instructions": "Preheat oven to 350°F. Shred cooked chicken and season with cumin, chili powder, garlic powder, onion powder, salt, and pepper. Roll chicken in tortillas, place in a baking dish, top with salsa and cheese, and bake for 20-25 minutes."
            },
            "Chicken Tacos": {
                "dish": "Chicken Tacos",
                "time": 30,
                "ingredients": ["500g cooked chicken, shredded", "8 taco shells", "1 cup shredded lettuce", "1/2 cup shredded cheese", "1/4 cup sour cream", "1 tbsp taco seasoning", "1 tbsp olive oil"],
                "instructions": "In a skillet, heat olive oil and sauté shredded chicken with taco seasoning for 5 minutes. Fill taco shells with seasoned chicken, lettuce, cheese, and top with sour cream."
            },
            "Chicken Fajitas": {
                "dish": "Chicken Fajitas",
                "time": 25,
                "ingredients": ["500g chicken breast, sliced", "1 bell pepper, sliced", "1 onion, sliced", "2 tbsp fajita seasoning", "1 tbsp olive oil", "Tortillas for serving"],
                "instructions": "Heat oil in a skillet and sauté chicken, bell peppers, and onions with fajita seasoning for 7-10 minutes. Serve with warm tortillas."
            },
            "Pollo Asado": {
                "dish": "Pollo Asado",
                "time": 50,
                "ingredients": ["1 whole chicken, cut into parts", "Juice of 2 limes", "4 cloves garlic, minced", "2 tbsp olive oil", "1 tbsp chili powder", "1 tbsp paprika", "1 tsp cumin", "Salt and pepper to taste"],
                "instructions": "Marinate chicken in lime juice, garlic, olive oil, chili powder, paprika, cumin, salt, and pepper for at least 30 minutes. Grill chicken on medium-high heat for 20-30 minutes until fully cooked."
            },
            "Chicken Quesadillas": {
                "dish": "Chicken Quesadillas",
                "time": 20,
                "ingredients": ["2 flour tortillas", "1 cup cooked chicken, shredded", "1 cup shredded cheese", "1/4 cup salsa", "1 tbsp butter"],
                "instructions": "Place one tortilla on a skillet, add shredded chicken, cheese, and salsa, and top with another tortilla. Grill with butter on both sides until golden brown and cheese is melted."
            },
            "Chicken Tamales": {
                "dish": "Chicken Tamales",
                "time": 120,
                "ingredients": ["2 cups masa harina", "1 cup chicken broth", "1/2 cup vegetable oil", "1 cup cooked chicken, shredded", "1/2 cup salsa", "Corn husks for wrapping"],
                "instructions": "Soak corn husks in warm water for 30 minutes. Mix masa harina, chicken broth, and vegetable oil to form the masa dough. Spread masa on the corn husks, add shredded chicken and salsa, then wrap and steam for 1-1.5 hours."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_beef_recipe(name):
        recipes = {
            "Beef Enchiladas": {
                "dish": "Beef Enchiladas",
                "time": 60,
                "ingredients": ["500g ground beef", "8 corn tortillas", "1 cup shredded cheese", "1 cup salsa", "1 tsp cumin", "1/2 tsp garlic powder", "Salt and pepper to taste"],
                "instructions": "Preheat oven to 350°F. Brown ground beef in a skillet, then add cumin, garlic powder, salt, and pepper. Roll beef in tortillas, place in a baking dish, top with salsa and cheese, and bake for 20-25 minutes."
            },
            "Beef Tacos": {
                "dish": "Beef Tacos",
                "time": 30,
                "ingredients": ["500g ground beef", "8 taco shells", "1 cup shredded lettuce", "1/2 cup shredded cheese", "1/4 cup sour cream", "1 tbsp taco seasoning", "1 tbsp olive oil"],
                "instructions": "Heat olive oil in a skillet and sauté ground beef with taco seasoning for 7-10 minutes. Fill taco shells with beef, lettuce, cheese, and top with sour cream."
            },
            "Beef Fajitas": {
                "dish": "Beef Fajitas",
                "time": 25,
                "ingredients": ["500g beef, sliced", "1 bell pepper, sliced", "1 onion, sliced", "2 tbsp fajita seasoning", "1 tbsp olive oil", "Tortillas for serving"],
                "instructions": "Heat oil in a skillet and sauté beef, bell peppers, and onions with fajita seasoning for 7-10 minutes. Serve with warm tortillas."
            },
            "Beef Burritos": {
                "dish": "Beef Burritos",
                "time": 30,
                "ingredients": ["500g ground beef", "4 large flour tortillas", "1 cup rice, cooked", "1 cup beans", "1 cup shredded cheese", "1/4 cup salsa"],
                "instructions": "Brown ground beef in a skillet. Warm tortillas, then fill with beef, rice, beans, cheese, and salsa. Roll up the tortillas and serve."
            },
            "Beef Tostadas": {
                "dish": "Beef Tostadas",
                "time": 20,
                "ingredients": ["500g ground beef", "4 tostada shells", "1 cup shredded lettuce", "1/2 cup shredded cheese", "1/4 cup sour cream"],
                "instructions": "Brown ground beef in a skillet and season to taste. Top tostada shells with beef, lettuce, cheese, and sour cream."
            },
            "Carne Asada": {
                "dish": "Carne Asada",
                "time": 40,
                "ingredients": ["500g flank steak", "Juice of 2 limes", "4 cloves garlic, minced", "2 tbsp olive oil", "1 tbsp chili powder", "1 tsp cumin", "Salt and pepper to taste"],
                "instructions": "Marinate flank steak in lime juice, garlic, olive oil, chili powder, cumin, salt, and pepper for at least 30 minutes. Grill steak on medium-high heat for 5-7 minutes per side, then slice thinly against the grain."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_vegan_recipe(name):
        recipes = {
            "Vegan Tacos": {
                "dish": "Vegan Tacos",
                "time": 20,
                "ingredients": ["8 taco shells", "1 cup shredded lettuce", "1 avocado, sliced", "1/2 cup salsa", "1 cup cooked beans"],
                "instructions": "Warm taco shells in the oven at 350°F for 5 minutes; slice avocado, shred lettuce, and warm beans; fill shells with lettuce, avocado, salsa, and beans."
            },
            "Vegan Burritos": {
                "dish": "Vegan Burritos",
                "time": 25,
                "ingredients": ["4 large flour tortillas", "1 cup cooked beans", "1 cup rice, cooked", "1 cup shredded lettuce", "1/2 cup salsa"],
                "instructions": "Warm tortillas in a pan; layer with rice, beans, lettuce, and salsa; roll up the tortillas and serve."
            },
            "Vegan Enchiladas": {
                "dish": "Vegan Enchiladas",
                "time": 50,
                "ingredients": ["8 corn tortillas", "1 cup cooked beans", "1 cup vegan cheese", "1 cup salsa"],
                "instructions": "Preheat oven to 350°F; fill tortillas with beans and vegan cheese, roll them up, place in a baking dish, top with salsa, and bake for 25 minutes."
            },
            "Vegan Quesadillas": {
                "dish": "Vegan Quesadillas",
                "time": 20,
                "ingredients": ["2 flour tortillas", "1 cup vegan cheese", "1/4 cup salsa", "1 avocado, sliced"],
                "instructions": "Place vegan cheese between tortillas and grill in a skillet until golden brown, then serve with salsa and sliced avocado."
            },
            "Vegan Fajitas": {
                "dish": "Vegan Fajitas",
                "time": 25,
                "ingredients": ["1 bell pepper, sliced", "1 onion, sliced", "1 tbsp fajita seasoning", "4 tortillas"],
                "instructions": "Sauté bell pepper and onion with fajita seasoning until tender; serve with warm tortillas."
            },
            "Vegan Tamales": {
                "dish": "Vegan Tamales",
                "time": 120,
                "ingredients": ["2 cups masa harina", "1/2 cup vegetable broth", "1 cup salsa", "1 cup vegan filling (e.g., mushrooms or squash)"],
                "instructions": "Soak corn husks for 30 minutes. Mix masa harina with vegetable broth. Spread masa on corn husks, add vegan filling, wrap, and steam for 1-1.5 hours."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_fish_recipe(name):
        recipes = {
            "Fish Tacos": {
                "dish": "Fish Tacos",
                "time": 20,
                "ingredients": ["500g white fish fillets", "8 taco shells", "1 cup shredded cabbage", "1/2 cup salsa", "1 lime, cut into wedges"],
                "instructions": "Grill fish fillets for 6-8 minutes, then fill taco shells with fish, shredded cabbage, salsa, and a squeeze of lime."
            },
            "Crispy Fish Tacos": {
                "dish": "Crispy Fish Tacos",
                "time": 30,
                "ingredients": ["500g white fish fillets", "8 corn tortillas", "1 cup shredded cabbage", "1/2 cup salsa", "1 lime"],
                "instructions": "Fry fish fillets in hot oil until crispy and golden, then place them in warm corn tortillas and top with shredded cabbage, salsa, and a squeeze of lime juice."
            },
            "Grilled Fish Burritos": {
                "dish": "Grilled Fish Burritos",
                "time": 30,
                "ingredients": ["500g white fish fillets", "4 tortillas", "1 cup rice", "1 cup beans", "1/4 cup salsa"],
                "instructions": "Grill the fish fillets for 5-7 minutes, then roll them up with cooked rice, beans, and salsa in flour tortillas to create burritos."
            },
            "Fish Veracruz": {
                "dish": "Fish Veracruz",
                "time": 45,
                "ingredients": ["500g white fish fillets", "2 tomatoes, chopped", "1/4 cup olives", "1 onion, sliced", "1 bell pepper, sliced"],
                "instructions": "Simmer the fish fillets with chopped tomatoes, olives, sliced onions, and bell peppers for 15-20 minutes, until the fish is fully cooked and the flavors have melded together."
            },
            "Fish Ceviche": {
                "dish": "Fish Ceviche",
                "time": 30,
                "ingredients": ["500g white fish, diced", "Juice of 3 limes", "1 tomato, chopped", "1 onion, chopped", "1/4 cup cilantro, chopped"],
                "instructions": "Marinate the diced fish in lime juice for 2-3 hours until it 'cooks' in the acidity, then mix with chopped tomato, onion, and cilantro for a fresh ceviche."
            },
            "Fish Fajitas": {
                "dish": "Fish Fajitas",
                "time": 25,
                "ingredients": ["500g white fish fillets", "1 bell pepper, sliced", "1 onion, sliced", "1 tbsp fajita seasoning", "4 tortillas"],
                "instructions": "Cook the fish fillets with sliced bell peppers and onions in a skillet, season with fajita seasoning, then serve with warm tortillas."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_lamb_recipe(name):
        recipes = {
            "Lamb Tacos": {
                "dish": "Lamb Tacos",
                "time": 30,
                "ingredients": ["500g ground lamb", "8 taco shells", "1 onion, diced", "1/4 cup cilantro, chopped", "1/2 cup salsa"],
                "instructions": "Cook ground lamb in a skillet over medium heat for 7-10 minutes, breaking it up as it cooks. Season with your choice of spices. Fill taco shells with cooked lamb, diced onions, fresh cilantro, and salsa."
            },
            "Lamb Burritos": {
                "dish": "Lamb Burritos",
                "time": 25,
                "ingredients": ["500g ground lamb", "4 large flour tortillas", "1 cup rice, cooked", "1 cup beans", "1 cup shredded cheese"],
                "instructions": "Brown the ground lamb in a skillet over medium heat for 8-10 minutes. Lay the cooked lamb on each flour tortilla and top with rice, beans, and shredded cheese. Roll the tortillas to form burritos."
            },
            "Lamb Fajitas": {
                "dish": "Lamb Fajitas",
                "time": 25,
                "ingredients": ["500g lamb, sliced", "1 bell pepper, sliced", "1 onion, sliced", "2 tbsp fajita seasoning", "Tortillas for serving"],
                "instructions": "Sauté sliced lamb, bell peppers, and onions in a skillet with fajita seasoning over medium-high heat for 8-10 minutes. Serve with warm tortillas."
            },
            "Lamb Enchiladas": {
                "dish": "Lamb Enchiladas",
                "time": 60,
                "ingredients": ["500g lamb, shredded", "8 corn tortillas", "1 cup shredded cheese", "1 cup salsa"],
                "instructions": "Roll the shredded lamb in corn tortillas and place them in a baking dish. Top with salsa and shredded cheese. Bake at 350°F for 25 minutes, or until cheese is melted and bubbly."
            },
            "Braised Lamb Shank": {
                "dish": "Braised Lamb Shank",
                "time": 120,
                "ingredients": ["2 lamb shanks", "2 tomatoes, chopped", "1 onion, chopped", "1 tbsp cinnamon", "1 tbsp cumin", "1 tbsp garlic powder"],
                "instructions": "Brown lamb shanks in a pot over medium-high heat for 5-7 minutes. Add chopped tomatoes, onions, cinnamon, cumin, and garlic powder. Simmer for 2 hours, until lamb is tender."
            },
            "Lamb Quesadillas": {
                "dish": "Lamb Quesadillas",
                "time": 20,
                "ingredients": ["500g lamb, cooked and shredded", "2 flour tortillas", "1 cup shredded cheese", "1/4 cup salsa"],
                "instructions": "Place cooked and shredded lamb and shredded cheese between two flour tortillas. Grill on medium heat for 3-4 minutes per side, until golden and crispy. Serve with salsa."
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
api.add_resource(UpdateRecipe, '/edit_recipe/<int:recipe_id>')
        
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