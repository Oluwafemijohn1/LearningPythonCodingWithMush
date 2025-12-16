from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    """Exception raised for invalid operations."""
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")
        self.opened = True
        print("Stream opened.")

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is not opened.")
        self.opened = False
        print("Stream closed.")

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def read(self):
        if not self.opened:
            raise InvalidOperationError("Cannot read from a closed stream.")
        print(f"Reading from {self.filename}.")


class NetworkStream(Stream):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def read(self):
        if not self.opened:
            raise InvalidOperationError("Cannot send data to a closed stream.")
        print(f"Sending to {self.url}.")


stream = FileStream("example.txt")
stream.open()
stream.read()
stream.close()
