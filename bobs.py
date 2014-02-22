"""

Donald Steinert

MIT Intro to CS and Programming

pset1b - bobss.py

requests user input and counts number of 'bob's

"""

s = raw_input('Please enter the string you would like to check: ').lower()
n = len(s)
i = 0
count = 0

while i < n - 1:
    if s[i:i + 3] == 'bob':
	count += 1
    i += 1

print 'Number of \'bob\'s: {}'.format(count)
