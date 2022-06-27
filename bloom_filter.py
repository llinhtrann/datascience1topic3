from bitarray import bitarray
import csv


class BloomFilter(set):

    def __init__(self, size):
        super(BloomFilter, self).__init__()
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        self.size = size

    def __len__(self):
        return self.size

    def __iter__(self):
        return iter(self.bit_array)

    def add(self, item):
        index = (2 * int(item) + 3) % self.size
        self.bit_array[index] = 1
        index = (5 * int(item) + 4) % self.size
        self.bit_array[index] = 1
        index = (7 * int(item) + 11) % self.size
        self.bit_array[index] = 1
        index = (13 * int(item) + 7) % self.size
        self.bit_array[index] = 1
        index = (19 * int(item) + 5) % self.size
        self.bit_array[index] = 1
        index = (13 * int(item) + 3) % self.size
        self.bit_array[index] = 1
        index = (2 * int(item) + 29) % self.size
        self.bit_array[index] = 1
        index = (2 * int(item) + 17) % self.size
        self.bit_array[index] = 1
        index = (11 * int(item) + 17) % self.size
        self.bit_array[index] = 1
        index = (23 * int(item) + 5) % self.size
        self.bit_array[index] = 1


        return self

    def __contains__(self, item):
        out = True
        index = (2 * int(item) + 3) % self.size
        if self.bit_array[index] == 0:
            out = False
        index = (5 * int(item) + 4) % self.size
        if self.bit_array[index] == 0:
            out = False
        index = (7 * int(item) + 11) % self.size
        if self.bit_array[index] == 0:
            out = False
        index = (13 * int(item) + 7) % self.size
        if self.bit_array[index] == 0:
            out = False
        index = (19 * int(item) + 5) % self.size
        if self.bit_array[index] == 0:
            out = False
        index = (13 * int(item) + 3) % self.size
        if self.bit_array[index] == 0:
            out = False
        index = (2 * int(item) + 29) % self.size
        if self.bit_array[index] == 0:
            out = False
        index = (2 * int(item) + 17) % self.size
        if self.bit_array[index] == 0:
            out = False
        index = (11 * int(item) + 17) % self.size
        if self.bit_array[index] == 0:
            out = False
        index = (23 * int(item) + 5) % self.size
        if self.bit_array[index] == 0:
            out = False

        return out

def main():

        with open('diabetic_data.csv', 'r') as file:
            reader = csv.reader(file)

            stream = []
            for line in reader:
                stream.append(line[0])

            stream.pop(0)

        bloom = BloomFilter(100)

        for line in stream:
            bloom.add(line)

        key = input("input a query key")
        if key in bloom:
            print('match')
        else:
            print('miss')


if __name__ == '__main__':
    main()