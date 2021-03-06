# -*- coding: utf-8 -*-
"""
Guo BuJia

The number of birds banded at a series of sampling sites has been counted 
by your field crew and entered into the following list. The first item in each 
sublist is an alphanumeric code for the site and the second value is the number 
of birds banded. Cut and paste the list into your assignment and then answer the 
following questions by printing them to the screen.

1.How many sites are there?
2.How many birds were counted at the 7th site?
3.How many birds were counted at the last site?
4.What is the total number of birds counted across all sites?
5.What is the average number of birds seen on a site?
6.What is the total number of birds counted on sites with codes beginning with C? 
(don’t just identify this sites by eye, in the real world there could be hundreds or thousands of sites)
"""

data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
        ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
		['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
		['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
		['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
		['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
		['D5', 98], ['D6', 32]]

"Answer to queston 1"
print(len(data))
"Answer to queston 2"
print(data[6][1])
"Answer to question 3, len(data)-1, because the pointer starts at 0"
print(data[len(data)-1][1]) 
"Answer to question 4"
total = 0
for x in range (len(data)):
    total = total + data[x][1]    
print(total)
"Answer to queston 5"
average = total/len(data)
print(round(average,2))
"Answer to question 6, data[x][0][0] = first letter"
ctotal = 0
for x in range (len(data)):
    if("C" in data[x][0][0]):
        ctotal += data[x][1]
print(ctotal)
