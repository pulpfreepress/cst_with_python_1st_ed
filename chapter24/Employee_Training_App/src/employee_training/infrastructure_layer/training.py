"""Contains the definition for the Training class."""


import json
from datetime import date


class Training():
    """Implements a Training entity."""
    def __init__(self)->None:
        self.title:str = None
        self.description:str = None
        self.start_date:date = None
        self.end_date:date = None
        self.status:str = None

    



