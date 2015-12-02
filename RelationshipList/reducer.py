#! /usr/bin/python
import sys
def reducer():
    old_key = None
    thread_user_list = []
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) == 2:
            this_key, this_id = data
            if old_key and old_key != this_key:
                #time to change
                print "{0}\t{1}".format(old_key, thread_user_list)
                old_key = None
                thread_user_list = []
            old_key = this_key
            thread_user_list.append(this_id)
    if old_key is not None:
        print "{0}\t{1}".format(old_key, thread_user_list)
if __name__ == "__main__":
    reducer()
