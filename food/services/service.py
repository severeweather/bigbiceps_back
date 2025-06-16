from ..forms import FoodItemForm
from ..repositories.repository import *
from ..exceptions.exeptions import IDNotFound, InvalidReference, MissingField, AlreadyExists


class NutrientService:

    @staticmethod
    def get_all():
        return NutrientRepository.get_all()
    
    @staticmethod
    def get_by_id(id):
        try:
            return NutrientRepository.get_by_id(id)
        except IDNotFound as e:
            raise InvalidReference(f"Invalid reference {str(e)}")
   
    @staticmethod
    def get_form():
        return {
            "note": "Expecting list of key-value pairs with following structure. Structure: {name: unit}, where both 'name' and 'unit' are strings. Example: {'protein': 'g'}.",
        }

    @staticmethod
    def post_form(nutrients):
        for key, value in nutrients.items():
            try:
                NutrientRepository.create(key.capitalize(), value)
            except AlreadyExists:
                continue
        

class FoodCategoryService:

    @staticmethod
    def get_all():
        return FoodCategoryRepository.get_all()
    
    @staticmethod
    def get_by_id(id):
        try:
            return FoodCategoryRepository.get_by_id(id)
        except IDNotFound as e:
            raise InvalidReference(f"Invalid reference {str(e)}")
    
    @staticmethod
    def get_form():
        return {
            "note": "Expecting list 'categories' of values type string."
        }
    
    @staticmethod
    def post_form(categories):
        for category in categories:
            try:
                FoodCategoryRepository.create(category.capitalize())
            except AlreadyExists:
                continue
            
        

class FoodCuisineService:

    @staticmethod
    def get_all():
        return FoodCuisineRepository.get_all()
    
    @staticmethod
    def get_by_id(id):
        try:
            return FoodCuisineRepository.get_by_id(id)
        except IDNotFound as e:
            raise InvalidReference(f"Invalid reference {str(e)}")

    @staticmethod
    def get_form():
        return {
            "note": "Expecting list 'cuisines' of values type string."
        }
    
    @staticmethod
    def post_form(cuisines):
        for cuisine in cuisines:
            try:
                FoodCuisineRepository.create(cuisine.capitalize())
            except AlreadyExists:
                continue



class FoodItemService:
    @staticmethod
    def get_by_id(id):
        try:
            return FoodItemRepository.get_by_id(id)
        except IDNotFound as e:
            raise InvalidReference(f"Invalid reference {e}")
        
    @staticmethod
    def get_all_ingredients():
        return FoodItemRepository.get_all(food_type="ingredient")
    
    @staticmethod
    def get_all_dishes():
        return FoodItemRepository.get_all(food_type="dish")
    
    @staticmethod
    def get_all_meals():
        return FoodItemRepository.get_all(food_type="meal")

    @staticmethod
    def get_form(food_type):
        return {
            "form": FoodItemForm().Meta.fields,
            "type": food_type,
        }

    @staticmethod
    def post_form(request_user, food_type, form_data):
        form = FoodItemForm(form_data)
        if form.is_valid():
            saved = form.save(commit=False)
            saved.type = food_type
            saved.created_by = request_user
            saved.save()
            return saved.id
        else:
            raise ValueError("Invalid form.")


class FoodItemNutrientService:

    @staticmethod
    def validate_amount(amount):
        try:
            amount = float(amount)
        except ValueError:
            return 0

        if amount < 0 or amount > 10000:
            raise ValueError("Amount must be an integer within interval [0-10000]")
        return amount

    @staticmethod
    def get_food_item_nutrients(id):
        try:
            return FoodItemNutrientRepository.get_food_item_nutrients(id)
        except IDNotFound as e:
            raise InvalidReference(f"Invalid reference {str(e)}")

    @staticmethod
    def get_form():
        nutrients = NutrientService.get_all()
        return {
            "note": "Expecting list of key-value pairs, where key is nutrient's id and value is amount in nutrient's units",
            "nutrients": nutrients
        }

    @staticmethod
    def post_form(nutrients, id):
        food_item = FoodItemService.get_by_id(id)
        
        valid_nutrients = NutrientService.get_all()

        for v in valid_nutrients:
            if v["id"] not in nutrients:
                raise MissingField(f"Nutrient field '{v["name"]}' is missing")

            try:
                nutrient = NutrientService.get_by_id(v["id"])
                amount = FoodItemNutrientService.validate_amount(nutrients[v["id"]])
            except (IDNotFound, ValueError) as e:
                raise InvalidReference(f"Invalid nutrient data: {e}")
        
            try:
                FoodItemNutrientRepository.create(food_item, nutrient, amount)
            except AlreadyExists:
                raise InvalidReference(f"Nutrient '{nutrient.id}' already exists for FoodItem {food_item.id}")
            
    @staticmethod
    def exists(id):
        try:
            return FoodItemNutrientRepository.exists(id)
        except IDNotFound as e:
            raise InvalidReference(str(e))


