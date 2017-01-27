WTA2017 - Instrospecção e compilação tardia em Python
=====================================================

Repositório com o código criado para o tutorial "Instrospecção e
compilação tardia em Python" ministrado no Workshop de Tecnologia
Adaptativa de 2017 (WTA2017) na Escola Politécnica da Universidade de
São Paulo (Poli-USP) no dia 2017-01-27.

* Slides:

  http://www.slideshare.net/djsbellini/20170127-wta2017-instrospeco-e-compilao-tardia-em-python-tutorial

* Programação:

  http://lta.poli.usp.br/lta/wta/wta-2017/programacao

Esse tutorial pode ser visto como um complemento ou uma continuação ao
tutorial `Adaptatividade em Python`_ que foi realizado no WTA2015.


Conteúdo
--------

O tutorial foi dividido em 5 partes, na qual as 3 primeiras abordaram
do tema "instrospecção", enquanto as duas últimas abordaram o tema
"compilação tardia":

1. Dicionários
2. Objetos
3. Escopo / Closure
4. Compilação
5. AST (\ *Abtract Syntax Tree*\ )


Outras informações
------------------

Os arquivos de código foram organizados neste repositório iniciando com
dos dígitos, em que o primeiro representa a parte na qual o código
aparece e o segundo é um número de ordem. Arquivos contendo o sufixo
``_ipython`` são o resultado de rodar no IPython cada "bloco" separado
por uma linha em branco do arquivo sem esse sufixo.

O highlighting dos slides foi obtido copiando e colando o resultado do
pygments_ no LibreOffice, utilizando o estilo "xcode":

.. code-block: shell

  pygmentize -O full,style=xcode -o arquivo.rtf arquivo.py

A imagem de fundo, assim como no WTA2015, foi criada utilizando a
AudioLazy_.


----

Criado por Danilo J. S. Bellini


.. _`Adaptatividade em Python`:
  https://github.com/danilobellini/wta2015

.. _pygments:
  http://pygments.org/

.. _AudioLazy:
  https://github.com/danilobellini/audiolazy
