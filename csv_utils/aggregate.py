from typing import List, Dict


def aggregate_column(rows: List[Dict[str, str]], aggregate: str) -> str:
    """
    Aggregates a specified column in the rows based on the provided aggregate function.
    The aggregate function should be in the format "column=func", where func can be "avg", "min", or "max".
    """

    try:
        column, func = aggregate.split("=")
    except ValueError:
        raise ValueError("Aggregate format must be 'column=func'")

    column = column.strip()  # Remove any leading/trailing whitespace
    func = func.strip().lower()  # Normalize function name to lowercase

    try:
        values = [float(row[column]) for row in rows]  # Convert column values to float
    except ValueError:
        raise ValueError(f"Column '{column}' must contain numeric values for aggregation")

    if func == "avg":
        result = sum(values) / len(values) if values else 0
    elif func == "min":
        result = min(values) if values else 0
    elif func == "max":
        result = max(values) if values else 0
    else:
        raise ValueError(f"Unsupported aggregate function: {func}")

    return f"{func.upper()} of '{column}' = {result}"
