from dataclasses import dataclass # dataclass 

class Context:
    path: str
    fname: str
    train: object
    test: object
    id: str
    label: str
    
    @property
    def path(self) -> str: return self._path
    
    @path.setter
    def path(self, path: str): self._path = path
    