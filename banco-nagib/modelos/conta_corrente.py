from modelos.banco import Banco

class ContaCorrente(Banco):
    def __init__(self, titular, saldo, tipo_conta, numero_conta):
        super().__init__(titular, saldo, tipo_conta)
        self._numero_conta = numero_conta