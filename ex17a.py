# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 10:29:52 2018
@author: Berdakh
"""
from sys import argv
from os.path import exists

script, from_file, to_file = argv
open(to_file,'w').write(open(from_file).read())

input(f"""Copying from {from_file} to {to_file}.
      The input file is {len(open(from_file).read())} bytes long.
      Does the output file exist? {exists(to_file)}.
      Ready,hit RETURN to continue, CTRL-C to abort.
      Alright, all done.
""")
