In [1]: d = {"nome": "Danilo",
   ...:      "twitter": "@danilobellini"}

In [2]: d["nome"]
Out[2]: 'Danilo'

In [3]: del d["twitter"]

In [4]: len(d) # Tamanho (número de pares)
Out[4]: 1

In [5]: d["sobrenome"] = "J. S. Bellini"

In [6]: d["sobrenome"] = d["sobrenome"].split()[-1]

In [7]: d
Out[7]: {'nome': 'Danilo', 'sobrenome': 'Bellini'}
