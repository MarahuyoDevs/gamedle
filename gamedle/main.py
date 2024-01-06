from fastapi import FastAPI
from pypox import Pypox
from os.path import dirname
from gamedle.middleware import PypoxJinjaMiddleware
from starlette.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import mimetypes

mimetypes.init()
app: FastAPI = Pypox(dirname(__file__))()
app.add_middleware(
    PypoxJinjaMiddleware,
    route_dir=(dirname(__file__) + "/routes"),
    excepted_routes=["/docs", "/static/pyodide/console.html"],
)
app.mount(
    "/static", StaticFiles(directory=dirname(__file__) + "/static"), name="static"
)
app.add_middleware(CORSMiddleware, allow_origins=["*"])
