from abc import ABC, abstractmethod

class Device(ABC):

    @abstractmethod
    def connect(self):
        pass


class Phone(Device):
    def connect(self):
        print("Phone connected.")


class Tablet(Device):
    def connect(self):
        print("Tablet connected.")


d1 = Phone()
d2 = Tablet()

d1.connect()
d2.connect()