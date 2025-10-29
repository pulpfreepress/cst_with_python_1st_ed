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


    def __str__(self)->str:
        return self.to_json()
    
    
    def __repr__(self)->str:
        return self.to_json()

    
    def to_json(self)->str:
        training_dict = {}
        training_dict['title'] = self.title
        training_dict['description'] = self.description
        training_dict['start_date'] = self.start_date
        training_dict['end_date'] = self.end_date
        training_dict['status'] = self.status

        return json.dumps(training_dict)
    



