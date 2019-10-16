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


