import random
from typing import Callable, Dict, List, Tuple, TypeVar, DefaultDict

FeatureVector = Dict[str, int]
WeightVector = Dict[str, float]
Example = Tuple[FeatureVector, int]

def r(n,x):
    x = x.replace(' ','')
    res = Dict[str,int]
    inicial = x[:n]
    print(inicial)

r(3,"I like tacos")