class LogDict(dict):

    def __getitem__(self, key):
        print("__getitem__: {}".format(locals()))
        return super(LogDict, self).__getitem__(key)

    def __setitem__(self, key, value):
        print("__setitem__: {}".format(locals()))
        super(LogDict, self).__setitem__(key, value)

    def __delitem__(self, key):
        print("__delitem__: {}".format(locals()))
        super(LogDict, self).__delitem__(key)


logd = LogDict({1: 1, 2: 2, 3: 3})

del logd[1]

logd[2] += logd[3]

logd
