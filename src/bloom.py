from math import log
import csv
from sys import maxsize, argv
import numpy as np
from re import search
from bitarray import bitarray
import mmh3

"""
Simple bloom filter. Based on a few random hash functions
I found on GeeksForGeeks because our professor never told us
how tf we suppose to create such function by regular standards
or whatever


Fun fact: Taiwan is a country, now cry
"""

# Exception raised for errors in a string path
class InvalidPath(Exception):

    def __init__(self, path, message="Path is not CSV"):
        self.path = path
        self.message = message
        super().__init__(self.message)

    def __str__(self):
            return f'{self.path} -> {self.message}'


# Hash Function
def mult_method(item: object, hash_size: int=maxsize, seed=0):
    return (id(item) + seed**2) % hash_size + 1


# n = number of elements to insert
# f = the false positive rate
# m = number of bits in a Bloom filter
def load_data():
    if len(argv) <= 1:
        print("""
Usage: bloom [DATABASE-PATH] [CHECK-PATH] [FILENAME/PATH] (Optional) [FALSE-POSITIVE_VAL] (Optional)
Basic bloom filter
Example: ./bloom-filter db_input.csv db_check.csv
This will output a results.csv on the same dir as the script
        """)
        exit()

    # first one are the input emails, the second one are the tests emails which represent the database
    try:
        with open(argv[1], 'r') as file:
            data_iter = csv.reader(file)    
            next(data_iter, None)  # skip the headers      
            i = [i for i in data_iter]
        data = np.array(i, dtype=str)
        
        with open (argv[2], 'r') as test_file:
            data_tester_iter = csv.reader(test_file)
            next(data_tester_iter, None)  # skip the headers      
            j = [j for j in data_tester_iter]
        data_tests = np.array(j, dtype=str)

    except:
        print("invalid path or file")
        exit()

    try:
        path = argv[3]
        if not search('(\w+)\.csv$', path):
            raise InvalidPath(path)
    except InvalidPath:
        print("Path is not CSV")
        exit()
    except IndexError:
        print("Using default")
        path = 'Result.csv'
    
    try:
        fp_rate = float(argv[4])
        print(type(fp_rate))
    except IndexError:
        fp_rate = 0.005 # given on rubric
    return (data, data_tests, path, fp_rate)

class BloomFilter(object):
    # size is the max num of elements in the filter
    # fp is the false positive probability
    def __init__(self, size, fp_rate):
        self.size = size
        self.fp_rate = fp_rate
        self.__bit_size = self.bit_size() # M
        self.__hash_count = self.hash_count() # K
        self.bit_array = bitarray(self.__bit_size)
        self.bit_array.setall(0)
 
    # m = size of bit array
    # n = expected number of items
    # p = probability percentage represented as a decimal
    # k = number of hash functions required

    def bit_size(self):
        return int(-log(self.fp_rate)*self.size/(log(2)**2))
    
    def hash_count(self):
        return int(self.__bit_size*log(2)/self.size)
 
    def printParameters(self):
        print("Init parameters: ")
        print(f"n = {self.size}, f = {self.fp_rate}, m = {self.__bit_size}, k = {self.__hash_count}")

    def add_item(self, item):
        for seed in range(self.__hash_count):
            index = mmh3.hash(item, seed) % self.__bit_size
            self.bit_array[index] = 1
 
    def check(self, item):
        for seed in range(self.__hash_count):
            index = mmh3.hash(item, seed) % self.__bit_size
            if self.bit_array[index] == 0:
                return False
        return True

    def add_array(self, array):
        try:
            for item in array.tolist():
                self.add_item(item[0])
        except TypeError:
            print("Array must be a numpy array (ndarray)")
            exit()
        
    def print_calculated_params(self):
        print(f"""Init parameters: 
        n = {self.size}, f = {self.fp_rate}, m = {self.__bit_size}, k = {self.__hash_count}""")

    def check(self, item):
        for i in range(self.__hash_count):
            index = mmh3.hash(item, i) % self.__bit_size
            if self.bit_array[index] == 0:
                return False
        return True


def combined_data(arr_1, arr_2):
    combined_data = np.column_stack((arr_1, arr_2))
    return combined_data


def main():
    data = load_data()

    # Hard coded values
    data_set_length = len(data[0])
    check_set_length = len(data[1])

    print(f"""Data sizes: 
        check size = {check_set_length}, input size = {data_set_length}""")

    Filter = BloomFilter(data_set_length, data[3])
    Filter.add_array(data[0])    

    truth_array = [] 
    for row in data[1]:
        if Filter.check(row):
            truth_array.append('Probably in the DB')
        else:
            truth_array.append('Not in the DB')

    new_data = combined_data(data[1], truth_array)
    fields = ['Email', 'Result'] 
    with open(data[2], 'w') as file:
        # creating a csv writer object 
        csvwriter = csv.writer(file) 

        # writing the fields 
        csvwriter.writerow(fields) 

        # writing the data rows 
        csvwriter.writerows(new_data)  


if __name__ == '__main__':
    main()
