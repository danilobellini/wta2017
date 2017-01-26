class GetAttributeLen(object):

    def __getattribute__(self, name):
        print("__getattribute__ {}".format(name))
        return super().__getattribute__(name)

    def __len__(self):
        return len(vars(self))


obj = GetAttributeLen()

obj.a = 1

obj.b = 2

obj.a += obj.b

len(obj)
