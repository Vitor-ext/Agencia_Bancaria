from Cliente import Cliente
from Conta import Conta

class Main:
    print("Bem Vindo ao Nosso APP !! ")


print("Insira seu nome: ")
nome = (str(input()))

print("Insira seu Telefone: ")
telefone = (int(input()))

print("Insira sua Conta: ")
numero = (int(input()))

client= Cliente(nome, telefone)

conta= Conta(client._nome, numero, 5000)

print("Titular: ",conta.titular(),"\nConta: ",conta.numero(), "\nSeu Saldo é: ", "R$",conta.saldo)

print("\nQual ação deseja Seguir ?",
      "\n 1 - Deposito",
      "\n 2 - Saque",
      "\n 3 - Extrato")

acao = int(input())

if (acao == 1):
    print("Qual valor deseja Depositar ?")
    valor = int(input())
    conta.deposita(valor)

if (acao == 2):
    print("Qual valor deseja Sacar ?")
    valor = int(input())
    conta.saque(valor)

if (acao == 3):
    conta.extrato()

if (acao != 1 and acao != 2 and acao != 3 ):
    print("Opção Invalida !")






