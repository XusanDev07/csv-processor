import sys
from tabulate import tabulate
from csv_utils.sorter import sort_rows
from csv_utils.filter import filter_rows
from csv_utils.csv_reader import read_csv
from csv_utils.cli import parse_arguments
from csv_utils.aggregate import aggregate_column


def main():
    """
    Main function to execute the CLI tool for filtering, aggregating, and sorting CSV files.
    :raises FileNotFoundError: If the specified CSV file does not exist.
    :raises ValueError: If the provided arguments are invalid.
    """

    args = parse_arguments()

    try:
        rows = read_csv(args.file)
    except FileNotFoundError:
        print(f"File not found: {args.file}")
        sys.exit(1)

    if args.where:
        rows = filter_rows(rows, args.where)

    if args.aggregate:
        result = aggregate_column(rows, args.aggregate)
        print(result)
        return

    if args.order_by:
        rows = sort_rows(rows, args.order_by)

    print(tabulate(rows, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
