data = {"linguagem": "Python"}

nome = "Exemplo"

f'Tutorial de {3 + 2} partes sobre {data["linguagem"]}'

# Sem f-strings, seria necessário:
"Tutorial de {} partes sobre {data[linguagem]}".format(3 + 2, **locals())

# Representação, como repr(linguagem)
f"Agora o {nome!r} está entre aspas simples!"

# Formatação, sufixo ":3.2f" como no str.format
f"Número {len(nome):3.2f} com duas casas decimais..."
