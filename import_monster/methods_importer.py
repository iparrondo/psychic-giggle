import builtins
import importlib
import math
import sys
from types import ModuleType
from typing import Callable, List, Optional, Union

import scipy


def methods_importer(
    method_name: str, modules: List[Union[str, ModuleType]]
) -> List[Callable]:
    output = []
    for module in modules:
        try:
            if isinstance(module, ModuleType):
                mod = module
            elif isinstance(module, str):
                mod = importlib.import_module(module)
            else:
                raise TypeError("Must be list of strings or ModuleType")

            #print("mod.__name__ :", mod.__name__)

            met = getattr(mod, method_name, None)

            if met:
                if isinstance(met, Callable):
                    output.append(met)

        except ImportError:
            continue

    return output



if __name__ == "__main__":
    #test of function methods_importer
    search_callable = methods_importer("sqrt", [scipy, math])
    print(search_callable)
    print(type(search_callable))
    for i in range(len(search_callable)):
        print(search_callable[i], 'test with parameter (3):', search_callable[i](3))
    print("compare to math.sqrt(3) = ", math.sqrt(3))
