#! /usr/bin/python
import sys
def read_mapper_input(stdin):
    for line in stdin:
        yield line.rstrip()

def mapper():
    for line in read_mapper_input(sys.stdin):
        # one line is one document
        data = line.strip().split(' ')
        line_id = data[0]
        tf_dict = dict()
        for word in data[1:]:
            tf_dict[word] = tf_dict.get(word, 0) + 1
        for item in tf_dict.items():
            print "{0}\t{1}\t{2}".format(item[0], line_id, item[1])
            #word, docid, term frequency
        

if __name__ == "__main__":
    mapper()