class FoodItemCategoryService:

    @staticmethod
    def get_form():
        categories = FoodCategoryService.get_all()
        return {
            "note": "Expecting list 'categories' of category id's",
            "categories": categories
            }

    @staticmethod
    def post_form(categories, id):
        food_item = FoodItemService.get_by_id(id)

        valid_categories = []

        for category_id in categories:
            try:
                _ = FoodCategoryService.get_by_id(category_id)
                valid_categories.append(_)
            except IDNotFound as e:
                raise InvalidReference(f"Invalid category data: {e}")
        
        for valid_category in valid_categories:
            try:
                FoodItemCategoryRepository.create(food_item, valid_category)
            except AlreadyExists:
                continue

        return
    
    @staticmethod
    def exists(id):
        try:
            FoodItemCategoryRepository.exists(id)
        except IDNotFound as e:
            raise InvalidReference(str(e))


class FoodItemCuisineService:

    @staticmethod
    def get_form():
        cuisines = FoodCuisineService.get_all()
        return {
            "note": "Expecting list 'cuisines' of cuisine id's",
            "cuisines": cuisines
        }

    @staticmethod
    def post_form(cuisines, id):
        food_item = FoodItemService.get_by_id(id)
    
        valid_cuisines = []

        for cuisine_id in cuisines:
            try:
                _ = FoodCuisineService.get_by_id(cuisine_id)
                valid_cuisines.append(_)
            except IDNotFound as e:
                raise InvalidReference(f"Invalid cuisine data: {e}")
        
        for valid_cuisine in valid_cuisines:
            try:
                FoodItemCuisineRepository.create(food_item, valid_cuisine)
            except AlreadyExists:
                continue

        return
    
    @staticmethod
    def exists(id):
        try:
            FoodItemCuisineRepository.exists(id)
        except IDNotFound as e:
            raise InvalidReference(str(e))


class FoodItemChildService:

    @staticmethod
    def validate_amount(amount):
        amount = int(amount)
        if amount < 0 or amount > 100:
            raise ValueError("Amount must be an integer within interval [1-100]")
        return amount
    
    
    @staticmethod
    def get_form(id):
        food_item = FoodItemService.get_by_id(id)
        if food_item.type == "dish":
            food_type = ["ingredient"]
        elif food_item.type == "meal":
            food_type = ["ingredient", "dish"]
            
        return {
            "note": "Expecting a dict with following structure",
            "note 2": "amount type 'float' min 0.1 max 100",
            "structure": [
                {
                    "uuid": "amount"
                }
            ]
        }
        

    @staticmethod
    def post_form(parent_id, children_list):
        parent = FoodItemService.get_by_id(parent_id) 

        good_children = {}

        for id, amount in children_list.items():
            try:
                good_child = FoodItemService.get_by_id(id)
                amount = FoodItemChildService.validate_amount(amount)
                good_children[id] = amount

            except (IDNotFound, KeyError, ValueError) as e:
                raise InvalidReference(f"Invalid reference: {str(e)}")
        
        parent_nutrients = {}

        for id1, amount1 in good_children.items():
            child_nutrients = FoodItemNutrientService.get_food_item_nutrients(id1)

            for id2, amount2 in child_nutrients.items():
                amount = round(float(amount2) * float(amount1), 2)

                if id2 in parent_nutrients:
                    parent_nutrients[str(id2)] += amount
                else:
                    parent_nutrients[str(id2)] = amount

        FoodItemNutrientService.post_form(parent_nutrients, parent_id)

        for id, amount in good_children.items():
            good_child = FoodItemService.get_by_id(id)
            FoodItemChildRepository.add(parent, good_child, amount)