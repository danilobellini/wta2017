In [1]: class GetAttributeLen(object):
   ...:
   ...:     def __getattribute__(self, name):
   ...:         print("__getattribute__ {}".format(name))
   ...:         return super().__getattribute__(name)
   ...:
   ...:     def __len__(self):
   ...:         return len(vars(self))
   ...:

In [2]: obj = GetAttributeLen()

In [3]: obj.a = 1

In [4]: obj.b = 2

In [5]: obj.a += obj.b
__getattribute__ a
__getattribute__ b

In [6]: len(obj)
__getattribute__ __dict__
Out[6]: 2
