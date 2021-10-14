from typing import Generic, TypeVar

T = TypeVar("T")


class List(Generic[T]):
    # Just raise NotImplementedErrors to make List similar to an interface
    def __init__(self):
        raise NotImplementedError()

    def insert(self, element):
        raise NotImplementedError()

    def append(self, element: T) -> 'NonEmptyList':
        raise NotImplementedError()

    def find(self, element):
        raise NotImplementedError()

    def __str__(self) -> str:
        raise NotImplementedError()


class NonEmptyList(List[T]):
    def __init__(self, data, next: List):
        self.data: T = data
        self.next: List[T] = next

    def append(self, element: T) -> 'NonEmptyList':
        self.next = self.next.append(element)
        return self

    def __str__(self) -> str:
        curr = str(self.data)
        # Recursively get the next element str repr
        rest = str(self.next)

        # Add a space if not last node
        curr += " " if rest != '' else ''
        return curr + rest


class EmptyList(List[T]):
    def __init__(self):
        # Exists to prevent super constructor from executing
        pass

    def append(self, element: T) -> NonEmptyList:
        return NonEmptyList(element, self)

    def __str__(self) -> str:
        return ''
