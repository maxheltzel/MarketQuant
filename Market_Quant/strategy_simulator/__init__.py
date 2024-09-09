import pkgutil
import importlib

__path__ = pkgutil.extend_path(__path__, __name__)

for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    module = importlib.import_module(f"{__name__}.{module_name}")
    globals()[module_name] = module
