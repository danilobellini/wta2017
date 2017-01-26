class Usuário(object):

    def __init__(self, nome, twitter=None):
        self.nome = nome
        self.twitter = twitter

obj = Usuário("Danilo", "@danilobellini")

obj.nome

vars(obj)

vars(obj) is obj.__dict__

dir(obj)

type(obj)

vars(Usuário)

Usuário.mro()
