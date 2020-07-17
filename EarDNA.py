# -*- coding: utf-8 -*-
"""
Guo Bujia

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
"""
import pandas as pd

file = pd.read_csv("https://nyu-cds.github.io/courses/data/houseelf_earlength_dna_data.csv")

print(file.earlength[0])

small = 0
big = 0

for x in range(len(file)):
    if file.earlength[x] > 10:
        file.earlength[x] = "long"
    else:
        file.earlength[x] = "short"
    
file.to_csv("granger_analysis.csv", sep=",", index=False)

"GC ratio equation is (G+C/A+T+G+C)*100%"
data = (file.dnaseq.str.count("C") + file.dnaseq.str.count("G"))/(file.dnaseq.str.count("T") + file.dnaseq.str.count("C") + file.dnaseq.str.count("G") +file.dnaseq.str.count("A"))
"Data shown in percentage how many CG content they have in their DNA seq"
print(data)

