import typing as t

def f1(a: int) -> None: ...
def f2(a: str) -> None: ...
def f3(a: t.List[int]) -> None: ...
def f4(a: t.Dict[str, str]) -> None: ...
def f5(a: t.Iterable[str]) -> None: ...


def f10():
    x: int
    y: int = 0
    z: str
    w: str = 'Default w'

def f11(a: t.List[t.Union[int, float]]) -> None: ...

NumType = t.Union[str, float]
def f12(b: t.Dict[str, NumType]) -> None: ...


def main():
    f12()

CallbackType = t.Callable[[str, int], str]

TypeAlias = t.List[t.Dict[str, int]]

def work(arg1: str, arg2: int = 0, arg3: t.List[float]) -> float:
    return 1.2

def process(stuff: t.Iterable[t.Union[int, float]]) -> int:
    return [x*2 for x in stuff]

class MyClass:
    items: t.ClassVar[int]
    template: t.ClassVar[str]

obj = MyClass()
obj.items = 20 # Type error

MODE = t.Literal['r', 'rb', 'w', 'wb']
def open_file(file: str, mode: MODE): ...