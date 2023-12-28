# script to run all tests defined in tests.py 

import inspect
import tests

if __name__ == "__main__":

    # create list of all functions in tests.py
    functions = []
    for name, obj in inspect.getmembers(tests):
        if inspect.isfunction(obj):
            functions.append(obj)

    # run each function
    for func in functions:
        func()