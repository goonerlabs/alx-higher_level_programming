#!/usr/bin/python3
"""adds args to the program as a list to a file in JSON format"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if __name__ == "__main__":
    try:
        res = load_from_json_file("add_item.json")
    except FileNotFoundError:
        res = []
    res.extend(sys.argv[1:])
    save_to_json_file(res, "add_item.json")
