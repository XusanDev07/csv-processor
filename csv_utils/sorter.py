from typing import List, Dict


def sort_rows(rows: List[Dict[str, str]], order_by: str) -> List[Dict[str, str]]:
    """
    Sorts rows based on a specified column and direction.
    The order_by parameter should be in the format "column=asc" or "column=desc".
    """
    try:
        column, direction = order_by.split("=")
    except ValueError:
        raise ValueError("Sort format must be 'column=asc' or 'column=desc'")

    column = column.strip()  # Remove any leading/trailing whitespace
    direction = direction.strip().lower()  # Normalize direction to lowercase

    reverse = direction == "desc"

    def sort_key(row):
        value = row.get(column)  # Use get to avoid KeyError if column doesn't exist
        try:
            return float(value)
        except ValueError:
            return value.lower() if isinstance(value, str) else value

    return sorted(rows, key=sort_key, reverse=reverse)
