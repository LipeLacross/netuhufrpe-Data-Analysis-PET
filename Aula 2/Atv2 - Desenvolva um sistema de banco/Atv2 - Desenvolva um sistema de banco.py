'''Desenvolva um sistema de banco, onde um banco pode ter até 1000 contas. Ele deve ser capaz de criar e desativar uma conta. E ainda, realizar depósitos e saques nestas contas.
A interação deve ser feita por linha de texto:
Criar conta - solicita as informações do cliente
Desativar conta - solicita o numero da conta
Saque - solicita o numero da conta e a quantia, e deve verificar se há saldo suficiente
Deposito - solicita o número da conta e o valor depositado
Sair

Considere o Mesmo Problema
Mas agora temos dois tipos de conta
Conta Corrente
Que permite as mesmas funções anteriores
Conta Poupança
Que permite as mesmas funções
Permite a função de render 1%

Altere o código para que TODO tipo de conta (Conta Corrente, Poupança, etc.) deveram descontar 0,1% do que foi depositado.
Altere o código para incluir uma nova classe chamada ContaBonificada
Depositar acumula um bônus equivalente a 0,01% do valor depositado
Método renderBonus que CREDITA no saldo a quantidade que houver no BÔNUS, bem como zera a quantidade de bônus acumulado.
Somente a classe ContaBonificada pode acumula o bônus
'''
from Atv2lib import Banco

def imprimirMenu():
    print("Menu")
    print("0 - Sair")
    print("1 - Criar uma Nova Conta")
    print("2 - Consultar Saldo Conta")
    print("3 - Depositar na Conta")
    print("4 - Sacar na Conta")
    print("5 - Render Poupanca")
    print("6 - Render Bonificada")
    print("7 - Excluir Conta")
    choice = int(input("digite a opção desejada:"))
    return choice

print("Bem-vindo")
bancoLacross = Banco("Lacross")
escolha = imprimirMenu()

while escolha > 0 or escolha < 0:
    if escolha == 1:
        # criar uma conta
        print("Criando Conta...")
        print("1 - Conta Corrente")
        print("2 - Conta Poupanca")
        print("3 - Conta Bonificada")
        opcao = int(input("digite o tipo da conta:"))
        while opcao > 1 or opcao < 4:
            if opcao == 1:
                numConta = bancoLacross.criarConta()
                print("Conta criada:", numConta)
                break
            elif opcao == 2:
                numConta = bancoLacross.criarPoupanca()
                print("Conta criada:", numConta)
                break
            elif opcao == 3:
                numConta = bancoLacross.criarBonificada()
                print("Conta criada:", numConta)
                break
            else:
                print("Número inválido.")
                opcao = int(input("digite o tipo da conta:"))
    elif escolha == 2:
        # consultar saldo
        print("Consultando Saldo...")
        numConta = int(input("digite o numero da conta:"))
        saldo = bancoLacross.consultaSaldo(numConta)
        if saldo == -1:
            print("Conta não encontrada.")
        else:
            print("o saldo da conta", numConta, "é", saldo, "R$.")
    elif escolha == 3:
        # depositar para uma conta
        print("Depositando Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja depositar:"))
        saldo = bancoLacross.depositar(numConta, valor)
        if saldo == False:
            print("Conta não encontrada.")
        else:
            print("Valor Depositado.")
    elif escolha == 4:
        # sacar de uma conta
        print("Sacando da Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja sacar:"))
        resp = bancoLacross.sacar(numConta, valor)
        if resp:  # significa resp == True
            print("Valor Sacado")
        else:
            print("Saldo Insuficiente")
    elif escolha == 5:
        # render poupança
        print("Rendendo Poupanca...")
        numConta = int(input("digite o numero da conta poupanca:"))
        resp = bancoLacross.renderPoupanca(numConta)
        if resp:
            print("Poupanca com novo saldo")
        else:
            print("Conta não encontrada ou a conta não é poupança.")
    elif escolha == 6:
        # render bonificada
        print("Rendendo bônus...")
        numConta = int(input("digite o numero da conta bonificada:"))
        resp = bancoLacross.renderBonus(numConta)
        if resp:
            print("Um valor bônus foi adicionado ao saldo da conta.")
        else:
            print("Conta não encontrada ou a conta não é bonificada.")
    elif escolha == 7:
        # Excluir conta
        print("Iniciando exclusão...")
        numConta = int(input("digite o numero da conta:"))
        resp = bancoLacross.excluirConta(numConta)
        if resp:
            print("A conta foi excluída com sucesso.")
        else:
            print("A conta não existe.")       
    else:
        print("Escolha inválida")
    
    escolha = imprimirMenu()
    