import argparse


def parse_arguments():
    """
    The CLI tool parses arguments to filter, aggregate, and sort a CSV file.
    """

    parser = argparse.ArgumentParser(description="CLI tool for filtering, aggregating, and sorting CSV files.")

    parser.add_argument("--file", required=True, help="CSV file path")
    parser.add_argument("--where", help="Filter condition. For example: 'price>100'")
    parser.add_argument("--aggregate", help="Aggregate condition. For example: 'price=avg'")
    parser.add_argument("--order-by", help="Ordering. For example: 'rating=desc' or 'brand=asc'")

    return parser.parse_args()
