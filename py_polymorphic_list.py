from typing import Generic, TypeVar

T = TypeVar("T")


class PolymorphicList(Generic[T]):
    """A generic class to represent a polymorphic list that stores objects of type T

    This class throws errors for every method because it is not meant to be instantiated. 
    It is meant to act like an interface, which the NonEmptyList and EmptyList classes extend.

    Args:
        Generic ([type]): The type of the objects that will be stored in the list.
    """
    def __init__(self):
        """Init function throws NotImplementedError to prevent instantiation of a List object.

        Raises:
            NotImplementedError: Prevent instantiation of a list object.
        """
        raise NotImplementedError()

    def __str__(self) -> str:
        raise NotImplementedError()

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError()

    def prepend(self, element):
        raise NotImplementedError()

    def append(self, element: T) -> 'NonEmptyList':
        raise NotImplementedError()

    def find(self, element: T) -> bool:
        raise NotImplementedError()


class NonEmptyList(PolymorphicList[T]):
    def __init__(self, data, next: PolymorphicList):
        self.data: T = data
        self.next: PolymorphicList[T] = next

    def __str__(self) -> str:
        # String for the curr data
        curr = str(self.data)
        # Recursively get the next element str
        rest = str(self.next)

        # Add a space if not last node
        curr += " " if rest != '' else ''
        return curr + rest

    def __eq__(self, other: object) -> bool:
        if (isinstance(other, NonEmptyList) and self.data == other.data):
            return self.next == other.next
        return False

    def append(self, element: T) -> 'NonEmptyList':
        self.next = self.next.append(element)
        return self

    def find(self, element: T) -> bool:
        if self.data == element:
            return True
        return self.next.find(element)


class EmptyList(PolymorphicList[T]):
    def __init__(self):
        # Exists to prevent super constructor from executing
        pass

    def __str__(self) -> str:
        return ''

    def __eq__(self, other: object) -> bool:
        # TODO: Check if there is a way to check that other isinstance with EmptyList[T]
        return isinstance(other, EmptyList)

    def append(self, element: T) -> NonEmptyList:
        return NonEmptyList(element, self)

    def find(self, element: T) -> bool:
        return False
