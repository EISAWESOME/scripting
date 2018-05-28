#!/usr/bin/env python3

from os import walk
from os import path
# Walk in current directory
for root, dirs, files in walk("."):
  jpg_set = set()
  raw_set = set()
  for name in files:
    extension = path.splitext(name)[1]
    surname = path.splitext(name)[0]
    if extension.upper() == '.JPG':
      jpg_set.add(surname)
    elif extension.upper() == '.RAW':
      raw_set.add(surname)
print("JPG sans raw : ")
print(jpg_set.difference(raw_set))
print("RAW sans JPG : ")
print(raw_set.difference(jpg_set))
