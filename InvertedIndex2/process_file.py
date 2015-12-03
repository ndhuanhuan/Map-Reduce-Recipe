#!/usr/bin/python
import sys
filename_in = sys.argv[1]
filename_out = sys.argv[2]
line_id = 1
with open(filename_in, 'r') as f_in:
    with open(filename_out, 'w') as f_out:
        for line in f_in:
            f_out.write("{0} {1}".format(line_id, line))
            line_id += 1