d = {"nome": "Danilo",
     "twitter": "@danilobellini"}

d["nome"]

del d["twitter"]

len(d) # Tamanho (número de pares)

d["sobrenome"] = "J. S. Bellini"

d["sobrenome"] = d["sobrenome"].split()[-1]

d
