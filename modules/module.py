class Person:

    def __init__(self, first: str, last: str, email: str):
        self.first = first
        self.last = last
        self.email = email

    @property
    def fullname(self) -> str:
        return self.first + ' ' + self.last

