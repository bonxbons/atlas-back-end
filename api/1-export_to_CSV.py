import csv
import requests
import sys

"""
Exports tasks of a given employee to a CSV file.

Usage: python3 1-export_to_CSV.py <employee_id>
"""

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

