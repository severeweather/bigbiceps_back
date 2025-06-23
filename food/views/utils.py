from ..exeptions import InvalidReference


def validate_dict(dictionary, value_type):
    for key, value in dictionary.items():
        if isinstance(value, list):
            value = value[0]
        try:
            dictionary[key] = value_type(value)
        except (TypeError, ValueError) as e:
            raise InvalidReference(details=str(e))
    return dictionary