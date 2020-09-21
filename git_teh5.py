class person():

    def __init__(self, name, age):
        self.name = ""
        self.age = ""

    def __str__(self):
        return (f' Name:{self.name} /n Age:{self.age}')