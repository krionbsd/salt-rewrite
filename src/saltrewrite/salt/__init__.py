# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring
from saltrewrite.salt import fix_docstrings

__all__ = [modname for modname in list(globals()) if modname.startswith("fix_")]

__fixes__ = [
    (getattr(module, "FIX_PRIORITY", 0), module)
    for module in [globals()[modname] for modname in __all__]
]
