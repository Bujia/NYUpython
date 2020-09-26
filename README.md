# NYUpython
NYU data science exercises
https://nyu-cds.github.io/courses/exercises/

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

Write a Python script that:
Imports the data into a data structure of your choice
Loops over the rows in the dataset
For each row in the dataset checks to see if the ear length is large (>10 cm) or small (<=10 cm)
 and determines the GC-content of the DNA sequence (i.e., the percentage of bases that are either G or C)
Stores this information in a table where the first column has the ID for the individual, 
the second column contains the string ‘large’ or the string ‘small’ depending on the size of 
the individuals ears, and the third column contains the GC content of the DNA sequence.
Prints the average GC-content for both large-eared elves and small-eared elves to the screen.
Exports the table of individual level GC values to a CSV 
(comma delimited text) file titled grangers_analysis.csv.
