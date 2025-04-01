from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class MRWordCount(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   combiner=self.combiner,
                   reducer=self.reducer)
        ]

    def mapper(self, _, line):
        # Remove special characters and convert to lowercase
        line = line.strip()
        words = re.findall(r'\w+', line.lower())
        # Emit each word with a count of 1
        for word in words:
            yield word, 1

    def combiner(self, word, counts):
        # Sum the counts for each word on the mapper side
        yield word, sum(counts)

    def reducer(self, word, counts):
        # Sum the counts for each word across all mappers
        yield word, sum(counts)

if __name__ == '__main__':
    MRWordCount.run()