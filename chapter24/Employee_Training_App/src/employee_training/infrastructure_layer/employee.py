"""Contains the definition for the Employee class."""

import json
from datetime import date
from typing import List

class Employee():
    """Implements an Employee entity."""
    def __init__(self)->None:
        self.first_name:str = None
        self.middle_name:str = None
        self.last_name:str = None
        self.birthday:date = None
        self.gender:str = None
        self.training:List = []


