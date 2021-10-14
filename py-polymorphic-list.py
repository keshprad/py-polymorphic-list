from typing import Generic, TypeVar

T = TypeVar("T")


class List(Generic[T]):
    def __init__(self):
        raise NotImplementedError()

    def insert(self, element):
        raise NotImplementedError()

    def append(self, element):
        raise NotImplementedError()

    def find(self, element):
        raise NotImplementedError()


class NonEmptyList(List):
    def __init__(self, data, next: List):
        self.data: T = data
        self.next: List[T] = next


class EmptyList(List):
    def __init__(self, ):
        self.data: T = None
        self.next: List[T] = None
