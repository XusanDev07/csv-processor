import csv
from typing import List, Dict


def read_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns its content as a list of dictionaries.
    Each dictionary represents a row in the CSV file, with keys as column headers.
    """

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
