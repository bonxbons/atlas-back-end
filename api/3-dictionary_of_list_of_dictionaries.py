#!/usr/bin/python3

"""
Exports tasks of a given employee to a JSON file.

Usage: python3 2-export_to_JSON.py <employee_id>
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Check if the employee ID is provided as a command-line argument
    if len(sys.argv)!= 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
