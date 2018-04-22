#!/usr/bin/env python3
import tarfile
import os
import sys

# Script used to tar directories

# Main tar function
def make_tarfile(output_filename, source_dir, compression):
    with tarfile.open(output_filename, "w:%s" % compression) as tar:
            i = 0
            while i < len(source_dir):
                tar.add(source_dir[i], arcname=os.path.basename(source_dir[i]))
                i += 1
    print('Done!')

if(len(sys.argv) < 4):
    print("Usage : ./tar.py <compression : bz2 or gz> <archive name> <path to folder 1> ... <path to folder n> ")
    exit()

comp = sys.argv[1]

if (comp == 'bz2') or (comp == 'gz'):
    print('Compression : %s' % comp)
else :    
    print('Compression type not found, falling back to gz')
    comp = 'gz'

name = sys.argv[2]
name += '.tar.' + comp

source = []
if(len(sys.argv) >= 4):
    for x in range(3, len(sys.argv)):
        source.append(sys.argv[x])

# Function call
make_tarfile(name, source, comp)