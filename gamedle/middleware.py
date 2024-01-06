from asyncio import iscoroutinefunction
import inspect
from types import coroutine
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction
from starlette.types import ASGIApp
from fastapi import Request, Response
from fastapi.templating import Jinja2Templates
import os
import importlib.util


class PypoxJinjaMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: ASGIApp,
        route_dir: str = "routes",
        excepted_routes: list = [],
    ) -> None:
        super().__init__(app)
        self.templates = Jinja2Templates(directory=route_dir)
        self.route_load_functions = self.walk(route_dir)
        self.exception_routes = excepted_routes

    async def dispatch(self, request: Request, call_next):
        if request.headers.get("accept"):
            if "text/html" in request.headers.get("accept").split(","):  # type: ignore
                # get the load function from the route if exists
                # check if load function is coroutine
                # if so, await it
                # else, call it
                if request.url.path in self.exception_routes:
                    return await call_next(request)

                if request.url.path in self.route_load_functions:
                    if inspect.iscoroutinefunction(
                        self.route_load_functions[request.url.path].load
                    ):
                        response = await self.route_load_functions[
                            request.url.path
                        ].load(request)
                    else:
                        response = self.route_load_functions[request.url.path].load(
                            request
                        )

                    return self.templates.TemplateResponse(
                        name=f"{request.url.path}/index.html", **response
                    )
                    
                else:
                    return self.templates.TemplateResponse(
                        name=f"{request.url.path}/index.html",
                        request=request,
                        headers={"Content-Type": "application/rss+xml;charset=utf-8"},
                    )
            else:
                return await call_next(request)
        else:
            return await call_next(request)

    def walk(self, path: str):
        load_modules = {}
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                if filename == "load.py":
                    module_name = os.path.splitext(filename)[0]
                    module_path = os.path.join(dirpath, filename)
                    spec: ModuleType = importlib.util.spec_from_file_location(module_name, module_path)  # type: ignore
                    module: ModuleType = importlib.util.module_from_spec(spec)  # type: ignore
                    spec.loader.exec_module(module)  # type: ignore

                    load_modules[
                        dirpath.replace(path, "")
                        .replace("\\", "/")
                        .replace("[", "{")
                        .replace("]", "}")
                        .replace("\\routes\\", "/")
                        + "/"
                    ] = module
        return load_modules
