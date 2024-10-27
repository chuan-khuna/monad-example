from typing import Generic, TypeVar, Callable

# function input T -> output S
T = TypeVar('T')  # value type T
S = TypeVar('S')  # value type S

E = TypeVar('E')  # error type E


class Maybe(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def is_nothing(self) -> bool: ...
    def is_just(self) -> bool: ...
    def bind(self, f: Callable[[T], 'Maybe[S]']) -> 'Maybe[S]': ...

    def __rshift__(self, f: Callable[[T], 'Maybe[S]']) -> 'Maybe[S]':
        # a >> func = a.bind(func)
        return self.bind(f)


class Just(Maybe[T]):
    """Wrapper for a value of type T"""

    def __init__(self, value: T):
        self.value = value
        self.error = None

    def is_nothing(self) -> bool:
        return False

    def is_just(self) -> bool:
        return True

    def __repr__(self) -> str:
        return f'Just({self.value.__repr__()})'

    def bind(self, f: Callable[[T], Maybe[S]]) -> Maybe[S]:
        return f(self.value)


class Nothing(Maybe):
    """
    Wrapper for an error message (str)
    """

    def __init__(self, value: str):
        # use value to store error message
        self.value = value
        self.error = value

    def is_nothing(self) -> bool:
        return True

    def is_just(self) -> bool:
        return False

    def __repr__(self) -> str:
        return 'Nothing'

    def bind(self, f: Callable[[T], Maybe[S]]) -> Maybe[S]:
        # return self, which is Nothing(error_message)
        return self
