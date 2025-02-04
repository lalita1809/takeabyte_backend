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
                "ingredients": ["2 chicken breasts, thinly sliced", "200g rice noodles", "1/4 cup peanuts, chopped", "1 lime, cut into wedges", "2 tbsp soy sauce", "1 tbsp fish sauce", "1 tbsp brown sugar", "2 eggs", "2 cloves garlic, minced", "1/2 cup bean sprouts", "2 tbsp vegetable oil", "1/2 cup green onions, chopped", "1/4 tsp chili flakes (optional)"],
                "instructions": "Cook the rice noodles according to package instructions, then drain and set aside. Heat 1 tablespoon of oil in a pan and scramble the eggs. Set aside. In the same pan, heat another tablespoon of oil, then add the garlic and chicken slices. Stir-fry until the chicken is cooked through. Add the cooked noodles to the pan and pour in the soy sauce, fish sauce, brown sugar, and chili flakes (if using). Toss everything together. Stir in the scrambled eggs, green onions, and bean sprouts. Serve with chopped peanuts and lime wedges on top."
            },
            "Thai Green Curry Chicken": {
                "dish": "Thai Green Curry Chicken",
                "time": 50,
                "ingredients": ["2 chicken breasts, thinly sliced", "1 can (400ml) coconut milk", "2 tbsp green curry paste", "1/2 cup bamboo shoots, drained", "1/2 cup bell peppers, sliced", "1/4 cup fresh basil leaves", "1 tbsp fish sauce", "1 tbsp sugar", "1 tbsp vegetable oil", "1/2 cup chicken broth", "1/4 cup lime leaves (optional)", "1 red chili, sliced (optional)"],
                "instructions": "In a large pot, heat vegetable oil over medium heat. Add the green curry paste and fry for 1-2 minutes. Add the chicken and cook for 5-6 minutes. Pour in the coconut milk and chicken broth, and bring to a simmer. Add bamboo shoots, bell peppers, basil leaves, and fish sauce. Simmer for 20-25 minutes, until the chicken is cooked through. Garnish with lime leaves and chili slices. Serve with rice."
            },
            "Thai Basil Chicken": {
                "dish": "Thai Basil Chicken",
                "time": 25,
                "ingredients": ["2 chicken breasts, sliced", "1/2 cup fresh basil leaves", "2 cloves garlic, minced", "2 red chilies, sliced", "2 tbsp soy sauce", "1 tbsp fish sauce", "1 tbsp oyster sauce", "1 tbsp vegetable oil", "1 tsp sugar", "1/2 onion, sliced", "1/4 cup chicken broth"],
                "instructions": "Heat vegetable oil in a pan over medium heat. Add garlic, chilies, and onions, stir-fry for 2 minutes. Add chicken slices and cook for 6-7 minutes. Stir in soy sauce, fish sauce, oyster sauce, sugar, and chicken broth. Cook for another 3-4 minutes. Add basil leaves and toss until wilted. Serve with rice."
            },
            "Thai Red Curry Chicken": {
                "dish": "Thai Red Curry Chicken",
                "time": 50,
                "ingredients": ["2 chicken breasts, thinly sliced", "1 can (400ml) coconut milk", "3 tbsp red curry paste", "1/2 cup carrots, sliced", "1/2 cup bell peppers, sliced", "1/4 cup bamboo shoots", "1 tbsp fish sauce", "1 tbsp sugar", "1 tbsp vegetable oil", "1/2 cup chicken broth", "1/4 cup fresh basil leaves"],
                "instructions": "Heat vegetable oil in a pot and fry the red curry paste for 2-3 minutes. Add chicken and cook for 5 minutes. Add coconut milk, chicken broth, carrots, bell peppers, bamboo shoots, fish sauce, and sugar. Simmer for 20-25 minutes until the chicken is cooked. Stir in basil leaves before serving. Serve with steamed rice."
            },
            "Thai Lemon Chicken": {
                "dish": "Thai Lemon Chicken",
                "time": 35,
                "ingredients": ["2 chicken breasts, boneless and skinless", "1 stalk lemongrass, finely chopped", "2 cloves garlic, minced", "1 lime, juiced", "2 tbsp fish sauce", "1 tbsp soy sauce", "1 tsp brown sugar", "1 tbsp vegetable oil", "1 tbsp fresh cilantro, chopped"],
                "instructions": "In a bowl, mix lime juice, fish sauce, soy sauce, sugar, lemongrass, and garlic. Marinate chicken in this mixture for 20 minutes. Heat vegetable oil in a pan and cook chicken for 6-7 minutes on each side, until golden brown. Garnish with cilantro and serve with rice."
            },
            "Thai Chicken Satay": {
                "dish": "Thai Chicken Satay",
                "time": 40,
                "ingredients": ["2 chicken breasts, cut into strips", "1/4 cup peanut butter", "2 tbsp soy sauce", "1 tbsp curry powder", "1/2 cup coconut milk", "1 tbsp brown sugar", "1 tbsp vegetable oil", "1/2 tsp garlic powder", "Wooden skewers"],
                "instructions": "Mix peanut butter, soy sauce, curry powder, coconut milk, brown sugar, garlic powder, and vegetable oil into a marinade. Marinate chicken strips for at least 30 minutes. Thread chicken onto wooden skewers. Grill for 5-7 minutes on each side. Serve with extra peanut sauce."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_beef_recipe(name):
        recipes = {
            "Pad Thai Beef": {
                "dish": "Pad Thai Beef",
                "time": 30,
                "ingredients": ["200g beef, thinly sliced", "200g rice noodles", "1/4 cup peanuts, crushed", "1 lime, cut into wedges", "2 tbsp soy sauce", "1 tbsp fish sauce", "1 tbsp brown sugar", "2 eggs, beaten", "2 cloves garlic, minced", "1/2 cup bean sprouts", "2 tbsp vegetable oil", "1/2 cup green onions, chopped", "1/4 tsp chili flakes (optional)"],
                "instructions": "Cook rice noodles according to package instructions. In a pan, heat 1 tablespoon of oil and scramble the eggs until cooked. Remove and set aside. In the same pan, add garlic and beef slices, and stir-fry for 5 minutes until the beef is cooked. Add cooked noodles, soy sauce, fish sauce, brown sugar, and chili flakes (optional). Stir well and toss in eggs, bean sprouts, and green onions. Garnish with peanuts and lime wedges."
            },
            "Thai Beef Salad": {
                "dish": "Thai Beef Salad",
                "time": 30,
                "ingredients": ["200g beef (steak or tenderloin), grilled", "1 cup lettuce, shredded", "1/2 cup cilantro, chopped", "1 lime, juiced", "2 tbsp fish sauce", "1 tbsp soy sauce", "1 tbsp brown sugar", "1 cucumber, sliced", "1 red onion, thinly sliced", "1 chili, sliced", "1/2 cup tomatoes, sliced"],
                "instructions": "Grill beef to desired doneness. Let rest before slicing thinly. In a large bowl, combine lettuce, cilantro, cucumber, onion, tomatoes, and chili. In a separate bowl, mix lime juice, fish sauce, soy sauce, and brown sugar to make the dressing. Toss the salad with the dressing and top with sliced beef."
            },
            "Thai Red Curry Beef": {
                "dish": "Thai Red Curry Beef",
                "time": 50,
                "ingredients": ["200g beef, thinly sliced", "1 can (400ml) coconut milk", "3 tbsp red curry paste", "1/2 cup carrots, sliced", "1/2 cup bell peppers, sliced", "1 tbsp fish sauce", "1 tbsp sugar", "1 tbsp vegetable oil", "1/2 cup chicken broth", "1/4 cup basil leaves"],
                "instructions": "Heat oil in a pan and sauté the red curry paste for 2-3 minutes. Add beef slices and cook until browned. Pour in coconut milk and chicken broth, then add carrots, bell peppers, fish sauce, and sugar. Let it simmer for 20-25 minutes, then add basil leaves and stir well. Serve with jasmine rice."
            },
            "Thai Basil Beef": {
                "dish": "Thai Basil Beef",
                "time": 25,
                "ingredients": ["200g beef, sliced", "1/2 cup fresh basil leaves", "2 cloves garlic, minced", "2 red chilies, sliced", "2 tbsp soy sauce", "1 tbsp fish sauce", "1 tbsp oyster sauce", "1 tbsp vegetable oil", "1 tsp sugar", "1/2 onion, sliced", "1/4 cup chicken broth"],
                "instructions": "Heat oil in a wok and stir-fry garlic, chilies, and onion for 2 minutes. Add sliced beef and cook for 4-5 minutes. Stir in soy sauce, fish sauce, oyster sauce, sugar, and chicken broth. Let it simmer for 2-3 minutes, then add basil leaves and toss until wilted. Serve with steamed rice."
            },
            "Thai Beef Skewers": {
                "dish": "Thai Beef Skewers",
                "time": 40,
                "ingredients": ["200g beef, cut into cubes", "2 tbsp soy sauce", "1 tbsp ginger, minced", "1 tbsp garlic, minced", "1 tbsp lemongrass, chopped", "1 tbsp vegetable oil", "1 tsp brown sugar", "1/4 cup lime juice", "Wooden skewers"],
                "instructions": "Marinate beef cubes in soy sauce, ginger, garlic, lemongrass, vegetable oil, brown sugar, and lime juice for at least 30 minutes. Thread the beef onto skewers and grill for 4-5 minutes on each side. Serve with dipping sauce."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_vegan_recipe(name):
        recipes = {
            "Vegan Pad Thai": {
                "dish": "Vegan Pad Thai",
                "time": 30,
                "ingredients": ["200g tofu, pressed and cubed", "200g rice noodles", "1/4 cup peanuts, crushed", "1 lime, cut into wedges", "2 tbsp soy sauce", "1 tbsp brown sugar", "2 tbsp vegetable oil", "1/2 cup bean sprouts", "1/2 cup green onions, chopped", "1/4 tsp chili flakes (optional)"],
                "instructions": "Cook rice noodles according to package instructions. In a pan, heat 1 tablespoon of oil and sauté tofu cubes until golden brown. Remove and set aside. In the same pan, add garlic and sauté until fragrant, then add the noodles, soy sauce, brown sugar, and chili flakes (optional). Stir well and toss in tofu, bean sprouts, and green onions. Garnish with crushed peanuts and lime wedges."
            },
            "Vegan Thai Green Curry": {
                "dish": "Vegan Thai Green Curry",
                "time": 50,
                "ingredients": ["1 can (400ml) coconut milk", "2 tbsp green curry paste", "1/2 cup bamboo shoots, drained", "1/2 cup bell peppers, sliced", "1/2 cup carrots, sliced", "1/4 cup fresh basil leaves", "1 tbsp soy sauce", "1 tbsp sugar", "1 tbsp vegetable oil", "1/2 cup vegetable broth", "1 red chili, sliced (optional)"],
                "instructions": "In a pot, heat vegetable oil and sauté the green curry paste for 2-3 minutes. Add coconut milk and vegetable broth, then bring to a simmer. Add bamboo shoots, bell peppers, carrots, soy sauce, and sugar. Let it simmer for 20-25 minutes. Stir in basil leaves and serve with rice."
            },
            "Vegan Thai Basil Stir-fry": {
                "dish": "Vegan Thai Basil Stir-fry",
                "time": 25,
                "ingredients": ["200g tofu, cubed", "1/2 cup fresh basil leaves", "2 garlic cloves, minced", "1/2 cup bell peppers, sliced", "1/2 cup onions, sliced", "2 tbsp soy sauce", "1 tbsp vegetable oil", "1 tbsp lime juice", "1 tsp sugar", "1 red chili, chopped (optional)"],
                "instructions": "Heat oil in a pan and sauté tofu until golden and crispy. Remove and set aside. In the same pan, sauté garlic for 1 minute, add bell peppers and onions, and stir-fry for another 3-4 minutes. Add soy sauce, lime juice, and sugar, and toss in tofu and basil leaves. Garnish with chopped red chili (optional)."
            },
            "Vegan Thai Red Curry": {
                "dish": "Vegan Thai Red Curry",
                "time": 50,
                "ingredients": ["1 can (400ml) coconut milk", "2 tbsp red curry paste", "1/2 cup carrots, sliced", "1/2 cup zucchini, sliced", "1/2 cup bell peppers, sliced", "1/2 cup tofu, cubed", "1 tbsp soy sauce", "1 tbsp brown sugar", "1/4 cup fresh cilantro", "1 tbsp lime juice"],
                "instructions": "In a pot, heat vegetable oil and sauté red curry paste for 2 minutes. Add coconut milk and bring to a simmer. Add carrots, zucchini, bell peppers, tofu, soy sauce, and brown sugar. Let simmer for 25-30 minutes, then stir in lime juice and fresh cilantro before serving with steamed rice."
            },
            "Vegan Thai Salad": {
                "dish": "Vegan Thai Salad",
                "time": 20,
                "ingredients": ["1 cup lettuce, shredded", "1/2 cup cucumber, sliced", "1/2 cup carrots, shredded", "1/4 cup red cabbage, shredded", "1/4 cup cilantro, chopped", "1 tbsp soy sauce", "1 tbsp lime juice", "1 tbsp sesame oil", "1 tbsp peanut butter", "1 tsp sugar", "1 red chili, sliced (optional)"],
                "instructions": "In a large bowl, toss together lettuce, cucumber, carrots, cabbage, and cilantro. In a separate small bowl, whisk together soy sauce, lime juice, sesame oil, peanut butter, sugar, and red chili (optional). Pour the dressing over the salad and toss to combine. Serve immediately."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_fish_recipe(name):
        recipes = {
            "Thai Fish Curry": {
                "dish": "Thai Fish Curry",
                "time": 50,
                "ingredients": ["500g white fish fillets (e.g. tilapia, cod)", "1 can (400ml) coconut milk", "2 tbsp red curry paste", "1/2 cup bell peppers, sliced", "1/2 cup zucchini, sliced", "1/4 cup fresh cilantro", "1 tbsp soy sauce", "1 tbsp brown sugar", "1 tbsp vegetable oil", "1 lime, juiced"],
                "instructions": "In a pot, heat vegetable oil and sauté the red curry paste for 2 minutes. Add coconut milk and bring to a simmer. Add fish fillets, bell peppers, zucchini, soy sauce, and sugar. Simmer for 20-25 minutes until fish is cooked through. Stir in lime juice and fresh cilantro before serving."
            },
            "Thai Steamed Fish with Lime and Garlic": {
                "dish": "Thai Steamed Fish with Lime and Garlic",
                "time": 30,
                "ingredients": ["1 whole fish (about 500g)", "2 garlic cloves, minced", "1 lime, sliced", "1 tbsp fish sauce", "2 spring onions, chopped", "1 red chili, sliced", "1/4 cup cilantro", "1 tbsp soy sauce", "1 tbsp vegetable oil"],
                "instructions": "Steam the whole fish for 15-20 minutes. Meanwhile, heat vegetable oil in a pan and sauté garlic until fragrant. Add soy sauce and fish sauce. Once the fish is done, pour the garlic sauce over it. Garnish with lime slices, spring onions, chili, and fresh cilantro."
            },
            "Thai Fish Cakes": {
                "dish": "Thai Fish Cakes",
                "time": 25,
                "ingredients": ["400g white fish fillets, minced", "2 tbsp green curry paste", "1 egg", "1 tbsp fish sauce", "1/4 cup fresh basil, chopped", "1/4 cup breadcrumbs", "1 tbsp vegetable oil", "1 red chili, chopped (optional)", "1 tbsp lime juice"],
                "instructions": "In a bowl, mix minced fish, green curry paste, egg, fish sauce, basil, breadcrumbs, and lime juice. Form into small patties. Heat oil in a pan and fry fish cakes for 2-3 minutes per side until golden and crispy. Serve with a side of lime wedges and chili sauce."
            },
            "Crispy Thai Fish Fillets": {
                "dish": "Crispy Thai Fish Fillets",
                "time": 20,
                "ingredients": ["400g white fish fillets (e.g. tilapia, cod)", "1/2 cup cornflour", "1/4 cup rice flour", "1/4 tsp turmeric", "1/2 tsp paprika", "1 egg, beaten", "1/4 tsp salt", "1/2 tsp pepper", "1 tbsp soy sauce", "1 tbsp vegetable oil"],
                "instructions": "Mix cornflour, rice flour, turmeric, paprika, salt, and pepper. Dip fish fillets in beaten egg, then coat in flour mixture. Heat oil in a pan and fry the fish fillets for 3-4 minutes per side until crispy. Serve with a soy sauce dipping sauce and garnish with fresh cilantro."
            },
            "Grilled Thai Fish Skewers": {
                "dish": "Grilled Thai Fish Skewers",
                "time": 35,
                "ingredients": ["500g white fish fillets, cut into chunks", "1 tbsp soy sauce", "1 tbsp fish sauce", "1 tbsp lime juice", "1 tbsp brown sugar", "2 garlic cloves, minced", "1/4 cup fresh cilantro, chopped", "1/2 tsp chili flakes", "Skewers (wooden or metal)"],
                "instructions": "In a bowl, mix soy sauce, fish sauce, lime juice, brown sugar, garlic, cilantro, and chili flakes. Marinate the fish for 20 minutes. Thread the fish onto skewers and grill for 5-7 minutes on each side, until the fish is cooked through. Serve with a side of grilled vegetables."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_lamb_recipe(name):
        recipes = {
            "Thai Braised Lamb": {
                "dish": "Thai Braised Lamb",
                "time": 60,
                "ingredients": ["1kg lamb shanks", "1 can (400ml) coconut milk", "2 tbsp green curry paste", "1 onion, chopped", "2 garlic cloves, minced", "1 tbsp soy sauce", "1 tbsp fish sauce", "1 tbsp brown sugar", "1 lime, juiced", "2 sprigs fresh basil", "1 tbsp vegetable oil"],
                "instructions": "Heat oil in a pot and sear lamb shanks until browned on all sides. Remove and set aside. In the same pot, sauté garlic and onion for 3 minutes, then add green curry paste and cook for 1 more minute. Add coconut milk, soy sauce, fish sauce, sugar, and lime juice. Return the lamb shanks to the pot, cover, and braise for 45 minutes to 1 hour until tender. Garnish with fresh basil."
            },
            "Thai Lamb Skewers": {
                "dish": "Thai Lamb Skewers",
                "time": 35,
                "ingredients": ["500g lamb, cut into cubes", "2 tbsp soy sauce", "1 tbsp fish sauce", "1 tbsp lime juice", "1 tbsp brown sugar", "1 tsp ground cumin", "1 tsp ground coriander", "1 tbsp fresh ginger, minced", "1 tbsp garlic, minced", "Wooden or metal skewers"],
                "instructions": "In a bowl, mix soy sauce, fish sauce, lime juice, brown sugar, cumin, coriander, ginger, and garlic. Marinate lamb cubes for 30 minutes. Thread lamb onto skewers and grill for 8-10 minutes, turning occasionally. Serve with a side of peanut sauce or dipping sauce."
            },
            "Thai Lamb Red Curry": {
                "dish": "Thai Lamb Red Curry",
                "time": 50,
                "ingredients": ["500g lamb, cubed", "1 can (400ml) coconut milk", "2 tbsp red curry paste", "1/2 cup bell peppers, sliced", "1/2 cup carrots, sliced", "1 tbsp soy sauce", "1 tbsp fish sauce", "1 tbsp brown sugar", "1 tbsp vegetable oil", "1/4 cup fresh cilantro, chopped"],
                "instructions": "In a pot, heat oil and sauté red curry paste for 2 minutes. Add coconut milk and bring to a simmer. Add lamb, bell peppers, carrots, soy sauce, fish sauce, and sugar. Simmer for 25-30 minutes until the lamb is cooked and tender. Garnish with fresh cilantro before serving."
            },
            "Crying Tiger Lamb": {
                "dish": "Crying Tiger Lamb",
                "time": 40,
                "ingredients": ["500g lamb, thinly sliced", "1 tbsp soy sauce", "1 tbsp fish sauce", "1 tbsp lime juice", "1 tbsp brown sugar", "1 tbsp vegetable oil", "1 tbsp chili flakes", "1/4 cup fresh cilantro", "1 garlic clove, minced", "1/2 red onion, thinly sliced"],
                "instructions": "Mix soy sauce, fish sauce, lime juice, sugar, and chili flakes in a bowl. Marinate lamb slices in this mixture for 20 minutes. Heat oil in a pan and sauté lamb slices for 5-7 minutes until crispy and tender. Serve with cilantro and thinly sliced red onion."
            },
            "Thai Massaman Lamb Curry": {
                "dish": "Thai Massaman Lamb Curry",
                "time": 70,
                "ingredients": ["1kg lamb, cubed", "1 can (400ml) coconut milk", "2 tbsp Massaman curry paste", "1 potato, cubed", "1 onion, chopped", "1/4 cup peanuts", "1 tbsp soy sauce", "1 tbsp fish sauce", "1 tbsp brown sugar", "1/4 tsp cinnamon", "1/4 tsp star anise", "1 tbsp vegetable oil"],
                "instructions": "In a pot, heat oil and sauté Massaman curry paste for 2 minutes. Add coconut milk, soy sauce, fish sauce, sugar, cinnamon, and star anise. Add lamb and potatoes and cook on low heat for 45 minutes to 1 hour, until the lamb is tender. Garnish with roasted peanuts."
            },
            "Thai Basil and Lemongrass Rack of Lamb": {
                "dish": "Thai Basil and Lemongrass Rack of Lamb",
                "time": 90,
                "ingredients": ["1 rack of lamb (about 1kg)", "1/4 cup fresh basil", "2 stalks lemongrass, minced", "2 garlic cloves, minced", "1 tbsp soy sauce", "1 tbsp fish sauce", "1 tbsp brown sugar", "1 tbsp vegetable oil", "1 tbsp lime juice", "1 tbsp chili flakes (optional)"],
                "instructions": "Blend basil, lemongrass, garlic, soy sauce, fish sauce, brown sugar, lime juice, and chili flakes into a paste. Rub the paste over the rack of lamb and marinate for at least 1 hour. Preheat the grill or oven and cook lamb for 25-30 minutes, or until the desired doneness is reached. Serve with jasmine rice or sautéed vegetables."
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
