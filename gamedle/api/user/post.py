from fastapi.responses import RedirectResponse


async def endpoint():
    """
    create a user and send it to the database
    """
    return RedirectResponse("auth/login/")
