from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class indian_recipe_API:
    @staticmethod
    def get_chicken_recipe(name):
        recipes = {
            "Butter Chicken": {
                "ingredients": ["chicken", "butter", "cream", "tomato", "spices"],
                "instructions": "Cook chicken in a creamy tomato sauce with spices."
            },
            "Chicken Tikka Masala": {
                "ingredients": ["chicken", "yogurt", "spices", "tomato", "onion"],
                "instructions": "Grill marinated chicken and simmer in a spicy tomato sauce."
            },
            "Chicken Korma": {
                "ingredients": ["chicken", "cream", "yogurt", "cashews", "spices"],
                "instructions": "Cook chicken in a rich and creamy cashew gravy."
            },
            "Chicken Vindaloo": {
                "ingredients": ["chicken", "vinegar", "spices", "potatoes"],
                "instructions": "Cook chicken in a spicy, tangy vinegar-based sauce."
            },
            "Chicken Saag": {
                "ingredients": ["chicken", "spinach", "onions", "garlic", "spices"],
                "instructions": "Cook chicken with spinach and spices."
            },
            "Chicken Biryani": {
                "ingredients": ["chicken", "rice", "yogurt", "spices", "saffron"],
                "instructions": "Cook marinated chicken with rice and aromatic spices."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_beef_recipe(name):
        recipes = {
            "Beef Curry": {
                "ingredients": ["beef", "onions", "garlic", "tomato", "spices"],
                "instructions": "Cook beef in a rich, spiced tomato gravy."
            },
            "Beef Vindaloo": {
                "ingredients": ["beef", "vinegar", "spices", "potatoes"],
                "instructions": "Cook beef in a tangy, spicy gravy with potatoes."
            },
            "Beef Keema": {
                "ingredients": ["beef", "peas", "onions", "garlic", "spices"],
                "instructions": "Cook minced beef with peas and spices."
            },
            "Beef Rogan Josh": {
                "ingredients": ["beef", "yogurt", "garlic", "onions", "spices"],
                "instructions": "Slow-cook beef in a yogurt-based gravy with aromatic spices."
            },
            "Beef Biryani": {
                "ingredients": ["beef", "rice", "yogurt", "spices", "onions"],
                "instructions": "Cook marinated beef with rice and fragrant spices."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_vegan_recipe(name):
        recipes = {
            "Chana Masala": {
                "ingredients": ["chickpeas", "tomato", "onion", "spices"],
                "instructions": "Cook chickpeas in a spicy, tangy tomato gravy."
            },
            "Aloo Gobi": {
                "ingredients": ["potatoes", "cauliflower", "onions", "garlic", "spices"],
                "instructions": "Cook potatoes and cauliflower with spices."
            },
            "Baingan Bharta": {
                "ingredients": ["eggplant", "tomato", "onions", "garlic", "spices"],
                "instructions": "Roast eggplant and cook with tomato and spices."
            },
            "Vegan Tikka Masala": {
                "ingredients": ["tofu", "tomato", "onions", "spices", "cream"],
                "instructions": "Cook tofu in a creamy, spiced tomato sauce."
            },
            "Vegan Biryani": {
                "ingredients": ["tofu", "rice", "spices", "onions", "saffron"],
                "instructions": "Cook tofu with rice and aromatic spices."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_fish_recipe(name):
        recipes = {
            "Fish Curry": {
                "ingredients": ["fish", "coconut milk", "tomato", "spices"],
                "instructions": "Cook fish in a creamy coconut curry sauce."
            },
            "Goan Fish Curry": {
                "ingredients": ["fish", "tamarind", "coconut milk", "spices"],
                "instructions": "Cook fish in a tangy, spicy coconut-based gravy."
            },
            "Fish Tikka": {
                "ingredients": ["fish", "yogurt", "spices", "lemon"],
                "instructions": "Marinate fish in yogurt and spices, then grill."
            },
            "Fish Fry": {
                "ingredients": ["fish", "spices", "flour", "oil"],
                "instructions": "Coat fish in spices and fry until crispy."
            },
            "Masala Fish": {
                "ingredients": ["fish", "onions", "tomato", "garlic", "spices"],
                "instructions": "Cook fish with a spicy, flavorful gravy."
            }
        }
        return recipes.get(name)

    @staticmethod
    def get_lamb_recipe(name):
        recipes = {
            "Lamb Curry": {
                "ingredients": ["lamb", "onions", "tomato", "spices", "garlic"],
                "instructions": "Cook lamb in a spiced tomato gravy."
            },
            "Lamb Rogan Josh": {
                "ingredients": ["lamb", "yogurt", "garlic", "spices", "onions"],
                "instructions": "Slow-cook lamb in a yogurt-based sauce with aromatic spices."
            },
            "Lamb Korma": {
                "ingredients": ["lamb", "cream", "yogurt", "cashews", "spices"],
                "instructions": "Cook lamb in a rich, creamy cashew gravy."
            },
            "Lamb Keema": {
                "ingredients": ["lamb", "peas", "onions", "garlic", "spices"],
                "instructions": "Cook minced lamb with peas and spices."
            },
            "Lamb Biryani": {
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
        return {"message": "Data not found"}, 404


class _ChickenTikkaMasala(Resource):
    def get(self):
        recipe = indian_recipe_API.get_chicken_recipe("Chicken Tikka Masala")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _ChickenKorma(Resource):
    def get(self):
        recipe = indian_recipe_API.get_chicken_recipe("Chicken Korma")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _ChickenVindaloo(Resource):
    def get(self):
        recipe = indian_recipe_API.get_chicken_recipe("Chicken Vindaloo")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _ChickenSaag(Resource):
    def get(self):
        recipe = indian_recipe_API.get_chicken_recipe("Chicken Saag")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _ChickenBiryani(Resource):
    def get(self):
        recipe = indian_recipe_API.get_chicken_recipe("Chicken Biryani")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _BeefCurry(Resource):
    def get(self):
        recipe = indian_recipe_API.get_beef_recipe("Beef Curry")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _BeefVindaloo(Resource):
    def get(self):
        recipe = indian_recipe_API.get_beef_recipe("Beef Vindaloo")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _BeefKeema(Resource):
    def get(self):
        recipe = indian_recipe_API.get_beef_recipe("Beef Keema")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _BeefRoganJosh(Resource):
    def get(self):
        recipe = indian_recipe_API.get_beef_recipe("Beef Rogan Josh")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _BeefBiryani(Resource):
    def get(self):
        recipe = indian_recipe_API.get_beef_recipe("Beef Biryani")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _ChanaMasala(Resource):
    def get(self):
        recipe = indian_recipe_API.get_vegan_recipe("Chana Masala")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _AlooGobi(Resource):
    def get(self):
        recipe = indian_recipe_API.get_vegan_recipe("Aloo Gobi")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _BainganBharta(Resource):
    def get(self):
        recipe = indian_recipe_API.get_vegan_recipe("Baingan Bharta")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _VeganTikkaMasala(Resource):
    def get(self):
        recipe = indian_recipe_API.get_vegan_recipe("Vegan Tikka Masala")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _VeganBiryani(Resource):
    def get(self):
        recipe = indian_recipe_API.get_vegan_recipe("Vegan Biryani")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _FishCurry(Resource):
    def get(self):
        recipe = indian_recipe_API.get_fish_recipe("Fish Curry")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _GoanFishCurry(Resource):
    def get(self):
        recipe = indian_recipe_API.get_fish_recipe("Goan Fish Curry")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _FishTikka(Resource):
    def get(self):
        recipe = indian_recipe_API.get_fish_recipe("Fish Tikka")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _FishFry(Resource):
    def get(self):
        recipe = indian_recipe_API.get_fish_recipe("Fish Fry")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _MasalaFish(Resource):
    def get(self):
        recipe = indian_recipe_API.get_fish_recipe("Masala Fish")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _LambCurry(Resource):
    def get(self):
        recipe = indian_recipe_API.get_lamb_recipe("Lamb Curry")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _LambRoganJosh(Resource):
    def get(self):
        recipe = indian_recipe_API.get_lamb_recipe("Lamb Rogan Josh")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _LambKorma(Resource):
    def get(self):
        recipe = indian_recipe_API.get_lamb_recipe("Lamb Korma")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _LambKeema(Resource):
    def get(self):
        recipe = indian_recipe_API.get_lamb_recipe("Lamb Keema")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404


class _LambBiryani(Resource):
    def get(self):
        recipe = indian_recipe_API.get_lamb_recipe("Lamb Biryani")
        if recipe:
            return jsonify(recipe)
        return {"message": "Data not found"}, 404

api.add_resource(_ButterChicken, '/butter_chicken')
api.add_resource(_ChickenTikkaMasala, '/chicken_tikka_masala')
api.add_resource(_ChickenKorma, '/chicken_korma')
api.add_resource(_ChickenVindaloo, '/chicken_vindaloo')
api.add_resource(_ChickenSaag, '/chicken_saag')
api.add_resource(_ChickenBiryani, '/chicken_biryani')

api.add_resource(_BeefCurry, '/beef_curry')
api.add_resource(_BeefVindaloo, '/beef_vindaloo')
api.add_resource(_BeefKeema, '/beef_keema')
api.add_resource(_BeefRoganJosh, '/beef_rogan_josh')
api.add_resource(_BeefBiryani, '/beef_biryani')

api.add_resource(_ChanaMasala, '/chana_masala')
api.add_resource(_AlooGobi, '/aloo_gobi')
api.add_resource(_BainganBharta, '/baingan_bharta')
api.add_resource(_VeganTikkaMasala, '/vegan_tikka_masala')
api.add_resource(_VeganBiryani, '/vegan_biryani')

api.add_resource(_FishCurry, '/fish_curry')
api.add_resource(_GoanFishCurry, '/goan_fish_curry')
api.add_resource(_FishTikka, '/fish_tikka')
api.add_resource(_FishFry, '/fish_fry')
api.add_resource(_MasalaFish, '/masala_fish')

api.add_resource(_LambCurry, '/lamb_curry')
api.add_resource(_LambRoganJosh, '/lamb_rogan_josh')
api.add_resource(_LambKorma, '/lamb_korma')
api.add_resource(_LambKeema, '/lamb_keema')
api.add_resource(_LambBiryani, '/lamb_biryani')


indian_recipe_api_instance = indian_recipe_API()