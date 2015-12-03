#! /usr/bin/python
import sys
from itertools import groupby
from operator import itemgetter
def read_mapper_output(file, separator):
    for line in file:
        yield line.rstrip().split(separator, 2)

def reducer(separator='\t'):
    data = read_mapper_output(sys.stdin, separator)
    #data is all mapper's output
    #use group by, instead of old_key or this_key trick
    for current_word, group in groupby(data, itemgetter(0)):
        doclist = []
        df = 0
        for current_word, doc_id, tf in group:
            doclist.append((doc_id, tf))
            df += 1
        print "{0}\t{1}\t{2}".format(current_word, df, doclist)


if __name__ == "__main__":
    reducer()

