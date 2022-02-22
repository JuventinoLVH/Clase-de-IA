import collections
import math
from typing import Any, DefaultDict, List, Set, Tuple
SparseVector = DefaultDict[Any, float]

def increment_sparse_vector(v1: SparseVector, scale: float, v2: SparseVector,
) -> None:
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    If the scale is zero, you are allowed to modify v1 to include any
    additional keys in v2, or just not add the new keys at all.

    NOTE: This function should MODIFY v1 in-place, but not return it.
    Do not modify v2 in your implementation.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    for llaves in v2.keys() :
        if(v2[llaves] != 0):
           v1[llaves] += scale * v2[llaves]

    # END_YOUR_CODE

increment_sparse_vector({1:32,4:32,15:3} , 3 ,{1:32,4:32,15:3} )

