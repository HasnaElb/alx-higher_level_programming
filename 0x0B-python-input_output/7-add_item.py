#!/usr/bin/python3
""" task 7"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argv_edit = argv[1:]

try:
<<<<<<< HEAD
my_list = load_from_json_file(filename)
except:
pass
finally:
for idx in range(1, len(sys.argv)):
my_list.append(sys.argv[idx])
save_to_json_file(my_list, filename)
=======
    content_list = load_from_json_file("add_item.json")
except:
    content_list = []
finally:
    for arg in argv_edit:
        content_list.append(arg)
    save_to_json_file(content_list, "add_item.json")
>>>>>>> daddd338da0c7075a10c29c2317800961830b1b5
