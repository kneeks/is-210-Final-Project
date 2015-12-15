#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks question in order to acquire candidates for a roommate"""

ERROR = ('Sorry, you did not meet the criteria.'
         'Thank you for you time and good luck!')
COUNT = 0
Q1 = 'What is your name? '
Q2 = 'What is your phone number? '
Q3 = 'Do you like sports? '
Q4 = 'Do you like video games? '
Q5 = 'Do you like meeting new people? '
Q6 = 'Do you mind sharing a living space? '
Q7 = 'Can you afford your share of rent? '

A1 = raw_input(Q1).upper()
A2 = raw_input(Q2)
A3 = raw_input(Q3)[:1].lower()
A4 = raw_input(Q4)[:1].lower()

if A3 == 'y' or A4 == 'y':
    A5 = raw_input(Q5)[:1].lower()
    A6 = raw_input(Q6)[:1].lower()
    A7 = raw_input(Q7)[:1].lower()
    ANSWERS = [A3, A4, A5, A6, A7]
    for Y in ANSWERS:
        if Y == 'y':
            COUNT += 1

        else:
            pass
    if COUNT >= 3:
        F = open('Candidates.txt', 'a')
        F.write(('Name: {0}\nPhone Number: {1}\n{2}{3}\n{4}{5}\n{6}{7}\n'
                 '{8}{9}\n{10}{11}\n\n').format(A1, A2, Q3, A3,
                                                Q4, A4, Q5, A5,
                                                Q6, A6, Q7, A7))
        F.close()
        print '\n\n\nCongrats. You have been selected as a candidate!'
    else:
        print ERROR
else:
    print ERROR
