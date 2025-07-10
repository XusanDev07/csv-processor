from typing import List, Dict


def filter_rows(rows: List[Dict[str, str]], condition: str) -> List[Dict[str, str]]:
    """
    Filters rows based on a condition.
    The condition should be in the format "column>value", "column<value", or "column=value".
    For example, "price>100" will filter rows where the price column is greater than 100.
    """

    if not rows:
        raise ValueError("No rows to filter.")
    if not condition:
        raise ValueError("Condition cannot be empty.")
    if ">" in condition:
        column, value = condition.split(">")
        op = ">"
    elif "<" in condition:
        column, value = condition.split("<")
        op = "<"
    elif "=" in condition:
        column, value = condition.split("=")
        op = "="
    else:
        raise ValueError("Unsupported condition format. Use >, <, or =.")

    column = column.strip()  # Remove any leading/trailing whitespace
    value = value.strip()  # Remove any leading/trailing whitespace

    def matches(row):
        cell = row[column]
        try:
            cell_val = float(cell)
            cond_val = float(value)
        except ValueError:
            cell_val = cell
            cond_val = value

        if op == ">":
            return cell_val > cond_val
        elif op == "<":
            return cell_val < cond_val
        elif op == "=":
            return cell_val == cond_val
        return None

    return [row for row in rows if matches(row)]
