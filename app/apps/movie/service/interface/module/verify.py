from abc import ABCMeta, abstractmethod


class MovieVerifyInterface(metaclass=ABCMeta):
    @abstractmethod
    def verify_movie_name(self, name: str) -> bool:
        pass

