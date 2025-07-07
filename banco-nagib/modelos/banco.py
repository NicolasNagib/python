from datetime import date

class Banco():
    def __init__(self, titular, saldo, data_nascimento, tipo_conta):
        self._titular      = titular
        self._saldo        = saldo
        self._tipo_conta   = tipo_conta.title()
        self._data_nascimento = date(int(data_nascimento[4:]), int(data_nascimento[2:4]), int(data_nascimento[0:2]))
        # self._tipo_conta = tipo_conta

    
    def __str__(self):
        return f'O titular da conta é {self._titular} e o saldo dele é {self._saldo}'
    
    def depositar(self, deposito):
        self._saldo += deposito
        print(f'Valor de R${deposito} depositado com sucesso! Saldo atual: R${self._saldo}')
    
    def sacar(self, saque):
        self._saldo -= saque
        print(f'Valor sacado com sucesso! Saldo atual: R${self._saldo}')
    
    def criarConta(self):   
        if self._tipo_conta =='Corrente':
            print(f'Conta Corrente criada com sucesso! Titular: {self._titular}, Saldo inicial: R${self._saldo}') # numero da conta {self._numero_conta}
        elif self._tipo_conta == 'Poupança':
            print(f'Conta Poupança criada com sucesso! Titular: {self._titular}, Saldo inicial: R${self._saldo} ') # numero da conta {self._numero_conta}
        
    # def acessarConta(self, acesso_conta):
        
        pass