import streamlit as st
import pandas as pd
import csv
import bloom_filter
st.title('Data Set')
data = pd.read_csv("diabetic_data.csv") #path folder of the data file
st.write(data)

st.title('Bloom Filter')


with open('diabetic_data.csv', 'r') as file:
    reader = csv.reader(file)

    stream = []
    for line in reader:
        stream.append(line[0])

    stream.pop(0)

length = st.number_input('enter the length of Bloomfilter', step=1, min_value=1)

bloom = bloom_filter.BloomFilter(length)

for line in stream:
    bloom.add(line)

key = st.number_input('enter a query key', step=1, min_value=1)

if key in bloom:
    st.write('key is in bloom filter but can be false positive')
    if str(key) in stream:
        st.write('true positive')
    else:
        st.write('false positive')
else:
    st.write('key is not in bloom filter: true negative')

st.title('Count-Distinct Problem')

with open('diabetic_data.csv', 'r') as file:
    reader = csv.reader(file)

    sstream = []
    for line in reader:
        sstream.append(line[9])

    sstream.pop(0)


    ssstream = []
    for item in sstream:
        ssstream.append(int(item))

maxnum = 0
for i in range(0, len(ssstream)):
    val = bin((1 * ssstream[i] + 6) % 32)[2:]

    sum = 0
    for j in range(len(val) - 1, 0, -1):

        if val[j] == '0':
            sum += 1
        else:
            break
    if sum > maxnum:
        maxnum = sum

st.write('Flajolet Martin algorithm: distinct elements ', 2 ** maxnum)

st_unique = []
for i in ssstream:
    if i in st_unique:
        continue
    else:
        st_unique.append(i)

st.write('Real distinct elements', len(st_unique))