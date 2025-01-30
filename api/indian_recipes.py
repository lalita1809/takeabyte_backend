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
                "ingredients": ["500g chicken (boneless, skinless, cut into 1-inch pieces)", "100g unsalted butter", "200ml heavy cream", "400g diced tomatoes", "2 tsp garam masala", "1 tsp ground cumin", "1 tsp ground coriander", "1/2 tsp turmeric", "1 tsp chili powder", "1/2 tsp salt"],
                "instructions": "Melt the butter in a large pan over medium heat. Add the chicken pieces and sear until golden brown on all sides. In a separate pan, cook diced tomatoes until soft, then add the cream, garam masala, cumin, coriander, turmeric, chili powder, and salt. Simmer the sauce for 10 minutes to thicken. Add the seared chicken and cook for another 10-15 minutes. Serve with naan or rice."
            },
            "Chicken Tikka Masala": {
                "dish": "Chicken Tikka Masala",
                "time": 50,
                "ingredients": ["500g chicken (boneless, skinless, cut into 1-inch pieces)", "200g plain yogurt", "2 tsp ground coriander", "1 tsp ground cumin", "1/2 tsp turmeric", "1 tsp garam masala", "1 tsp paprika", "1 large onion (chopped)", "2 tomatoes (blended)", "3 cloves garlic (minced)", "1-inch piece ginger (grated)"],
                "instructions": "In a bowl, mix yogurt with coriander, cumin, turmeric, garam masala, and paprika. Marinate the chicken in this mixture for at least 2 hours. Grill or pan-sear the chicken pieces until cooked through. In a large pan, sauté onions, garlic, and ginger until soft. Add blended tomatoes and cook for 10 minutes. Add the cooked chicken and simmer for 10 more minutes. Adjust salt to taste and serve with rice or naan."
            },
            "Chicken Korma": {
                "dish": "Chicken Korma",
                "time": 70,
                "ingredients": ["500g chicken (boneless, skinless, cut into 1-inch pieces)", "100g heavy cream", "100g plain yogurt", "50g cashews", "1 large onion (finely chopped)", "3 cloves garlic (minced)", "1-inch piece ginger (grated)", "2 tsp ground coriander", "1 tsp ground cumin", "1/2 tsp ground cardamom", "1/2 tsp ground cinnamon", "2 tbsp vegetable oil"],
                "instructions": "Grind the cashews into a fine powder. Heat oil in a pan and sauté the onions, garlic, and ginger until golden brown. Add the ground coriander, cumin, cardamom, and cinnamon, cooking for 2 minutes to release the flavors. Add the chicken and brown it on all sides. Stir in yogurt, cream, and cashew powder, and cook for 15-20 minutes until the sauce thickens and the chicken is cooked through. Garnish with chopped cilantro and serve with basmati rice."
            },
            "Chicken Vindaloo": {
                "dish": "Chicken Vindaloo",
                "time": 60,
                "ingredients": ["500g chicken (boneless, skinless, cut into pieces)", "2 tbsp vinegar", "3 medium potatoes (peeled and diced)", "1 large onion (chopped)", "3 cloves garlic (minced)", "1-inch piece ginger (grated)", "2 tsp ground mustard seeds", "1 tsp ground cumin", "1 tsp chili powder", "2 tsp turmeric", "1 tsp sugar", "1/2 tsp salt"],
                "instructions": "In a large pan, sauté onions, garlic, and ginger until soft. Add mustard seeds, cumin, chili powder, turmeric, and cook for 2 minutes. Add chicken and brown on all sides. Stir in vinegar, sugar, and potatoes, and cook for 10 minutes. Add enough water to cover the ingredients, bring to a boil, then simmer for 20-25 minutes until the potatoes are tender and the sauce has thickened. Serve with rice or naan."
            },
            "Chicken Saag": {
                "dish": "Chicken Saag",
                "time": 55,
                "ingredients": ["500g chicken (boneless, skinless, cut into pieces)", "300g fresh spinach (or 250g frozen spinach)", "1 large onion (chopped)", "3 cloves garlic (minced)", "1-inch piece ginger (grated)", "1 tsp ground cumin", "1 tsp ground coriander", "1/2 tsp garam masala", "1/2 tsp chili powder", "2 tbsp vegetable oil", "1/2 cup water"],
                "instructions": "Heat oil in a pan and sauté onions, garlic, and ginger until softened. Add cumin, coriander, garam masala, and chili powder, and cook for 1-2 minutes. Add chicken pieces and cook until browned. Add spinach and cook until wilted (if using fresh spinach). Pour in water and simmer for 20 minutes until the chicken is cooked through and the sauce thickens. Serve with naan or rice."
            },
            "Chicken Biryani": {
                "dish": "Chicken Biryani",
                "time": 90,
                "ingredients": ["500g chicken (bone-in pieces)", "1 cup basmati rice", "1 large onion (thinly sliced)", "3 cloves garlic (minced)", "1-inch piece ginger (grated)", "200g plain yogurt", "1/2 tsp saffron", "2 tsp ground cumin", "1 tsp ground cinnamon", "3-4 cloves", "2 bay leaves", "2 tbsp vegetable oil", "1 1/2 cups water", "salt to taste"],
                "instructions": "Marinate the chicken in yogurt, saffron, cumin, cinnamon, cloves, and salt for 2 hours. Heat oil in a pan and fry the onions until golden brown. Remove half of the fried onions for garnishing. In the same pan, sauté garlic and ginger until fragrant. Add the marinated chicken and cook until browned. In a separate pot, cook rice with water and bay leaves until 80% cooked. Layer the rice and chicken in a pot, and steam for 20-25 minutes until fully cooked. Garnish with fried onions and serve with raita."
            }
        }
        return recipes.get(name)
    
    @staticmethod
    def get_beef_recipe(name):
        recipes = {
            "Beef Curry": {
                "dish": "Beef Curry",
                "time": 60,
                "ingredients": ["500g beef (cut into cubes)", "2 large onions (chopped)", "4 cloves garlic (minced)", "1-inch piece ginger (grated)", "400g diced tomatoes", "2 tsp ground coriander", "1 tsp ground cumin", "1/2 tsp turmeric", "1 tsp chili powder", "1 tsp garam masala", "2 tbsp vegetable oil", "1/2 cup water", "salt to taste"],
                "instructions": "Heat oil in a pot and sauté onions, garlic, and ginger until softened. Add ground coriander, cumin, turmeric, chili powder, and garam masala, and cook for 2 minutes. Add beef cubes and brown on all sides. Add diced tomatoes, water, and salt. Bring to a boil, then simmer for 45 minutes until the beef is tender. Serve with rice or naan."
            },
            "Beef Vindaloo": {
                "dish": "Beef Vindaloo",
                "time": 70,
                "ingredients": ["500g beef (cut into cubes)", "2 tbsp vinegar", "2 large potatoes (peeled and diced)", "1 large onion (chopped)", "3 cloves garlic (minced)", "1-inch piece ginger (grated)", "2 tsp mustard seeds", "1 tsp ground cumin", "2 tsp chili powder", "1 tsp turmeric", "2 tbsp vegetable oil", "1/2 tsp salt", "1/2 cup water"],
                "instructions": "In a pot, heat oil and sauté onions, garlic, and ginger until softened. Add mustard seeds, cumin, chili powder, and turmeric, cooking for 2 minutes. Add beef and brown on all sides. Stir in vinegar, potatoes, water, and salt. Bring to a boil, then simmer for 45 minutes until the beef is tender and potatoes are cooked. Serve with rice or naan."
            },
            "Beef Keema": {
                "dish": "Beef Keema",
                "time": 50,
                "ingredients": ["500g ground beef", "1 cup peas", "1 large onion (chopped)", "3 cloves garlic (minced)", "1-inch piece ginger (grated)", "2 tomatoes (blended)", "2 tsp ground coriander", "1 tsp ground cumin", "1/2 tsp garam masala", "2 tbsp vegetable oil", "salt to taste"],
                "instructions": "Heat oil in a pan and sauté onions, garlic, and ginger until softened. Add ground coriander, cumin, and garam masala, and cook for 1-2 minutes. Add ground beef and cook until browned. Stir in blended tomatoes, peas, and salt. Simmer for 20 minutes until the meat is cooked through and the sauce thickens. Serve with roti or rice."
            },
            "Beef Rogan Josh": {
                "dish": "Beef Rogan Josh",
                "time": 90,
                "ingredients": ["500g beef (cut into cubes)", "1 cup yogurt", "2 onions (chopped)", "3 cloves garlic (minced)", "1-inch piece ginger (grated)", "2 tsp ground cumin", "2 tsp ground coriander", "2 tsp garam masala", "1 tsp chili powder", "2 tbsp vegetable oil", "1/2 tsp salt", "1/2 cup water"],
                "instructions": "Heat oil in a pot and sauté onions, garlic, and ginger until softened. Add ground cumin, coriander, garam masala, and chili powder, cooking for 2 minutes. Add beef and brown on all sides. Stir in yogurt and water, bring to a boil, then reduce heat and simmer for 60 minutes, until beef is tender. Serve with rice or naan."
            },
            "Beef Biryani": {
                "dish": "Beef Biryani",
                "time": 100,
                "ingredients": ["500g beef (bone-in pieces)", "1 1/2 cups basmati rice", "2 large onions (thinly sliced)", "3 cloves garlic (minced)", "1-inch piece ginger (grated)", "200g yogurt", "2 tsp ground cumin", "1 tsp ground coriander", "2 bay leaves", "2 cinnamon sticks", "3-4 cloves", "2 tbsp vegetable oil", "2 1/2 cups water", "salt to taste"],
                "instructions": "Marinate beef in yogurt, cumin, coriander, and salt for 2 hours. Heat oil in a pan and fry onions until golden brown. Remove half for garnishing. In the same pan, sauté garlic and ginger until fragrant. Add the marinated beef and cook until browned. In a separate pot, cook rice with bay leaves, cinnamon sticks, cloves, and water until 80% cooked. Layer the rice and beef, then steam for 25 minutes until fully cooked. Garnish with fried onions and serve with raita."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_vegan_recipe(name):
        recipes = {
            "Chana Masala": {
                "dish": "Chana Masala",
                "time": 45,
                "ingredients": ["2 cups cooked chickpeas", "2 large tomatoes (chopped)", "1 large onion (chopped)", "4 cloves garlic (minced)", "1-inch piece ginger (grated)", "2 tsp ground coriander", "1 tsp ground cumin", "1/2 tsp garam masala", "1 tsp chili powder", "1/2 tsp turmeric", "2 tbsp vegetable oil", "salt to taste"],
                "instructions": "Heat oil in a pot and sauté onions, garlic, and ginger until soft. Add coriander, cumin, garam masala, chili powder, and turmeric, and cook for 2 minutes. Stir in tomatoes and cook until softened. Add cooked chickpeas, salt, and a little water to create a thick gravy. Simmer for 20 minutes, then serve with rice or naan."
            },
            "Aloo Gobi": {
                "dish": "Aloo Gobi",
                "time": 40,
                "ingredients": ["2 large potatoes (peeled and cubed)", "1 medium cauliflower (cut into florets)", "1 large onion (chopped)", "4 cloves garlic (minced)", "1-inch piece ginger (grated)", "2 tsp ground cumin", "1 tsp ground coriander", "1/2 tsp turmeric", "1/2 tsp chili powder", "2 tbsp vegetable oil", "salt to taste"],
                "instructions": "Heat oil in a pan and sauté onions, garlic, and ginger until softened. Add cumin, coriander, turmeric, and chili powder, and cook for 2 minutes. Add potatoes and cauliflower, stir well to coat with spices. Add salt and a little water, then cover and cook for 20 minutes until vegetables are tender. Serve with rice or roti."
            },
            "Baingan Bharta": {
                "dish": "Baingan Bharta",
                "time": 50,
                "ingredients": ["2 large eggplants (roasted)", "2 large tomatoes (chopped)", "1 large onion (chopped)", "4 cloves garlic (minced)", "1-inch piece ginger (grated)", "2 tsp ground cumin", "1 tsp ground coriander", "1/2 tsp garam masala", "2 tbsp vegetable oil", "salt to taste"],
                "instructions": "Roast the eggplants over an open flame or in the oven until the skin is charred. Peel the skin off and mash the flesh. Heat oil in a pan and sauté onions, garlic, and ginger until soft. Add cumin, coriander, and garam masala, then cook for 2 minutes. Stir in chopped tomatoes and cook until soft. Add mashed eggplant and cook for 15 minutes, adjusting salt to taste. Serve with roti or rice."
            },
            "Vegan Tikka Masala": {
                "dish": "Vegan Tikka Masala",
                "time": 55,
                "ingredients": ["400g tofu (pressed and cut into cubes)", "200g diced tomatoes", "1 large onion (chopped)", "4 cloves garlic (minced)", "1-inch piece ginger (grated)", "2 tsp ground cumin", "1 tsp ground coriander", "1/2 tsp garam masala", "2 tbsp vegetable oil", "1/2 cup coconut cream", "salt to taste"],
                "instructions": "Pan-fry tofu cubes until golden brown. Heat oil in a pan and sauté onions, garlic, and ginger until soft. Add cumin, coriander, garam masala, and cook for 2 minutes. Stir in tomatoes and cook for 10 minutes. Add fried tofu and coconut cream, and simmer for another 15 minutes. Serve with rice or naan."
            },
            "Vegan Biryani": {
                "dish": "Vegan Biryani",
                "time": 90,
                "ingredients": ["200g tofu (pressed and cut into cubes)", "1 1/2 cups basmati rice", "2 large onions (thinly sliced)", "3 cloves garlic (minced)", "1-inch piece ginger (grated)", "200g mixed vegetables (peas, carrots, potatoes)", "2 tsp ground cumin", "1 tsp ground coriander", "1/2 tsp saffron", "2 bay leaves", "2 cinnamon sticks", "3-4 cloves", "2 tbsp vegetable oil", "2 1/2 cups water", "salt to taste"],
                "instructions": "Sauté onions, garlic, and ginger in oil until golden. Add mixed vegetables and sauté for 5 more minutes. Stir in rice, cumin, coriander, saffron, bay leaves, cinnamon, and cloves. Add water, salt, and cook until rice is tender. In a separate pan, fry tofu cubes until golden. Mix tofu into the rice, cover, and cook for an additional 10-15 minutes. Serve with raita."
            }
        }
        return recipes.get(name)
    
    @staticmethod
    def get_fish_recipe(name):
        recipes = {
            "Fish Curry": {
                "dish": "Fish Curry",
                "time": 50,
                "ingredients": ["500g fish fillets (cut into pieces)", "1 can coconut milk", "2 tomatoes (chopped)", "1 large onion (chopped)", "4 cloves garlic (minced)", "1-inch piece ginger (grated)", "2 tsp ground cumin", "1 tsp turmeric", "1 tsp chili powder", "2 tbsp vegetable oil", "salt to taste"],
                "instructions": "Heat oil in a pan and sauté onions, garlic, and ginger until soft. Add cumin, turmeric, and chili powder, and cook for 2 minutes. Stir in tomatoes and cook until soft. Add coconut milk and bring to a boil. Add fish and simmer for 10-15 minutes until fish is cooked. Serve with rice."
            },
            "Goan Fish Curry": {
                "dish": "Goan Fish Curry",
                "time": 60,
                "ingredients": ["500g fish fillets", "1 tbsp tamarind paste", "1 can coconut milk", "2 tsp ground cumin", "1 tsp ground coriander", "1 tsp turmeric", "2 tbsp vegetable oil", "1 large onion (chopped)", "3 cloves garlic (minced)", "1-inch piece ginger (grated)", "salt to taste"],
                "instructions": "In a pan, heat oil and sauté onions, garlic, and ginger until soft. Add cumin, coriander, turmeric, and cook for 2 minutes. Stir in coconut milk, tamarind paste, and salt. Bring to a boil, then simmer for 5 minutes. Add fish fillets and cook for another 15 minutes until tender. Serve with rice."
            },
            "Fish Tikka": {
                "dish": "Fish Tikka",
                "time": 40,
                "ingredients": ["500g fish fillets (cut into cubes)", "1/2 cup yogurt", "2 tsp ground cumin", "1 tsp ground coriander", "1/2 tsp turmeric", "1/2 tsp chili powder", "2 tbsp lemon juice", "2 tbsp vegetable oil", "salt to taste"],
                "instructions": "In a bowl, mix yogurt, cumin, coriander, turmeric, chili powder, lemon juice, vegetable oil, and salt. Add fish cubes and marinate for at least 30 minutes. Preheat grill or oven to medium-high heat and grill fish for 8-10 minutes, turning once, until cooked through. Serve with a drizzle of lemon juice and fresh cilantro."
            },
            "Fish Fry": {
                "dish": "Fish Fry",
                "time": 30,
                "ingredients": ["500g fish fillets", "1/2 cup flour", "1 tsp ground cumin", "1 tsp chili powder", "1/2 tsp turmeric", "2 tbsp vegetable oil", "salt to taste"],
                "instructions": "Mix flour, cumin, chili powder, turmeric, and salt in a bowl. Coat fish fillets with the flour mixture. Heat oil in a pan and fry the fish for 3-4 minutes per side until crispy and golden brown. Drain on paper towels. Serve with lime wedges and fresh herbs."
            },
            "Masala Fish": {
                "dish": "Masala Fish",
                "time": 50,
                "ingredients": ["500g fish fillets", "1 large onion (chopped)", "2 tomatoes (chopped)", "4 cloves garlic (minced)", "1-inch piece ginger (grated)", "2 tsp ground cumin", "1 tsp ground coriander", "1 tsp garam masala", "2 tbsp vegetable oil", "salt to taste"],
                "instructions": "Heat oil in a pan and sauté onions, garlic, and ginger until soft. Add cumin, coriander, and garam masala, and cook for 2 minutes. Stir in tomatoes and cook until soft. Add fish fillets, season with salt, and simmer for 10-15 minutes until fish is cooked through. Serve with rice or naan."
            }
        }
        return recipes.get(name)
    
    @staticmethod
    def get_lamb_recipe(name):
        recipes = {
            "Lamb Curry": {
                "dish": "Lamb Curry",
                "time": 60,
                "ingredients": ["500g lamb (cut into cubes)", "1 large onion (chopped)", "4 cloves garlic (minced)", "1-inch piece ginger (grated)", "2 large tomatoes (chopped)", "1 tsp ground coriander", "1 tsp ground cumin", "1 tsp chili powder", "1 tsp garam masala", "2 tbsp vegetable oil", "1/2 cup water", "salt to taste"],
                "instructions": "Heat oil in a pot and sauté onions, garlic, and ginger until softened. Add ground coriander, cumin, chili powder, and garam masala, cooking for 2 minutes. Add lamb cubes and brown on all sides. Stir in chopped tomatoes, water, and salt. Bring to a boil, then simmer for 45 minutes until the lamb is tender. Serve with rice or naan."
            },
            "Lamb Rogan Josh": {
                "dish": "Lamb Rogan Josh",
                "time": 90,
                "ingredients": ["500g lamb (cut into cubes)", "1 cup yogurt", "2 onions (chopped)", "4 cloves garlic (minced)", "1-inch piece ginger (grated)", "1 tsp ground cumin", "1 tsp ground coriander", "1 tsp garam masala", "1/2 tsp ground cinnamon", "2 tbsp vegetable oil", "1/2 cup water", "salt to taste"],
                "instructions": "Heat oil in a pot and sauté onions, garlic, and ginger until softened. Add cumin, coriander, garam masala, and cinnamon, cooking for 2 minutes. Add lamb cubes and brown on all sides. Stir in yogurt, water, and salt. Bring to a boil, then simmer for 1 hour, or until lamb is tender. Serve with rice or naan."
            },
            "Lamb Korma": {
                "dish": "Lamb Korma",
                "time": 70,
                "ingredients": ["500g lamb (cut into cubes)", "1 large onion (chopped)", "4 cloves garlic (minced)", "1-inch piece ginger (grated)", "1/4 cup cashews", "1/4 cup yogurt", "2 tbsp cream", "1 tsp ground coriander", "1 tsp ground cumin", "1/2 tsp cinnamon", "2 tbsp vegetable oil", "1/2 cup water", "salt to taste"],
                "instructions": "Heat oil in a pot and sauté onions, garlic, and ginger until soft. Add ground coriander, cumin, and cinnamon, cooking for 2 minutes. Add lamb cubes and brown on all sides. Stir in cashews, yogurt, cream, and water. Bring to a boil, then simmer for 1 hour, or until lamb is tender. Serve with rice or naan."
            },
            "Lamb Keema": {
                "dish": "Lamb Keema",
                "time": 50,
                "ingredients": ["500g ground lamb", "1 large onion (chopped)", "4 cloves garlic (minced)", "1-inch piece ginger (grated)", "1 cup peas", "1 tsp ground cumin", "1 tsp ground coriander", "1/2 tsp chili powder", "1/2 tsp turmeric", "2 tbsp vegetable oil", "1/2 cup water", "salt to taste"],
                "instructions": "Heat oil in a pan and sauté onions, garlic, and ginger until softened. Add cumin, coriander, chili powder, and turmeric, cooking for 2 minutes. Stir in ground lamb and cook until browned. Add peas, water, and salt. Simmer for 10 minutes, stirring occasionally. Serve with rice or naan."
            },
            "Lamb Biryani": {
                "dish": "Lamb Biryani",
                "time": 100,
                "ingredients": ["500g lamb (cut into cubes)", "2 cups basmati rice", "1 large onion (sliced)", "4 cloves garlic (minced)", "1-inch piece ginger (grated)", "1/2 cup yogurt", "1 tsp garam masala", "1 tsp ground cumin", "1/2 tsp turmeric", "2 tbsp vegetable oil", "1/4 cup saffron (soaked in 2 tbsp warm milk)", "2 cups water", "salt to taste"],
                "instructions": "In a pan, heat oil and sauté onions, garlic, and ginger until soft. Add garam masala, cumin, and turmeric, and cook for 2 minutes. Add lamb cubes and brown on all sides. Stir in yogurt and cook until the lamb is browned. In a separate pot, cook basmati rice with water, saffron, and salt. Layer the rice over the lamb in the pot and cover. Simmer for 45 minutes on low heat. Serve with raita or salad."
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