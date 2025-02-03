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
                "ingredients": ["4 chicken thighs (boneless, skinless)", "1/4 cup soy sauce", "2 tbsp honey", "2 tbsp rice vinegar", "2 tsp sesame oil", "1 garlic clove (minced)", "1 tbsp grated ginger", "1 tbsp sesame seeds", "1/4 cup green onions (sliced)"],
                "instructions": "In a bowl, mix soy sauce, honey, rice vinegar, sesame oil, garlic, and ginger. Marinate the chicken thighs in this mixture for 20 minutes. Heat a pan over medium heat and cook chicken for 7-8 minutes on each side until fully cooked. Sprinkle with sesame seeds and green onions before serving. Serve with steamed rice."
            },
            "Chicken Katsu": {
                "dish": "Chicken Katsu",
                "time": 40,
                "ingredients": ["2 chicken breasts (boneless, skinless)", "1 cup breadcrumbs", "1/2 cup all-purpose flour", "2 large eggs (beaten)", "2 tbsp soy sauce", "2 tbsp vegetable oil", "1/4 cup tonkatsu sauce"],
                "instructions": "Tenderize the chicken breasts by gently pounding them to an even thickness. Dredge each piece in flour, dip in beaten eggs, and coat with breadcrumbs. Heat oil in a frying pan and cook the chicken for 5-6 minutes per side, until golden brown and crispy. Serve with tonkatsu sauce."
            },
            "Chicken Yakitori": {
                "dish": "Chicken Yakitori",
                "time": 25,
                "ingredients": ["4 chicken skewers (cut into bite-sized pieces)", "2 tbsp soy sauce", "1 tbsp sake", "1 tbsp mirin", "1 tbsp honey", "1 tbsp sesame oil", "2 green onions (sliced)"],
                "instructions": "Mix soy sauce, sake, mirin, honey, and sesame oil in a bowl to make the marinade. Marinate chicken pieces for 10-15 minutes. Thread chicken onto skewers and grill over medium heat for 4-5 minutes on each side, brushing with the marinade during cooking. Garnish with green onions before serving."
            },
            "Chicken Ramen": {
                "dish": "Chicken Ramen",
                "time": 50,
                "ingredients": ["2 chicken breasts (boneless, skinless)", "4 cups chicken broth", "2 packs ramen noodles", "2 tbsp soy sauce", "1 tbsp miso paste", "2 garlic cloves (minced)", "2 green onions (sliced)", "1 egg (soft-boiled)", "1 tbsp sesame oil"],
                "instructions": "Simmer chicken breasts in chicken broth for 20 minutes, then remove and shred the chicken. In the same pot, add soy sauce, miso paste, garlic, and sesame oil. Cook the ramen noodles according to package instructions and add to the broth. Serve the noodles with shredded chicken, soft-boiled egg, and green onions."
            },
            "Chicken Karaage": {
                "dish": "Chicken Karaage",
                "time": 35,
               "ingredients": ["4 chicken thighs (boneless, cut into chunks)", "1/4 cup soy sauce", "1 tbsp sake", "1 tbsp grated ginger", "2 cloves garlic (minced)", "1/2 cup potato starch", "1/2 cup all-purpose flour", "Vegetable oil for frying"],
                "instructions": "In a bowl, mix soy sauce, sake, ginger, and garlic. Marinate chicken chunks for 15 minutes. In a separate bowl, combine potato starch and flour. Coat the marinated chicken in the flour mixture. Heat oil in a pan over medium heat and fry the chicken for 4-5 minutes until golden and crispy. Serve with a wedge of lemon."
            },
            "Chicken Donburi": {
                "dish": "Chicken Donburi",
                "time": 45,
                "ingredients": ["2 chicken breasts (sliced)", "1 cup rice (cooked)", "2 tbsp soy sauce", "1 tbsp mirin", "1 tbsp sugar", "1 egg (beaten)", "1/4 cup green onions (chopped)", "1/4 cup cooked spinach"],
                "instructions": "In a skillet, cook sliced chicken with soy sauce, mirin, and sugar until fully cooked. In a separate pan, scramble the beaten egg. Serve the cooked chicken over steamed rice, top with scrambled egg, cooked spinach, and green onions."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_beef_recipe(name):
        recipes = {
            "Beef Teriyaki": {
                "dish": "Beef Teriyaki",
                "time": 30,
                "ingredients": ["500g beef (sliced thinly, preferably ribeye or sirloin)", "1/4 cup soy sauce", "2 tbsp mirin", "1 tbsp sake", "1 tbsp sugar", "1 tsp garlic (minced)", "1 tsp ginger (grated)", "2 tbsp vegetable oil", "Sesame seeds (for garnish)", "Green onions (for garnish)", "Steamed rice (to serve)"],
                "instructions": "In a small bowl, whisk together soy sauce, mirin, sake, sugar, garlic, and ginger to make the teriyaki sauce. Heat vegetable oil in a pan over medium-high heat, and sauté beef slices for 3-4 minutes until browned. Add the teriyaki sauce and cook for another 2-3 minutes until the sauce thickens. Garnish with sesame seeds and chopped green onions. Serve with steamed rice."
            },
            "Beef Sukiyaki": {
                "dish": "Beef Sukiyaki",
                "time": 60,
                "ingredients": ["500g thinly sliced beef (ribeye or sirloin)", "1 cup soy sauce", "1/2 cup sugar", "1/2 cup mirin", "1/2 cup sake", "1 block tofu (cubed)", "1 onion (sliced)", "1 carrot (sliced)", "100g shiitake mushrooms", "2 cups spinach", "1 tbsp sesame oil"],
                "instructions": "Heat sesame oil in a large pot. Add the beef and sear until browned. Add the onion, carrot, mushrooms, and tofu. In a separate bowl, mix soy sauce, sugar, mirin, and sake. Pour the mixture into the pot and bring it to a simmer. Add the spinach and let everything cook for 20-30 minutes until tender. Serve with steamed rice."
            },
            "Gyudon": {
                "dish": "Gyudon",
                "time": 30,
                "ingredients": ["500g beef (thinly sliced, like flank or ribeye)", "2 cups rice", "1 onion (sliced)", "1/4 cup soy sauce", "2 tbsp mirin", "1 tbsp sugar", "1 tbsp sake", "2 soft-boiled eggs (optional)"],
                "instructions": "Cook the rice and set it aside. In a pan, sauté the onion until soft, then add the beef and cook until browned. Add the soy sauce, mirin, sugar, and sake, and let it simmer for 5-10 minutes. Serve the beef mixture over rice, and top with a soft-boiled egg."
            },
            "Beef Yakiniku": {
                "dish": "Beef Yakiniku",
                "time": 40,
                "ingredients": ["500g beef (sirloin or short ribs, thinly sliced)", "2 tbsp soy sauce", "1 tbsp sesame oil", "2 tbsp sake", "1 tsp garlic (minced)", "1 tbsp sugar", "2 tbsp sesame seeds", "1 tbsp green onions (chopped)"],
                "instructions": "Mix soy sauce, sesame oil, sake, garlic, and sugar in a bowl. Marinate the beef for 15 minutes. Grill or pan-fry the beef slices for 2-3 minutes on each side. Garnish with sesame seeds and chopped green onions. Serve with rice."
            },
            "Beef Shabu-Shabu": {
                "dish": "Beef Shabu-Shabu",
                "time": 35,
                "ingredients": ["500g thinly sliced beef (ribeye or sirloin)", "1/2 napa cabbage (chopped)", "1 block tofu (cubed)", "2 cups shiitake mushrooms", "1/2 cup soy sauce", "1 tbsp sesame oil", "2 cups kombu dashi (seaweed broth)", "Ponzu sauce (for dipping)", "Green onions (for garnish)"],
                "instructions": "Bring kombu dashi to a simmer in a large pot. Add the napa cabbage, mushrooms, and tofu. Dip the thinly sliced beef into the broth for 10-15 seconds until just cooked. Serve with ponzu sauce and garnish with green onions."
            },
            "Beef Tataki": {
                "dish": "Beef Tataki",
                "time": 30,
                "ingredients": ["500g beef (flank or ribeye, sliced)", "2 cups rice", "1 onion (sliced)", "1/4 cup soy sauce", "1 tbsp sugar", "2 tbsp mirin", "1 tbsp sake", "1/4 cup dashi stock", "1 egg (optional)"],
                "instructions": "Cook rice and set it aside. In a pan, sauté the onion until soft. Add the beef, soy sauce, sugar, mirin, sake, and dashi stock, and let it simmer for 10-12 minutes. Serve the beef mixture over rice. Optionally, top with a raw or soft-boiled egg."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_vegan_recipe(name):
        recipes = {
            "Vegan Ramen": {
                "dish": "Vegan Ramen",
                "time": 40,
                "ingredients": ["2 packs ramen noodles", "1 tbsp sesame oil", "1 onion (chopped)", "2 cloves garlic (minced)", "1-inch piece ginger (grated)", "1 carrot (julienned)", "2 cups mushrooms (shiitake or button, sliced)", "1/2 cup soy sauce", "1 tbsp miso paste", "4 cups vegetable broth", "2 cups spinach", "1 tsp sesame seeds (for garnish)"],
                "instructions": "Heat sesame oil in a large pot and sauté onions, garlic, and ginger until softened. Add the carrots and mushrooms, cooking for 3-4 minutes. Add soy sauce, miso paste, and vegetable broth, then bring to a boil. Add ramen noodles and cook according to package instructions. Stir in spinach until wilted. Serve with sesame seeds as garnish."
            },
            "Vegan Sushi": {
                "dish": "Vegan Sushi",
                "time": 50,
                "ingredients": ["2 cups sushi rice", "2 1/2 cups water", "1/4 cup rice vinegar", "1 tbsp sugar", "1 tsp salt", "Nori sheets", "1 cucumber (cut into thin strips)", "1 avocado (sliced)", "1 carrot (cut into thin strips)", "Soy sauce (for dipping)"],
                "instructions": "Cook the sushi rice and let it cool. Mix rice vinegar, sugar, and salt in a bowl and stir into the cooled rice. Lay a sheet of nori on a bamboo mat, and spread a thin layer of rice on top. Add cucumber, avocado, and carrot in the center. Roll the sushi tightly and slice into pieces. Serve with soy sauce for dipping."
            },
            "Vegan Tempura": {
                "dish": "Vegan Tempura",
                "time": 30,
                "ingredients": ["1 cup all-purpose flour", "1/4 cup cornstarch", "1/2 tsp baking powder", "1/2 cup cold water", "1/2 cup ice-cold sparkling water", "1 sweet potato (sliced into rounds)", "1 zucchini (sliced into rounds)", "1 bell pepper (sliced)", "1/2 cup shiitake mushrooms", "Vegetable oil (for frying)"],
                "instructions": "In a bowl, mix flour, cornstarch, and baking powder. Slowly add the cold water and sparkling water, stirring gently to create a batter. Heat oil in a deep pan. Dip the vegetables into the batter and fry until golden brown and crispy. Drain on paper towels and serve with soy sauce."
            },
            "Vegan Gyoza": {
                "dish": "Vegan Gyoza",
                "time": 40,
                "ingredients": ["dumpling wrappers", "200g firm tofu (pressed and crumbled)", "1/2 small cabbage (finely chopped)", "2 cloves garlic (minced)", "2 tbsp soy sauce", "1 tbsp sesame oil", "1 tsp grated ginger", "1/4 cup green onions (chopped)", "1 tsp sugar", "1 tsp rice vinegar"],
                "instructions": "To prepare the filling, combine the crumbled tofu, chopped cabbage, minced garlic, grated ginger, soy sauce, sesame oil, sugar, and rice vinegar in a bowl. Mix well. Place a small spoonful of the filling onto each dumpling wrapper. Fold and seal the edges to form a half-moon shape. To cook, heat a non-stick pan with a little oil and place the gyoza in the pan. Cook until the bottoms are golden, then add a splash of water and cover to steam for 5 minutes. Serve with soy sauce or dipping sauce of your choice."
            },
            "Vegan Donburi": {
                "dish": "Vegan Donburi",
                "time": 35,
                "ingredients": ["1 cup rice", "200g firm tofu (cubed)", "2 tbsp soy sauce", "1 tbsp mirin", "1 tbsp rice vinegar", "1/2 cup mixed vegetables (carrots, bell peppers, mushrooms, etc.)", "1 tsp sesame oil", "1-inch piece ginger (grated)", "1 green onion (chopped)", "1 tbsp sesame seeds"],
                "instructions": "Cook the rice according to package instructions. In a pan, heat sesame oil over medium heat and sauté the grated ginger for 1 minute. Add the mixed vegetables and tofu cubes, stir-frying for about 5 minutes until the tofu is golden. Add soy sauce, mirin, rice vinegar, and stir to combine. Let the mixture simmer for another 5 minutes until the flavors meld. Serve the tofu and vegetable mixture over the cooked rice, and garnish with green onions and sesame seeds."
            },
            "Vegan Miso Soup": {
                "dish": "Vegan Miso Soup",
                "time": 20,
                "ingredients": ["2 tbsp miso paste", "200g firm tofu (cubed)", "1/4 cup dried seaweed (wakame)", "2 cups vegetable broth", "2 green onions (chopped)", "1 tsp sesame oil", "1 tsp soy sauce", "1 tsp rice vinegar"],
                "instructions": "In a pot, heat sesame oil over medium heat and sauté the green onions for 1 minute. Add vegetable broth and bring to a simmer. Stir in the miso paste, soy sauce, and rice vinegar, mixing well. Add the tofu and dried seaweed, simmering for 5-7 minutes until heated through. Adjust seasoning to taste with extra soy sauce if needed. Serve hot and enjoy!"
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_fish_recipe(name):
        recipes = {
            "Grilled Salmon": {
                "dish": "Grilled Salmon",
                "time": 30,
                "ingredients": ["2 salmon fillets", "2 tbsp soy sauce", "1 tbsp mirin", "1 tbsp sake", "1 tsp sesame oil", "1 tsp grated ginger", "1 tsp sesame seeds", "1/2 lemon (for serving)"],
                "instructions": "In a small bowl, mix together soy sauce, mirin, sake, sesame oil, and grated ginger. Place the salmon fillets in a shallow dish and pour the marinade over them. Let the salmon marinate for 15-20 minutes. Preheat the grill or a grill pan over medium heat. Grill the salmon fillets for about 4-5 minutes per side, or until cooked to your desired doneness. Serve with a sprinkle of sesame seeds and a wedge of lemon."
            },
            "Saba Shioyaki": {
                "dish": "Saba Shioyaki",
                "time": 25,
                "ingredients": ["2 mackerel fillets", "2 tsp salt", "1/2 lemon (for serving)"],
                "instructions": "Pat the mackerel fillets dry with paper towels. Sprinkle salt evenly on both sides of the fillets and let them sit for 10-15 minutes to allow the salt to draw out moisture. Preheat a grill or grill pan over medium-high heat. Grill the mackerel for about 5-7 minutes per side, until the skin is crispy and the fish is cooked through. Serve with a wedge of lemon for extra flavor."
            },
            "Unagi Donburi": {
                "dish": "Unagi Donburi",
                "time": 35,
                "ingredients": ["2 eel fillets (grilled or broiled)", "2 cups cooked rice", "3 tbsp soy sauce", "2 tbsp mirin", "1 tbsp sake", "1 tbsp sugar", "1 green onion (chopped)", "1 tsp sesame seeds"],
                "instructions": "In a small saucepan, combine soy sauce, mirin, sake, and sugar. Bring the mixture to a simmer over medium heat, stirring until the sugar dissolves and the sauce thickens slightly. Place the cooked rice in serving bowls. Drizzle the eel fillets with the sauce and arrange them over the rice. Garnish with chopped green onions and sesame seeds before serving."
            },
            "Tuna Tataki": {
                "dish": "Tuna Tataki",
                "time": 20,
                "ingredients": ["200g fresh tuna (sashimi-grade, seared)", "2 tbsp soy sauce", "1 tbsp rice vinegar", "1 tsp sesame oil", "1 tsp grated ginger", "1 tbsp sesame seeds", "1 green onion (chopped)"],
                "instructions": "Quick-sear the tuna fillet on all sides in a hot pan with a little oil for about 1-2 minutes until the outside is lightly cooked but the inside remains rare. Allow the tuna to rest for a minute before slicing thinly. In a small bowl, mix together soy sauce, rice vinegar, sesame oil, and grated ginger. Drizzle the sauce over the sliced tuna and garnish with sesame seeds and chopped green onions."
            },
            "Fish Karaage": {
                "dish": "Fish Karaage",
                "time": 30,
                "ingredients": ["300g white fish fillets (such as cod or tilapia)", "1/2 cup flour", "1 tbsp soy sauce", "1 tbsp grated ginger", "1 clove garlic (minced)", "1 egg", "1 tsp sesame oil", "oil for frying", "1/2 lemon (for serving)"],
                "instructions": "Cut the fish fillets into bite-sized pieces. In a bowl, mix soy sauce, grated ginger, minced garlic, egg, and sesame oil. Coat the fish pieces in the mixture and then dredge them in flour. Heat oil in a frying pan over medium heat. Fry the fish pieces in batches until golden brown and crispy, about 3-4 minutes per batch. Serve the crispy fish with a squeeze of lemon."
            },
            "Fish Miso Soup": {
                "dish": "Fish Miso Soup",
                "time": 25,
               "ingredients": ["200g white fish fillets (such as cod or snapper)", "2 tbsp miso paste", "1/2 cup tofu (cubed)", "1/4 cup dried seaweed (wakame)", "3 cups vegetable broth", "1 green onion (chopped)", "1 tsp sesame oil"],
                "instructions": "In a pot, heat sesame oil over medium heat and sauté the green onions for 1 minute. Add vegetable broth and bring to a simmer. Stir in miso paste and mix until fully dissolved. Add the fish fillets, tofu cubes, and dried seaweed. Simmer for about 5-7 minutes, until the fish is cooked through and tender. Adjust seasoning with additional miso paste or soy sauce if needed. Serve hot."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_lamb_recipe(name):
        recipes = {
        "Braised Lamb Shanks": {
            "dish": "Braised Lamb Shanks",
            "time": 90,
            "ingredients": ["2 lamb shanks", "1 large onion (chopped)", "2 cloves garlic (minced)", "2 carrots (chopped)", "2 celery stalks (chopped)", "1 cup red wine", "2 cups beef broth", "2 sprigs rosemary", "2 sprigs thyme", "2 tbsp tomato paste", "1 tbsp olive oil", "salt and pepper to taste"],
            "instructions": "Heat olive oil in a large pot or Dutch oven over medium heat. Season the lamb shanks with salt and pepper and brown them on all sides. Remove the shanks and set them aside. In the same pot, sauté onions, garlic, carrots, and celery until softened. Add tomato paste and cook for another 2 minutes. Pour in red wine and scrape up any browned bits from the bottom of the pot. Add the lamb shanks back to the pot, followed by beef broth, rosemary, and thyme. Bring the mixture to a simmer, then cover and cook in a preheated oven at 350°F (175°C) for about 1.5 hours, or until the lamb is tender. Serve the lamb shanks with the braising liquid."
        },
        "Lamb Katsu": {
            "dish": "Lamb Katsu",
            "time": 45,
            "ingredients": ["500g lamb loin (cut into 1-inch pieces)", "1 cup breadcrumbs", "1 egg", "1/2 cup all-purpose flour", "1 tbsp soy sauce", "1 tbsp mirin", "1 tsp sesame oil", "vegetable oil for frying", "tonkatsu sauce (for serving)"],
            "instructions": "Season the lamb pieces with soy sauce, mirin, and sesame oil. Dip each piece of lamb first into flour, then beaten egg, and finally coat in breadcrumbs. Heat vegetable oil in a deep pan over medium-high heat. Fry the lamb pieces in batches for 3-4 minutes, or until golden brown and cooked through. Remove from the oil and drain on paper towels. Serve with tonkatsu sauce for dipping."
        },
        "Lamb Teriyaki": {
            "dish": "Lamb Teriyaki",
            "time": 30,
            "ingredients": ["500g lamb (sliced into thin strips)", "3 tbsp soy sauce", "2 tbsp mirin", "1 tbsp sake", "1 tbsp sugar", "1 tbsp sesame oil", "1 tsp ginger (grated)", "1 tsp garlic (minced)", "sesame seeds (for garnish)", "green onions (for garnish)"],
            "instructions": "In a small saucepan, combine soy sauce, mirin, sake, and sugar. Bring the mixture to a simmer over medium heat, stirring until the sugar dissolves and the sauce thickens. Heat sesame oil in a pan over medium-high heat. Add the lamb strips and cook for 5-7 minutes until browned. Pour the teriyaki sauce over the cooked lamb and simmer for an additional 2-3 minutes. Serve the lamb over rice, garnished with sesame seeds and green onions."
        },
        "Lamb Donburi": {
            "dish": "Lamb Donburi",
            "time": 45,
            "ingredients": ["500g lamb (sliced)", "2 cups rice (cooked)", "3 tbsp soy sauce", "1 tbsp mirin", "1 tbsp sake", "1 tbsp sugar", "2 eggs (fried)", "2 green onions (chopped)", "sesame seeds (optional)"],
            "instructions": "In a small bowl, combine soy sauce, mirin, sake, and sugar to create the sauce. Heat a pan over medium-high heat and cook the lamb slices for 5-7 minutes until browned. Add the sauce and simmer for an additional 2-3 minutes. Place the cooked rice in bowls and top with the cooked lamb. Fry the eggs sunny-side up and place on top of the lamb. Garnish with chopped green onions and sesame seeds."
        },
        "Lamb Ramen": {
            "dish": "Lamb Ramen",
            "time": 50,
            "ingredients": ["500g lamb (sliced thinly)", "4 cups ramen broth (chicken or vegetable)", "200g ramen noodles", "2 tbsp soy sauce", "1 tbsp miso paste", "2 tbsp sesame oil", "2 green onions (chopped)", "1 soft-boiled egg (optional)", "1 tbsp chili paste (optional)"],
            "instructions": "In a pot, bring the ramen broth to a simmer. Add the sesame oil, soy sauce, and miso paste to the broth, stirring until the miso is dissolved. In a separate pan, quickly sear the lamb slices over medium-high heat for 3-4 minutes until browned. Cook the ramen noodles according to package instructions. Once the noodles are cooked, place them in a bowl and pour the broth over them. Top with the seared lamb, green onions, a soft-boiled egg, and chili paste if desired."
        },
        "Lamb Yakiniku": {
            "dish": "Lamb Yakiniku",
            "time": 40,
            "ingredients": ["500g lamb (thinly sliced)", "3 tbsp soy sauce", "1 tbsp sesame oil", "1 tbsp sugar", "2 cloves garlic (minced)", "1 tsp grated ginger", "1/2 tsp sesame seeds", "1 tbsp green onions (chopped)", "vegetable oil (for grilling)"],
            "instructions": "In a bowl, mix the soy sauce, sesame oil, sugar, garlic, and grated ginger to create the marinade. Add the lamb slices and marinate for 15-20 minutes. Heat a grill or grill pan over medium-high heat and brush with vegetable oil. Grill the lamb slices for 2-3 minutes per side until lightly charred and cooked through. Serve with a sprinkle of sesame seeds and chopped green onions."
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