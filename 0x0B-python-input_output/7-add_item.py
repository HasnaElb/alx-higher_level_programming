#!/usr/bin/python3
"""
Function to read and save argv in JSON format in a file
"""
import sys
from json import load, dump


def load_from_json_file(filename):
    """Load JSON data from file"""
    try:
        with open(filename, 'r') as file:
            return load(file)
        except FileNotFoundError:
            return []


def save_to_json_file(data, filename):
    """Save JSON data to file"""
    with open(filename, 'w') as file:
        dump(data, file)


def main():
    """Main function"""
    json_filename = "add_item.json"
    my_list = load_from_json_file(json_filename)

    for arg in sys.argv[1:]:
        my_list.append(arg)

    save_to_json_file(my_list, json_filename)


if __name__ == "__main__":
    main()
