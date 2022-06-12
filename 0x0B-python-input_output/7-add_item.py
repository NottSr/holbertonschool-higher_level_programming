#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then save them to a file
"""
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists('add_item.json'):
    file_obj_json = load_from_json_file('add_item.json')
else:
    file_obj_json = []

for i in range(1, len(sys.argv)):
    file_obj_json.append(sys.argv[i])

save_to_json_file(file_obj_json, 'add_item.json')
