from typing import Generic, TypeVar

T = TypeVar("T")


class List(Generic[T]):
    # I'll just raise NotImplementedErrors to make List like an interface
    def __init__(self):
        raise NotImplementedError()

    def insert(self, element):
        raise NotImplementedError()

    def append(self, element: T) -> 'NonEmptyList':
        raise NotImplementedError()

    def find(self, element):
        raise NotImplementedError()

    def __str__() -> str:
        raise NotImplementedError()


class NonEmptyList(List[T]):
    def __init__(self, data, next: List):
        self.data: T = data
        self.next: List[T] = next

    def append(self, element: T) -> 'NonEmptyList':
        self.next = self.next.append(element)
        return self


class EmptyList(List[T]):
    def __init__(self):
        # Exists to prevent super constructor from executing
        pass

    def append(self, element: T) -> NonEmptyList:
        return NonEmptyList(element, self)
