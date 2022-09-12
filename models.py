
# create a class which describes your data model

class Task():
    def __init__(self, title):
        self.id = None
        self.title = title
        self.date = None
    
    # method to represent the data
    def __repr__(self):
        return f'{self.title} created on {self.date}'