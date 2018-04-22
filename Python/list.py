#!/usr/bin/env python3

# List all files in cwd
from os import listdir
from os.path import isfile

path = '.'
onlyfiles = [f for f in listdir(path) if isfile(f)]

print(onlyfiles)
