"""

Donald Steinert

MIT Intro to CS and Programming

pset2a -- minpay.py

requests starting cc balance, interest rate and monthly payment rate
and prints monthly payment amount and remaining balance for 12 months,
as well as total paid for the year

interest charged on first day of next month

rounds printed results to two decimal places using round()
note: MIT appears to be rounding some results, but not others in its
solution; this only rounds printed results, as specified in instructions

"""

bal = float(raw_input('What is your starting balance: '))
ann_int = float(raw_input('What is the annual interest rate: '))
mnth_min_pmnt_rt = float(raw_input('What is the minimum monthly payment rate: ')) / 100
print '\n'

mnth = 1
mnth_int_rt = ann_int / 12.0 / 100
total_pmnt = 0

while mnth <= 12:
    print 'Month: {}'.format(mnth)
    mnth_min_pmnt = mnth_min_pmnt_rt * bal
    print 'Minimum monthly payment: {}'.format(round(mnth_min_pmnt, 2))
    bal = (bal - mnth_min_pmnt) + (bal * mnth_int_rt)
    print 'Remaining balance: {}\n'.format(round(bal, 2))
    mnth += 1
    total_pmnt = total_pmnt + mnth_min_pmnt

print 'Total paid: {}'.format(round(total_pmnt, 2))
print 'Remaining balance: {}\n'.format(round(bal, 2))
