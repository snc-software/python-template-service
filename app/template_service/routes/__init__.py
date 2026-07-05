import importlib
import pkgutil

from fastapi import APIRouter

routers: list[APIRouter] = []

package_name = __name__

for module_info in pkgutil.iter_modules(__path__):
    module = importlib.import_module(f"{package_name}.{module_info.name}")

    if hasattr(module, "router") and isinstance(module.router, APIRouter):
        routers.append(module.router)
