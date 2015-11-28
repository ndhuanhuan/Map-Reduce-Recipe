#!/usr/bin/python
import sys
import csv
import heapq
K = 10
def mapper():
    # using heap to store top k
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    heap = []
    for line in reader:
        try:
            if len(heap) < K or (len(line[4]), line) > heap[0]:
                if len(heap) == K:
                    heapq.heappop(heap)
                    
                heapq.heappush(heap, (len(line[4]), line))
        except IndexError as e:
            pass
    heap.sort()
    for item in heap:
        print writer.writerow(item[1])
def mapper_stupid():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    lines = []
    for line in reader:
        lines.append(line)
        # YOUR CODE HERE
    lines.sort(key = lambda x: len(x[4]), reverse = True)    
    for i in range(9, -1, -1):
        writer.writerow(lines[i])



test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"333\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"88888888\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"11111111111\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1000000000\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"22\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"4444\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"666666\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"55555\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"999999999\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"7777777\"\t\"\"
"""

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__
if __name__ == "__main__":
    mapper()