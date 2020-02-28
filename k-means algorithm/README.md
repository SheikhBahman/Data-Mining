
# Description
In this programming I implemented the k-means algorithm and apply it to a real-life data set.

# Author
Bahman Sheikh

# Programming Language
Python

## Input
The provided input file ("places.txt") consists of the locations of 300 places in the US. Each location is a two-dimensional point that represents the longitude and latitude of the place. For example, "-112.1,33.5" means the longitude of the place is -112.1, and the latitude is 33.5.

places.txt

## Output
Expectation: You are required to implement the k-means algorithm and use it to cluster the 300 locations into three clusters, such that the locations in the same cluster are geographically close to each other.
After reading the 300 locations in "places.txt" and applying the k-means algorithm (with k = 3), you are required to generate an output file named "clusters.txt". The output file should contain exactly 300 lines, where each line represents the cluster label of each location. Every line should be in the format: location_id cluster_label.
