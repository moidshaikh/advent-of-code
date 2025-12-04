import importlib


def import_function(module_name, func_name):
    """
    Import a function from a specified module.

    :param module_name: The dot-separated path to the Python module
    :param func_name: The name of the function to import
    :return: The specified function
    """
    import importlib

    # Import the module
    module = importlib.import_module(module_name)
    # Retrieve the function from the module
    return getattr(module, func_name)
