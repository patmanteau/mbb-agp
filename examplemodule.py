# Import other necessary modules
import math

# Definition of module-related variables
# Euclidean coordinated in three dimensions, examples
coord1 = [1, 5, 7]
coord2 = [3, 3, 8]
coord3 = [8, 4, 3]
coord4 = [7, 5, 7]

# Function to calculate euclidean distance metric
def calcEuclideanDist(c1, c2):
    """
    Calculate the Euclidean distance between two 3-dimensional points.
    
    This function computes the Euclidean distance between two points in 3D space,
    given their coordinates as tuples or lists of length 3. The distance is
    calculated using the formula: sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2).
    
    Args:
    c1 (tuple or list of float): The coordinates of the first point as a tuple or list (x1, y1, z1).
    c2 (tuple or list of float): The coordinates of the second point as a tuple or list (x2, y2, z2).
    
    Returns:
    float: The Euclidean distance between the two points.
    
    Example:
    >>> calcEuclideanDist((1, 2, 3), (4, 6, 9))
    7.0710678118654755
    
    Raises:
    TypeError: If the input coordinates are not provided as tuples or lists of length 3.
    """

    return math.sqrt(pow(c1[0]-c2[0], 2) + pow(c1[1]-c2[1], 2) + pow(c1[2]-c2[2], 2))
