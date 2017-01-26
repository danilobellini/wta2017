In [1]: from IPython.lib.pretty import pprint

In [2]: class LogObj(object):
   ...:
   ...:     def __getattr__(self, name):
   ...:         print("__getattr__:"); pprint(locals())
   ...:         return name # Para não lançar AttributeError
   ...:
   ...:     def __setattr__(self, name, value):
   ...:         print("__setattr__:"); pprint(locals())
   ...:         super(LogObj, self).__setattr__(name, value)
   ...:
   ...:     def __delattr__(self, name):
   ...:         print("__delattr__:"); pprint(locals())
   ...:         super(LogObj, self).__delattr__(name)

In [3]: logobj = LogObj()

In [4]: logobj.a = 1
__setattr__:
{'__class__': __main__.LogObj,
 'name': 'a',
 'self': <__main__.LogObj at 0x...>,
 'value': 1}

In [5]: logobj.b = 2
__setattr__:
{'__class__': __main__.LogObj,
 'name': 'b',
 'self': <__main__.LogObj at 0x...>,
 'value': 2}

In [6]: logobj.a += logobj.b
__setattr__:
{'__class__': __main__.LogObj,
 'name': 'a',
 'self': <__main__.LogObj at 0x...>,
 'value': 3}

In [7]: del logobj.b
__delattr__:
{'__class__': __main__.LogObj,
 'name': 'b',
 'self': <__main__.LogObj at 0x...>}

In [8]: vars(logobj)
Out[8]: {'a': 3}

In [9]: logobj.c
__getattr__:
{'name': 'c',
 'self': <...>}
Out[9]: 'c'
