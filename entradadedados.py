# ENTRADA DE DADOS

cliente = input("Qual o nome do cliente? ")
total = input("Qual o valor total? ")
txentrega = 15
vTot = float(total) + txentrega

# COMANDOS
print(cliente)
print(f"O valor total do(a) cliente {cliente} foi: {vTot}")