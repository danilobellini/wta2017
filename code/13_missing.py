class FibDict(dict):

    def __missing__(self, key):
        if key < 0:
            raise KeyError(key)
        return self[key - 1] + self[key - 2]

fibd = FibDict({0: 0, 1: 1})

fibd[2], fibd[3], fibd[4], fibd[5], fibd[6], fibd[7]

fibd

fibd[-1]

3 in fibd
