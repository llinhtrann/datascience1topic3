import csv

with open('diabetic_data.csv', 'r') as file:
    reader = csv.reader(file)

    stream = []
    for line in reader:
        stream.append(line[9])

    stream.pop(0)


    sstream = []
    for item in stream:
        sstream.append(int(item))




maxnum = 0
for i in range(0, len(sstream)):
    val = bin((1 * sstream[i] + 6) % 32)[2:]

    sum = 0
    for j in range(len(val) - 1, 0, -1):

        if val[j] == '0':
            sum += 1
        else:
            break
    if sum > maxnum:
        maxnum = sum

print('distict elements', 2 ** maxnum)

st_unique = []
for i in sstream:
    if i in st_unique:
        continue
    else:
        st_unique.append(i)

print('distinct elements', len(st_unique))
