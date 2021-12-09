from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from typing import TypedDict

class MeasurementUnit(Enum):
    grams = 1
    portions = 2
    
class Region(Enum):
    us = 1
    uk = 2
    pl = 3

class ActivityStatus(Enum):
    still = 1
    slightly_active = 2
    sedentary_work = 3
    avarage_work = 4
    intense_work = 5
    
@dataclass
class BodyMeasurements:
    weight_kg: float
    height_cm: float
    neck_cm: float
    waist_cm: float
    
@dataclass
class food:
    name: str
    unit: MeasurementUnit
    calories_per_100_g: int
        
    def calculate_calories():
        return None 
        
class FoodDict(TypedDict):
    meal: food
    consumption_date: datetime
@dataclass
class account:
    personaldata: str
    phone: str
    email: str
    birth_date: datetime
    measurements: BodyMeasurements
    status: ActivityStatus
    food_list: FoodDict


    
