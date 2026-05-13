from abc import ABC, abstractmethod

class FileReader(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def parse(self):
        pass


class TextFileReader(FileReader):

    def read(self):
        print("Reading text file...")

    def parse(self):
        print("Parsing text file...")


class CSVFileReader(FileReader):

    def read(self):
        print("Reading CSV file...")

    def parse(self):
        print("Parsing CSV file...")


readers = [TextFileReader(), CSVFileReader()]

for r in readers:
    r.read()
