"""

Donald Steinert

MIT Intro to CS and Programming

pset1c - alpha.py

requests user input and checks for longest consecutive aplhabetical block
assumes user input is a string of lower case letters
in event of tie, returns first block

"""

s = raw_input('Please enter the string you would like to check: ')
s_len = len(s)
max_count = 0
temp_count = 1
max_block_start = 0

for i in range(0, s_len - 1):
    for j in range(i + 1, s_len):
        if s[j-1] > s[j]:
            temp_count = 1
            break
        else:
            temp_count += 1
            if temp_count > max_count:
                max_count = temp_count
                max_block_start = i
    temp_count = 1

if max_count <= 1:
    print('No consecutive alphabetical substring')
else:
    print(s[max_block_start:max_block_start + max_count])

