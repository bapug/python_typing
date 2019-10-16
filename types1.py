import typing as t
from typing import NewType, Callable, Generator, NamedTuple

from modules.module import Person

AType = NewType('AType', int)
PersonType = NewType('PersonType', Person)
UserId = NewType('UserId', int)


print(UserId(1234))


class DoSomething:

    def show_name(self, p: Person) -> None:
        print(p.fullname)


def callback(get_next: Callable[[], str]) -> None:
    [c for c in get_next()]


#class BadType(UserId): pass


class Employee(NamedTuple):
    """ Simple Employee Object """
    name: str
    id: int = 3

print(Employee.__annotations__)

print(Employee('Guido'))
print(Employee('Ed', 5))


class Point2D(t.TypedDict):
    x: int
    y: int
    label: str

a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
b: Point2D = {'z': 3, 'label': 'bad'}           # Fails type check

UserId = t.NewType('UserId', int)

def get_employee(id: UserId) -> Employee:
    """ Lookup employee and return object"""
    pass

employee: Employee = get_employee(UserId(1234))
