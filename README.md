# K-Means-Clustering-Algorithm

In this programming assignment, the the k-means clustering algorithm was implemented.

## Dataset
This project used the ‘Yelp’ dataset. It contains 19 attributes: 15 diescrete and 4 continuous ({latitude, longitude, reviewCount, checkins}). Your task for this homework is to imple- ment the k-means algorithm and apply it to the continuous attributes in the data.
The submission was run on a hidden dataset which is different from the given dataset. The hidden dataset would have the same column names for the continuous attributes as the given dataset.
The features you will use are the 4 continuous attributes in yelp3.csv.

# Algorithm and Expected Output

**Features:** The 4 continuous attributes in yelp.csv were considered for X.

**Distance:** Euclidean distance was used unless otherwise specified.

**Score function:** Within-cluster sum of squared error was used (where rk is the centroid of cluster Ck, d is the distance function.).

The python script should take three arguments as input:
**1. trainingDataFileName:** corresponds to a subset of the data that should be used as the training set for your algorithm.
**2. K:** the value of k to use when clustering.
**3. clustering option:** takes one of the following six values, 1 (use the four original attributs for clus- tering, which corresponds to Q3.1), 2 (apply a log transform to reviewCount and checkins, which corresponds to Q3.2), 3 (use the standardized four attributes for clustering, which corresponds to Q3.3, 4 (use the four original attributes and Manhattan distance for clustering, which corresponds to Q3.4), 5 (use 3% random sample of data for clustering, which corresponds to Q3.5), and 6 (use the improved score function, which corresponds to Q3.6).
The code reads in the training sets from the csv file, clusters the training set using the specified value of k, and outputs the within-cluster sum of squared error and cluster centroids. For the centroid of each cluster, the values for each of the four attributes are reported in the following order.
{latitude, longitude, reviewCount, checkins}
The expected output is given below. Note that this will run your algorithm with the yelp.csv file, a K value of 4, and clustering option 1. Please make sure you follow this output else you WILL loose points. Note that this is only a sample output and the numbers are not representative of the actual results.

**$ python kmeans.py yelp.csv 4 1
WC-SSE=15.2179
Centroid1=[49.00895,8.39655,12,3]
...
CentroidK=[33.33548605,-111.7714182,9,97]**

The following clustering options were also implemented.
2. A log transform to reviewCount and checkins (corresponding to 3.2).
3. Standardize the 4 attributes for clustering (corresponding to 3.3).
4. Four original attributes and Manhattan distance for clustering (corresponding to 3.4). 5. A random sample of the data for clustering (corresponding to 3.5).
6. Use your improved score function from Theory Question 5 (corresponding to 3.6)
