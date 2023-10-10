from typing import Any


def validate_null_in_number_field(value: Any) -> int | Any:
    """Validate null values in numerical fields

    Args:
        value (Any): The given field that can be a numerical field or not

    Returns:
        int|Any: returns 0 if the given value is null otherwise returns the given value.
    """
    if not value:
        return 0
    if type(value) == str:
        if "." in value:
            return float(value)
        return 0
    return int(value)
