import sys
import numpy as np
import numpy.linalg
import matplotlib.pyplot as plt
import matplotlib.cm as cm

MAX_ITERATIONS = 50

# check if the all option parameters are entered
if len(sys.argv) != 4:
   print("Not Enough Arguments")
   print("Usage: python kmeans.py csv_file_name K clustering_option plot_option")
   exit()

# check if the data set file entered is present in the current directory
file_name = sys.argv[1]
try:
   # read the entered file and copy it to data_set variable. data_set is of type numpy.array
   data_set = np.genfromtxt(file_name, delimiter=",")
except:
   print("File %s not found.\nPlease check the file name." % file_name)
   exit()

# check if the entered K value is an integer
K = sys.argv[2]
try:
   K = int(K)
except:
   print("Value of K must be an Integer")
   exit()

# check if the entered clustering option is valid [1/2/3/4/5]
clustering_option = sys.argv[3]
if not clustering_option in ("1", "2", "3", "4", "5", "6"):
   print("Value of clustering_option must be 1/2/3/4/5/6")
   exit()



# extract the required columns from data_set
# column 3 -> latitude
# column 4 -> longitude
# column 6 -> reviewCount
# column 7 -> checkins
columns = np.array([i in (3, 4, 6, 7) for i in range(19)])
data_set = data_set[1:,columns].copy()

def euclid_distance(a, b):
   if len((a-b).shape) == 2:
      return numpy.linalg.norm(a-b, axis=1)
   else:
      return numpy.linalg.norm(a-b)

def manhattan_distance(a, b):
   if len((a-b).shape) == 2:
      return np.sum(np.absolute(a-b), axis=1)
   else:
      return np.sum(np.absolute(a-b))

modified_data_set = data_set.copy()
distance_function = euclid_distance
improve = 0
impscore = 0
if clustering_option == "1":
   # no tranformation
   pass
elif clustering_option == "2":
   # apply log tranformation to reviewCount and checkins
   modified_data_set[:,2] = np.log(modified_data_set[:,2]+1)
   modified_data_set[:,3] = np.log(modified_data_set[:,3]+1)
elif clustering_option == "3":
   # standardize the data_set
   modified_data_set = (modified_data_set - np.mean(modified_data_set, axis=0)) / np.std(modified_data_set, axis=0)
elif clustering_option == "4":
   # use manhattan_distance as distance_function
   distance_function = manhattan_distance
elif clustering_option == "5":
   # use 3 percent of data_set for clustering
   total_rows = int(modified_data_set.shape[0] * 0.03)
   np.random.seed(0)
   modified_data_set = modified_data_set[np.random.choice(modified_data_set.shape[0], total_rows)]
else:
   improve = 1
   row_number = 0
   for row in modified_data_set:
     d1 = euclid_distance(centroids[current_assignments[row_number]], row)
     d2 = min(euclid_distance(centroids[np.all(centroids != centroids[current_assignments[row_number]], axis=1)], row))
     impscore += d1/d2

# select K points randomly as the initial centroids
np.random.seed(3)
centroids = modified_data_set[np.random.choice(modified_data_set.shape[0], K)].copy()

# create a list to save cluster assignments
current_assignments = [None for i in range(modified_data_set.shape[0])]
previous_assignments = []
iterations = 0

while current_assignments != previous_assignments:

   if iterations == MAX_ITERATIONS: break
   iterations += 1
   previous_assignments = current_assignments[:]
   row_number = 0

   for row in modified_data_set:
      # compute distances from all centroids to the current data point
      distances = distance_function(centroids, row)
      # allocate data point to nearest cluster 
      allocation = np.argmin(distances)
      current_assignments[row_number] = allocation
      row_number += 1
   # recompute centroids with current_assignments
   for i in range(K):
      if len(modified_data_set[np.array(current_assignments) == i]) > 1:
         centroids[i] = np.mean(modified_data_set[np.array(current_assignments) == i], axis=0)

# compute WC-SSE
WC_SSE = 0
for i in range(K):
   WC_SSE += sum([distance_function(centroids[i],x) for x in modified_data_set[np.array(current_assignments) == i]])
print("WC-SSE = ",WC_SSE)

# print centroids
for i in range(1, K+1):
   print("Centroid%d = " % i,list(centroids[i-1]))
