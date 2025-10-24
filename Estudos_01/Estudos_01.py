"""Exemplo variavel global"""

codigo = "123321" # Variavel global

def testar():
    print(f'dentro da funcao testar(), codigo = {codigo}') # Acessando variavel global
testar()
print(f'fora da funcao testar(), codigo = {codigo}') # Acessando variavel global