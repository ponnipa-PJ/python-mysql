def validatePostdata(data):
    """Validate post data."""
    if 'userId' not in data or not data['userId']:
        return False, 'User ID is required.'
    if 'title' not in data or not data['title']:
        return False, 'Title is required.'
    if 'content' not in data or not data['content']:
        return False, 'Content is required.'
    if len(data['title']) > 255:
        return False, 'Title cannot exceed 255 characters.'
    return True, None
