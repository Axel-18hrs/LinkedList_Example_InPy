from abc import ABC, abstractmethod


class ListOperations(ABC):

    @abstractmethod
    def add(self, value):
        raise NotImplementedError("The 'add' function is not used")

    @abstractmethod
    def delete(self, data):
        raise NotImplementedError("The 'delete' function is not used")

    @abstractmethod
    def transverse(self):
        raise NotImplementedError("The 'transverse' function is not used")

    @abstractmethod
    def transverse_reverse(self):
        raise NotImplementedError("The 'transverse_reverse' function is not used")

    @abstractmethod
    def exist(self, data):
        raise NotImplementedError("The 'exist' function is not used")

    @abstractmethod
    def show(self):
        raise NotImplementedError("The 'show' function is not used")

    @abstractmethod
    def show_reverse(self):
        raise NotImplementedError("The 'show_reverse' function is not used")

    @abstractmethod
    def search(self, data):
        raise NotImplementedError("The 'search' function is not used")

    @abstractmethod
    def is_empty(self):
        raise NotImplementedError("The 'is_empty' function is not used")

    @abstractmethod
    def clear(self):
        raise NotImplementedError("The 'clear' function is not used")
