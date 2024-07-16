#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv)!= 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

