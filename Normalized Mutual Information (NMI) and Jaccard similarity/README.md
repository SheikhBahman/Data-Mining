# Discription
In this project, I will be implementing two clustering validation measures: Normalized Mutual Information (NMI) and Jaccard similarity.
In this project you will be given one set of ground-truth clustering (partition) results and five clustering test cases. You need to evaluate the clustering test cases with regard to the ground-truth by NMI and Jaccard measures and submit your measures. You will be graded based on whether your measures are correct.

# Author
Bahman Sheikh

# Programming Language
Python

## Input
The ground-truth clustering (partition) results are stored in file "partitions.txt"; the five clustering result test cases are stored in file "clustering_1.txt", ..., "clustering_5.txt".

Each clustering result (both ground-truth and test cases) is represented by a file. Each line in a file consists of two integers, separated by a space. The first integer represents the id of a data item, and the second integer represents the id of the cluster that this item belongs to.

## output
The file titled "scores.txt" consisting of 5 lines. Each line contains two float numbers separated by a space. The first number of the i-th line represents the NMI measure the code calculated for the i-th test case i (i.e., "clustering_i.txt") with regard to the ground-truth given in "partitions.txt", and the second number of the i-th line represents the Jaccard measure the code calculated for the i-th test case.

