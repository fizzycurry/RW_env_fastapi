from os import getenv
from typing import Any, Type

def getEnvironmentVariable(VARIABLE:str, type:Type[Any], defaultValue:Any)->Any:
    """
    Retrieves an environment variable, converts it to the specified type, and provides a default value if the variable is not set or the conversion fails.

    Args:
        VARIABLE (str): The name of the environment variable to retrieve.
        type (Type[Any]): A fixed data type (e.g., int, float, str) to which the environment variable value will be converted.
        defaultValue (Any): The default value to return if the environment variable is not set or conversion fails.

    Returns:
        Any: The value of the environment variable converted to the specified type, or the default value if unavailable or invalid.
    """
    
    value = getenv(VARIABLE)
    if value is None or value == "":
        return defaultValue
    
    try:
        value = type(value)
    except (ValueError, TypeError):
        return defaultValue
    
    return value