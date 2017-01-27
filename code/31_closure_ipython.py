In [1]: def itemgetter(key):
   ...:     return lambda obj: obj[key]

In [2]: data = {"a": 1, "b": 2, 3: 4}

In [3]: values = [5, 10, 15, 20]

In [4]: itemgetter("b")(data)
Out[4]: 2

In [5]: get3 = itemgetter(3)

In [6]: get3(values)
Out[6]: 20

In [7]: get3(data)
Out[7]: 4
