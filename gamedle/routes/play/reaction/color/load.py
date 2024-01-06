from fastapi import Request
from os.path import dirname
import os
from base64 import b64encode


async def load(request: Request):
    if os.path.exists(dirname(__file__) + "/script.py"):
        print("exists")

    with open(dirname(__file__) + "/script.py", "r") as f:
        data = f.read()
        print(data)
        return {
            "request": request,
            "context": {
                "script": b64encode(data.encode("utf-8")).decode("utf-8"),
            },
        }
