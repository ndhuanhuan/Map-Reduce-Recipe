#! /usr/bin/python
# code borrowed from https://github.com/jabaldonedo/udacity-hadoop/blob/master/lesson3/3.6/mapper.py
import sys
import re
regex_log = re.compile("(?P<host>\S+) (?P<identity>\S+) (?P<username>\S+) \[(?P<time>.+)\] \"(?P<method>.+) "
                       "(?P<request>.+) (?P<protocol>.+)\" (?P<status>[0-9]+) (?P<size>\S+)")

regex_fname = re.compile("http://.*?(/.*)")

def mapper():
    for line in sys.stdin:
        r = regex_log.search(line)
        if r is not None:
            res_log = r.groupdict()
            request = res_log[u'request']
            if request.startswith('http'):
                res_fname = regex_fname.findall(request)
                if res_fname is not None and len(res_fname) > 0:
                    print "{0}\t{1}".format(res_fname[0], 1)
            else:
                print "{0}\t{1}".format(request, 1)
                
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__
    
if __name__ == '__main__':
    mapper()    
