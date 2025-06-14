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
    def post_form(name, unit):
        if not name or not unit:
            raise ValueError("'name' or 'unit' value is missing")
        
        try:
            NutrientRepository.create(name, unit)
            return
        except AlreadyExists:
            raise InvalidReference(f"Nutrient '${name}' already exists")
        

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
    def post_form(name):
        try:
            FoodCategoryRepository.create(name)
            return
        except AlreadyExists:
            raise InvalidReference(f"Category '${name}' already exists")
        

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
    def post_form(name):
        try:
            FoodCuisineRepository.create(name)
            return
        except AlreadyExists:
            raise InvalidReference(f"Cuisine '${name}' already exists")



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

        if amount < 0 or amount > 100:
            raise ValueError("Amount must be an integer within interval [0-100]")
        return amount

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
            if str(v["id"]) not in nutrients:
                raise MissingField(f"Nutrient field '{v["name"]}' is missing")

            try:
                nutrient = NutrientService.get_by_id(v["id"])
                amount = FoodItemNutrientService.validate_amount(nutrients[str(v["id"])][0])
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
            "note": "Expecting a list of dicts with following structure",
            "structure": [
                {
                    "id": {"type": "uuid", "food_type": food_type},
                    "amount": {"type": "float", "min": 0.1, "max": 100}
                }
            ]
        }
        

    @staticmethod
    def post_form(parent_id, children_list):
        parent = FoodItemService.get_by_id(parent_id) 

        good_children = []

        for child in children_list:
            try:
                good_child = FoodItemService.get_by_id(child["id"])
                amount = FoodItemChildService.validate_amount(child["amount"])
                good_children.append({
                    "child": good_child,
                    "amount": amount,
                })
            except (IDNotFound, KeyError, ValueError) as e:
                raise InvalidReference(f"Invalid reference: {str(e)}")
        
        for good_child in good_children:
            FoodItemChildRepository.add(parent, good_child["child"], good_child["amount"])