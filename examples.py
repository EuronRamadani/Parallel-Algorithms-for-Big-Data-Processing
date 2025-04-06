from mapreduce import ParallelMapReduce
import re
import sys

def word_count_map(document):
    words = re.findall(r'\w+', document.lower())
    return [(word, 1) for word in words]

def word_count_reduce(word, counts):
    return sum(counts)

def read_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line for line in f if line.strip()]

def process_file(filename):
    lines = read_text_file(filename)
    
    # Create and execute MapReduce job
    mapreduce = ParallelMapReduce(n_workers=4)
    result = mapreduce.execute(lines, word_count_map, word_count_reduce)
    
    # Output results in sorted order
    for word, count in sorted(result.items()):
        print(f"{word}\t{count}")

if __name__ == "__main__":
    # Get input file from command line argument, default to input.txt
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    process_file(input_file) 