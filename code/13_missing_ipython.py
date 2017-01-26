In [1]: class FibDict(dict):
   ...:
   ...:     def __missing__(self, key):
   ...:         if key < 0:
   ...:             raise KeyError(key)
   ...:         return self[key - 1] + self[key - 2]

In [2]: fibd = FibDict({0: 0, 1: 1})

In [3]: fibd[2], fibd[3], fibd[4], fibd[5], fibd[6], fibd[7]
Out[3]: (1, 2, 3, 5, 8, 13)

In [4]: fibd
Out[4]: {0: 0, 1: 1}

In [5]: fibd[-1]
    [...]
KeyError: -1

In [6]: 3 in fibd
Out[6]: False
