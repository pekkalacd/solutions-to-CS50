"""

Donald Steinert

MIT Intro to CS and Programming

pset2a -- payoff.py

requests starting cc balance and interest rate

prints lowest monthly payment required to pay balance in 12 months

based on amortization formula from: http://www.myamortizationchart.com/
articles/how-is-an-amortization-schedule-calculated/ (last visited 2/23/14)

interest assumed charged on first day of next month
interst charged on remainin balance after monthly payment

rounds printed result to two decimal places using round()
note: MIT appears to be rounding some results, but not others in its
solution; this only rounds printed results, as specified in instructions

"""

p = float(raw_input('What is your starting balance: '))
ann_int = float(raw_input('What is the annual interest rate: '))

i = ann_int / 12.0 / 100 
mnths = 12

min_pmnt = (i * p * ((1 + i) ** mnths)) / (((1 + i) ** mnths) - 1)

print 'Lowest Payment: {}'.format(round(min_pmnt, 2))
