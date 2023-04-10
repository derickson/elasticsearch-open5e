import json

def pretty_print_json(json_data, indent_spaces=4):
    """Pretty print JSON data with variable indent spacing.

    Args:
        json_data (dict): The JSON data to be pretty printed.
        indent_spaces (int, optional): The number of spaces to use for each level of indentation.
            Defaults to 4.

    Returns:
        str: The pretty printed JSON string.
    """
    return json.dumps(json_data, indent=indent_spaces)