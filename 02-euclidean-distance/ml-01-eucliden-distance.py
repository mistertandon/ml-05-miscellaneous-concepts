import math

x1_vector = [1, 3]
x2_vector = [2, 5]

vector_len = len(x1_vector)

'''
Euclidean distance: https://en.wikipedia.org/wiki/Euclidean_distance
'''
# 1: Computing difference between two vectors, along with it computing square
diff_square = [math.pow((x1_vector[index] - x2_vector[index]), 2) for index in range(vector_len)]

# 2: Computing sum
distance = sum(diff_square)

# 3: Computing sqrt
euclidean_distance = math.sqrt(distance)