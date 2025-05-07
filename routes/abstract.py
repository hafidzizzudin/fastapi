from abc import ABC, abstractmethod


class AbstractRouter(ABC):
    @abstractmethod
    def init(self):
        pass
