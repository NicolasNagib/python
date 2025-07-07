from modelos.banco import Banco

class Cliente(Banco):
    def __init__(self, titular, saldo, data_nascimento, tipo_conta):
        super().__init__(titular, saldo, data_nascimento, tipo_conta)

