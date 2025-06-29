class NutrientSerializer:
    @staticmethod
    def to_dict(obj):
        return {
            "id": str(obj.id),
            "name": str(obj.name),
            "unit": str(obj.unit),
        }