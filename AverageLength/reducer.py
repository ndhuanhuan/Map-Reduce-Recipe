#!/usr/bin/python
import sys
def reducer():
    old_key = None
    answer_length = 0
    answer_count = 0
    post_length = 0
    avg_answer_length = 0
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 2:
            #print "this is a question, post_id is {0}".format(data[0])
            this_key, this_post_length = data
            #time to change
            if old_key and old_key != this_key:
                if answer_count == 0:
                    avg_answer_length = 0
                else:
                    avg_answer_length = answer_length / float(answer_count)
                print "{0}\t{1}\t{2}".format(old_key, post_length, avg_answer_length)
                old_key = this_key
                answer_length = 0
                answer_count = 0
                post_length = 0
                avg_answer_length = 0    
            old_key = this_key
            post_length = this_post_length
                    
        elif len(data) == 3:
            #print "this is an answer, post_id is {0}, parent id is {1}".format(data[0], data[1])
            this_key, this_question_id, this_answer_length = data
            #time to change
            if old_key and old_key != this_key:
                if answer_count == 0:
                    avg_answer_length = 0
                else:
                    avg_answer_length = answer_length / float(answer_count)                
                print "{0}\t{1}\t{2}".format(old_key, post_length, avg_answer_length)
                old_key = this_key
                answer_length = 0
                answer_count = 0
                post_length = 0
                avg_answer_length = 0

            old_key = this_key
            answer_length += int(this_answer_length)
            answer_count += 1
    if old_key is not None:
        print "{0}\t{1}\t{2}".format(old_key, post_length, avg_answer_length)        
if __name__ == '__main__':
    reducer()    