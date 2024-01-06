from fastapi import Request


async def load(request: Request):
    return {
        "request": request,
        "context": {
            "title": "Gamedle",
            "items": {
                "Featured Collection": [
                    {
                        "img": "",
                        "item": "Elegant Dress",
                        "price": 1.0,
                        "rating": 0,
                        "href": "",
                    },
                    {
                        "img": "",
                        "item": "Denim Jacket",
                        "price": 1.0,
                        "rating": 0,
                        "href": "",
                    },
                    {
                        "img": "",
                        "item": "Voile Blouse",
                        "price": 1.0,
                        "rating": 0,
                        "href": "",
                    },
                    {
                        "img": "",
                        "item": "Stylish Shirt",
                        "price": 1.0,
                        "rating": 0,
                        "href": "",
                    },
                    {
                        "img": "",
                        "item": "Elegant Dress",
                        "price": 1.0,
                        "rating": 0,
                        "href": "",
                    },
                    {
                        "img": "",
                        "item": "Denim Jacket",
                        "price": 1.0,
                        "rating": 0,
                        "href": "",
                    },
                ],
            },
        },
    }
