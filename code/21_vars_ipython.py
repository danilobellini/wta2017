In [1]: class Usuário(object):
   ...:
   ...:     def __init__(self, nome, twitter=None):
   ...:         self.nome = nome
   ...:         self.twitter = twitter

In [2]: obj = Usuário("Danilo", "@danilobellini")

In [3]: obj.nome
Out[3]: 'Danilo'

In [4]: vars(obj)
Out[4]: {'nome': 'Danilo', 'twitter': '@danilobellini'}

In [5]: vars(obj) is obj.__dict__
Out[5]: True

In [6]: dir(obj)
Out[6]:
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'nome',
 'twitter']

In [7]: type(obj)
Out[7]: __main__.Usuário

In [8]: vars(Usuário)
Out[8]:
mappingproxy({'__dict__': <attribute '__dict__' of 'Usuário' objects>,
              '__doc__': None,
              '__init__': <function __main__.Usuário.__init__>,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'Usuário' objects>})

In [9]: Usuário.mro()
Out[9]: [__main__.Usuário, object]
