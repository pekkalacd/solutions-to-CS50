"""

Donald Steinert

MIT Intro to CS and Programming

pset1a - vowels.py

requests user input and counts number of vowels

"""

s = raw_input('Please enter the string you would like to check: ').lower()
i = len(s)
count = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for w in s:
    for v in vowels:
        if w == v:
	    count += 1

print 'Number of vowels: {}'.format(count)
