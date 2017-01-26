In [1]: class CountGets(object):
   ...:     count = 0
   ...:
   ...:     def __getattr__(self, name):
   ...:         self.count += 1
   ...:         return name
   ...:

In [2]: cg = CountGets()

In [3]: hasattr(cg, "count")
Out[3]: True

In [4]: cg.count
Out[4]: 0

In [5]: hasattr(cg, "a")
Out[5]: True

In [6]: cg.count
Out[6]: 1

In [7]: hasattr(CountGets, "a")
Out[7]: False

In [8]: cg.count
Out[8]: 1
