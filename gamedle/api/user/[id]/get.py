async def endpoint(id: str):
    """
    get a user from the database
    """
    return {"message": "get user with id: " + id}
