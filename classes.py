from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from typing import List

class measurement_unit(Enum):
    grams = 1
    portions = 2
    
class region(Enum):
    us = 1
    uk = 2
    pl = 3

class activity_status(Enum):
    still = 1
    slightly_active = 2
    sedentary_work = 3
    avarage_work = 4
    intense_work = 5
    
@dataclass
class body_measurements:
    weight_kg: float
    height_cm: float
    neck_cm: float
    waist_cm: float
    
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
    measurements: body_measurements
    status: activity_status
    food_list: List[food]


    
