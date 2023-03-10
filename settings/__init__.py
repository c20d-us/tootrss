"""
Load variables from settings files, override with environment variables if allowed
"""
from ast import literal_eval
from os import getenv
from typing import Dict, List, Tuple

from ._settings import *
from ._overrides import *

def convert_string(in_string):
    """
    This function will try to convert strings to native Python types such as ints,
    floats, booleans, dicts, lists, and tuples. For numeric types, the intent is
    that '1.0' and '1' will both return 1, and real floats will return as floats.
    Mis-cased booleans will return as booleans.

    Strings that aren't one of the interrogated types will return as strings.

    Args:
        in_string (string): a string value to convert
    Returns:
        return_val (various): a converted string value
    """
    return_val = None
    if isinstance(in_string, str):
        # It's a string. Is it intended to be a boolean?
        if in_string.lower() in ['false', 'true']:
            try:
                return_val = literal_eval(in_string.capitalize())
            except ValueError:
                # in_string doesn't represent a boolean
                return_val = in_string
        # See if in_string is a number
        else:
            try:
                return_val = literal_eval(in_string)
            except (SyntaxError, ValueError):
                # in_string is not a number, just go with the string
                return_val = in_string
            # in_string is a number, make it an int or float as appropriate
            else:
                # Check to see if it's a dict, a list, a tuple
                if (not isinstance(return_val, Dict) and
                        not isinstance(return_val, List) and
                        not isinstance(return_val, Tuple)):
                    # Is the value actually a float or int?
                    if float(return_val) is True:
                        return_val = float(return_val)
                        if return_val.is_integer():
                            return_val = int(return_val)
    return return_val

# Override app settings with values from the environment, if present
for constant in ENV_ALLOWED_OVERRIDES:
    override = getenv(constant)
    if override:
        globals()[constant] = convert_string(override)