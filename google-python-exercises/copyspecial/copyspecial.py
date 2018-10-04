#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_paths(dirt):
  l=[]
  filenames = os.listdir(dirt)
  for filename in filenames:
    match = re.search(r'__\w+__', filename)
    if match:
      l.append(os.path.abspath(os.path.join(dirt, filename)))	
  
  return l

def copy_to(paths, dir):
  for path in paths:
    try:
      print "COPY"
      shutil.copy(path, os.path.abspath(dir))
    except IOError:
      sys.stderr.write('problem opening:' + dir)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    print 'DIR'
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths=[]
  try:
    print args
    print todir
    for dirt in args:
      #print get_paths(dirt)
      for path in get_paths(dirt):
        if path in paths:
	  raise IOError("Duplicated files!")
        paths.append(path)

    if todir != '':
      copy_to(paths, todir)
  

  except IOError:
    sys.stderr.write(repr(error))

if __name__ == "__main__":
  main()
