from Cliente import Cliente
from Conta import Conta

class Main:
    pass

client= Cliente("Joao", "1198989-8989")

conta= Conta(client._nome, 5050, 1000)

conta.deposita(158)
conta.saque(58)
conta.extrato()

#print("Titular: ",conta.titular(),"\nConta: ",conta.numero(), "\nSeu Saldo é: ", "R$",conta.saldo)