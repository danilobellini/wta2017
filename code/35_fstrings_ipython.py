In [1]: data = {"linguagem": "Python"}

In [2]: nome = "Exemplo"

In [3]: f'Tutorial de {3 + 2} partes sobre {data["linguagem"]}'
Out[3]: 'Tutorial de 5 partes sobre Python'

In [4]: # Sem f-strings, seria necessário:
   ...: "Tutorial de {} partes sobre {data[linguagem]}".format(3 + 2, **locals())
Out[4]: 'Tutorial de 5 partes sobre Python'

In [5]: # Representação, como repr(linguagem)
   ...: f"Agora o {nome!r} está entre aspas simples!"
Out[5]: "Agora o 'Exemplo' está entre aspas simples!"

In [6]: # Formatação, sufixo ":3.2f" como no str.format
   ...: f"Número {len(nome):3.2f} com duas casas decimais..."
Out[6]: 'Número 7.00 com duas casas decimais...'
