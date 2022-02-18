import random
from typing import Callable, Dict, List, Tuple, TypeVar, DefaultDict

FeatureVector = Dict[str, int]
WeightVector = Dict[str, float]
Example = Tuple[FeatureVector, int]

def extractWordFeatures(x: str) -> FeatureVector:
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x:
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    featDic = dict()
    for palabras in x.split():
        if palabras not in featDic:  featDic[palabras] = 1
        else:  featDic[palabras] = featDic[palabras] +1
    return featDic

x = extractWordFeatures("I am what I am")
for key in x:
    print(x[key])