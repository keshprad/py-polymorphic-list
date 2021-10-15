from typing import Generic, TypeVar

T = TypeVar("T")


class PolymorphicList(Generic[T]):
    """A generic class to represent a polymorphic list that stores objects of type T

    This class throws errors for every method because it is not meant to be instantiated. 
    It is meant to act like an interface, which the NonEmptyList and EmptyList classes extend.

    Args:
        Generic (T): The type of the objects that will be stored in the list.
    """
    def __init__(self):
        """Init function throws NotImplementedError to prevent instantiation of a List object.

        Raises:
            NotImplementedError: Prevent instantiation of a list object.
        """
        raise NotImplementedError()

    def __str__(self) -> str:
        """Creates a string for the object.

        Returns:
            str: string representation of the object.
        """
        raise NotImplementedError()

    def __eq__(self, other: object) -> bool:
        """Checks if the current object is equal to the given object.

        Args:
            other (object): the input object to compare to.

        Returns:
            bool: a bool indication whether the current object is equal to the given object
        """
        raise NotImplementedError()

    def __contains__(self, element: T) -> bool:
        """Overrides membership op to check whether an element exists in the list.

        Args:
            element (T): The element to look for.

        Returns:
            bool: a boolean indication of whether the element was found.
        """
        raise NotImplementedError()

    def size(self) -> int:
        """Finds the size/length of the list

        Returns:
            int: The size/length of the list
        """
        raise NotImplementedError()

    def append(self, element: T) -> 'NonEmptyList':
        """Appends an element to the beginning of the list

        Args:
            element (T): The element to be appended

        Returns:
            NonEmptyList: Object for the new list after append operation.
        """
        raise NotImplementedError()

    def prepend(self, element: T) -> 'NonEmptyList':
        """Prepends an element to the beginning of the list

        Args:
            element (T): The element to be prepended

        Returns:
            NonEmptyList: Object for the new list after prepend operation.
        """
        raise NotImplementedError()


class NonEmptyList(PolymorphicList[T]):
    """Represents a NonEmptyList with a T type data, and a reference to the next node in the abstraction

    Args:
        PolymorphicList ([type]): Extends the PolymorphicList class to have a generic type T.
    """
    def __init__(self, data, next: PolymorphicList):
        """Initializes the state of the NonEmptyList.

        Args:
            data ([type]): The data stored in this node
            next (PolymorphicList): Reference to the next node
        """
        self.data: T = data
        self.next: PolymorphicList[T] = next
        self.length: int = self.next.length + 1

    def __str__(self) -> str:
        """Creates a string representation for the NonEmptyList

        Returns:
            str: The string representation of each object in the list separated with arrows.
        """
        # String for the curr data
        curr = str(self.data)
        # Recursively get the next element str
        rest = str(self.next)

        # Add a space if not last node
        curr += " -> " if rest != '' else ''
        return curr + rest

    def __eq__(self, other: object) -> bool:
        """Recursively checks if the entire NonEmptyList is equal to another input object.

        Args:
            other (object): The input object to compare to.

        Returns:
            bool: a bool indication whether the current object is equal to the given object
        """
        if (isinstance(other, NonEmptyList) and self.data == other.data):
            return self.next == other.next
        return False

    def __contains__(self, element: T) -> bool:
        """Overrides membership op to check whether an element exists in the list.

        Args:
            element (T): The element to look for.

        Returns:
            bool: a boolean indication of whether the element was found.
        """
        if self.data == element:
            return True
        return element in self.next

    def size(self) -> int:
        """Finds the size/length of the list

        Returns:
            int: The size/length of the list
        """
        return self.length

    def append(self, element: T) -> 'NonEmptyList':
        """Appends an element to the beginning of the list

        Args:
            element (T): The element to be appended

        Returns:
            NonEmptyList: Object for the new list after append operation.
        """
        self.next = self.next.append(element)
        self.length += 1
        return self

    def prepend(self, element: T) -> 'NonEmptyList':
        """Prepends an element to the beginning of the list

        Args:
            element (T): The element to be prepended

        Returns:
            NonEmptyList: Object for the new list after prepend operation.
        """
        return NonEmptyList(element, self)


class EmptyList(PolymorphicList[T]):
    """Represents a EmptyList, the last node in the abstraction, which has no data or next pointer

    Args:
        PolymorphicList ([type]): Extends the PolymorphicList class to have a generic type T.
    """
    def __init__(self):
        """Initializes the state of the EmptyList.
        """
        self.length: int = 0
        pass

    def __str__(self) -> str:
        """Creates a string representation for the EmptyList

        Returns:
            str: an empty string, since this is an EmptyList object
        """
        return ''

    def __eq__(self, other: object) -> bool:
        """Checks if this EmptyList is equal to another input object.

        Args:
            other (object): The input object to compare to.

        Returns:
            bool: a bool indication whether the current object is equal to the given object
        """
        # TODO: Check if there is a way to check that other isinstance with EmptyList[T]
        return isinstance(other, EmptyList)

    def __contains__(self, element: T) -> bool:
        """Overrides membership op to check whether an element exists in the list.

        Args:
            element (T): The element to look for.

        Returns:
            bool: a boolean indication of whether the element was found.
        """
        return False

    def size(self) -> int:
        """Finds the size/length of the list

        Returns:
            int: The size/length of the list
        """
        return self.length

    def append(self, element: T) -> NonEmptyList:
        """Appends an element to the beginning of the list

        Args:
            element (T): The element to be appended

        Returns:
            NonEmptyList: Object for the new list after append operation.
        """
        return NonEmptyList(element, self)

    def prepend(self, element: T) -> 'NonEmptyList':
        """Prepends an element to the beginning of the list

        Args:
            element (T): The element to be prepended

        Returns:
            NonEmptyList: Object for the new list after prepend operation.
        """
        return NonEmptyList(element, self)