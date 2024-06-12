from abc import ABCMeta, abstractmethod


class MovieRepoInterface(metaclass=ABCMeta):
    @abstractmethod
    def check_in(self):
        pass
