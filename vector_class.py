import itertools

class Vetor(list):
    def __add__(self, other):
        if len(self) == len(other):
            result = Vetor([s + o for s, o in itertools.izip(self, other)])
        else:
            raise ValueError("Vector size mismatch")
        return result
    def __mul__(self, other):
        if isinstance(other,