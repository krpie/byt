from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
from typing import List, Tuple, TypedDict
import inspect

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
    
@dataclass(order=True)
class body_measurements:
    weight_kg: float
    height_cm: float
    neck_cm: float
    waist_cm: float
    
@dataclass(order=True)
class food:
    name: str
    unit: measurement_unit
    calories_per_100_g: int
        
    def calculate_calories():
        return None 
        
@dataclass(order=True)
class Account:
    personaldata: str 
    phone: str
    email: str
    birth_date: datetime
    measurements: body_measurements
    status: activity_status
    food_list: List[Tuple[datetime, food]] = field(default_factory=list)



account1 = Account("name1", "00000", "mail@mail.com", datetime.now, body_measurements(1, 1, 1, 1), activity_status.avarage_work)
account1.food_list.append(food)
print(f"{account1.__getattribute__('phone')}")
print(f"{account1}")
print(inspect.getmembers(Account, inspect.isfunction))