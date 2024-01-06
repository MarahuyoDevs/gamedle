from fastapi import Request


async def load(request: Request):
    return {
        "request": request,
        "context": {
            "games": {
                "Casino": [
                    {
                        "title": "BlackJack",
                        "href": "/play/blackjack",
                        "description": "A simple game of blackjack.",
                    },
                ],
                "Reaction": [
                    {
                        "title": "Reaction speed test",
                        "href": "/play/blackjack",
                        "description": "Let's see how fast are you shooting players.",
                    },
                    {
                        "title": "Grid clicker",
                        "href": "/play/blackjack",
                        "description": "Click on the grid as fast as you can.",
                    },
                ],
                "Casual": [
                    {
                        "title": "Whack A Mole",
                        "href": "/play/wam",
                        "description": "You better whack those moles!",
                    },
                ],
            }
        },
    }
