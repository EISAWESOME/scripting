#!/usr/bin/env python3

from os import walk
from os import path
# Walk in current directory
for root, dirs, files in walk("."):
  jpg_set = set()
  raw_set = set()
  # For every file in target dir
  for name in files:
    # Store extension, and extensionless name
    extension = path.splitext(name)[1]
    surname = path.splitext(name)[0]
    if extension.upper() == '.JPG' or extension.upper() == '.JPEG':
      jpg_set.add(surname)
    elif extension.upper() == '.RAW':
      raw_set.add(surname)
print("JPG sans raw : ")
print(jpg_set.difference(raw_set))
print("RAW sans JPG : ")
print(raw_set.difference(jpg_set))
