#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks question in order to acquire candidates for a roommate"""

ERROR = ('Sorry, you did not meet the criteria.'
        'Thank you for you time and good luck!')
COUNT = 0
Q1 = raw_input('What is your name? ').upper()
Q2 = raw_input('What is your phone number? ')
Q3 = raw_input('Do you like sports? ')[:1].lower()
Q4 = raw_input('Do you like video games? ')[:1].lower()

if Q3 == 'y' or Q4 == 'y':
    Q5 = raw_input('Do you like meeting new people? ')[:1].lower()
    Q6 = raw_input('Do you mind sharing a living space? ')[:1].lower()
    Q7 = raw_input('Can you afford your share of rent? ')[:1].lower()
    ANSWERS = [Q3, Q4, Q5, Q6, Q7]
    for Y in ANSWERS:
        if Y == 'y':
            COUNT += 1
        else:
            pass
    if COUNT >= 3:
        f = open('Candidates.txt', 'a')
        f.write(('Name: {0}\nPhone Number: {1}\n\n').format(Q1, Q2))
        f.close()
        print '\n\n\nCongrats. You have been selected as a candidate!'
    else:
        pass
else:
    print ERROR

