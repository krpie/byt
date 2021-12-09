from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class measurement_unit(Enum):
    grams = 1
    portions = 2
    
class region(Enum):
    us = 1
    uk = 2
    pl = 3

class activity_status(Enum):
    still = 1
    

@dataclass
class food:
    name: str
    unit: measurement_unit
    calories_per_100_g: int
    
@dataclass
class account:
    personaldata: str
    phone: str
    email: str
    birth_date: datetime
    
@dataclass
class body_measurements:
    weight_kg: float
    height_cm: float
    neck_cm: float
    waist_cm: float
    
