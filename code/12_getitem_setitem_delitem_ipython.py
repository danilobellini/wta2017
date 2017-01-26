In [1]: class LogDict(dict):
   ...:
   ...:     def __getitem__(self, key):
   ...:         print("__getitem__: {}".format(locals()))
   ...:         return super(LogDict, self).__getitem__(key)
   ...:
   ...:     def __setitem__(self, key, value):
   ...:         print("__setitem__: {}".format(locals()))
   ...:         super(LogDict, self).__setitem__(key, value)
   ...:
   ...:     def __delitem__(self, key):
   ...:         print("__delitem__: {}".format(locals()))
   ...:         super(LogDict, self).__delitem__(key)

In [2]: logd = LogDict({1: 1, 2: 2, 3: 3})

In [3]: del logd[1]
__delitem__: {'self': {1: 1, 2: 2, 3: 3}, 'key': 1}

In [4]: logd[2] += logd[3]
__getitem__: {'self': {2: 2, 3: 3}, 'key': 2}
__getitem__: {'self': {2: 2, 3: 3}, 'key': 3}
__setitem__: {'self': {2: 2, 3: 3}, 'key': 2, 'value': 5}

In [5]: logd
Out[5]: __getitem__: {'self': {2: 5, 3: 3}, 'key': 2}
__getitem__: {'self': {2: 5, 3: 3}, 'key': 3}
{2: 5, 3: 3}
