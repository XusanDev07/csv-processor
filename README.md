# csv-processor

CLI tool for filtering, aggregating, and sorting CSV files using Python.

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 🚀 Usage Examples

Filtering by rating and sorting by price (ascending):

```bash
python3 main.py --file products.csv --where "rating>4.5" --order-by "price=asc"
```

Aggregating by price — average value:

```bash
python3 main.py --file products.csv --aggregate "price=avg"
```

Minimum rating value:

```bash
python3 main.py --file products.csv --aggregate "rating=min"
```

## 📄 Description

The `main.py` script allows you to:

- 🔍 Filter rows in a CSV file based on conditions (supports >, <, =).
- 📊 Aggregate data in numeric columns (average, minimum, maximum).
- 🔃 Sort rows by any column (ascending or descending).

## 🛠️ Command-Line Arguments

| Argument      | Description                                                                         |
|---------------|-------------------------------------------------------------------------------------|
| `--file`      | \*\*Path to the CSV file\*\* (required).                                            |
| `--where`     | \*\*Filtering condition\*\*, for example: \`rating>4.5\`.                           |
| `--aggregate` | \*\*Aggregation on a column\*\*, e.g.: \`price=avg\`, \`price=max\`, \`price=min\`. |
| `--order-by`  | \*\*Sorting by column\*\*, e.g.: \`price=asc\` or \`price=desc\`.                   |

### ✅  Running Tests
Tests are written using pytest:
```bash
pytest -v
```
The tests cover functionality for filtering, aggregating, and sorting.