from IPython.lib.pretty import pprint


class LogObj(object):

    def __getattr__(self, name):
        print("__getattr__:"); pprint(locals())
        return name # Para não lançar AttributeError

    def __setattr__(self, name, value):
        print("__setattr__:"); pprint(locals())
        super(LogObj, self).__setattr__(name, value)

    def __delattr__(self, name):
        print("__delattr__:"); pprint(locals())
        super(LogObj, self).__delattr__(name)


logobj = LogObj()

logobj.a = 1

logobj.b = 2

logobj.a += logobj.b

del logobj.b

vars(logobj)

logobj.c
