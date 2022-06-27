import csv
import bloomfilter
with open('diabetic_data.csv' ,'r') as file:
        reader = csv.reader(file)

        stream = []
        for line in reader:
                stream.append(line[0])

        stream.pop(0)

        sstream = []
        for i in range(100):
                sstream.append(stream[i])


bloom = bloomfilter.BloomFilter()

# Test whether the bloom-filter has seen a key:
for item in sstream:
        assert item not in bloom

