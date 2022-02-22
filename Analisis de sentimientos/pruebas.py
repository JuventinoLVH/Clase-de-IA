import random
from typing import Callable, Dict, List, Tuple, TypeVar, DefaultDict

FeatureVector = Dict[str, int]
WeightVector = Dict[str, float]
Example = Tuple[FeatureVector, int]

prueba = [1,2,0,1,2,1,3,32,0]