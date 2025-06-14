from ..repository import items as repo


# get_item() is unnecessary

def delete_item(request, id):
    """
    Service. Checks whether instance exists and authenticates user, deletes instance if checks are valid.
    Returns 404, 403 or deletes instance accordingly.
    """
    item = repo.get_item(request, id)
    if not item:
        print(f'service: item {id} not found')
        return 404
    
    user_match = request.user == item.user 
    if not user_match:
        print(f'service: users do not match {request.user} - {item.user}')
        return 403
    
    print('service: passing id to repo..')
    repo.delete_item(request, id)
    return