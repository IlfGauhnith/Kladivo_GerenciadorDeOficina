class UniqueObjectViolated(Exception):
    def __init__(self):
        self.message = 'This object already exists in table.'

    def __str__(self):
        return f'Unique Object Constraint Violated: {self.message}'


class IndexUnrelatedToAnyObject(Exception):

    def __init__(self):
        self.message = 'Index not related to any object in the given table.'

    def __str__(self):
        return f'Index Unrelated To Any Object In Table: {self.message}'