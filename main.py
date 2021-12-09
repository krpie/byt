from dataclasses import dataclass
from enum import Enum

class measurement_unit(Enum):
    grams = 1
    portions = 2

@dataclass
class food:
    name: str
    unit: measurement_unit
    calories_per_100_g: int