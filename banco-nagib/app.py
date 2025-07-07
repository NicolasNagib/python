from modelos.cliente import Cliente



def main():
        resposta = "S"

        print("-="*20)
        print("Banco Nagib")
        print("-="*20)

        # print("""
        #         [1] Criar uma nova conta
        #         [2] Acessar uma conta
        #       """)
        # acao =input("Escolha uma ação, para prosseguir: ")        

        nome  = input("Insira o seu nome: ")
        saldo = float(input("Insira o saldo inicial: "))
        data_nascimento = input("Insira sua data de nascimento: ")
        
        while True:
            print("""
            [1] Corrente
            [2] Poupança
            """)
            tipo_conta = input("Qual o tipo da conta?: ")

            if tipo_conta == "1":
                cliente = Cliente(nome, saldo, data_nascimento, "Corrente")
                break

            elif tipo_conta == "2":
                cliente = Cliente(nome, saldo, data_nascimento, "Poupança")
                break

            else:
                print("Ocorreu um erro, tente novamente")
        cliente.criarConta()
            
        while resposta == "S":
                print("""
                    [1] Sacar dinheiro
                    [2] Realizar um depósito
                    [3] consultar rendimentos(caso a conta seja poupança)
                    [4] sair
                """)
                escolher_acao = input("Qual ação você deseja realizar? ")

                if escolher_acao == "1":
                    valor_saque = float(input("Insira o valor a ser sacado: "))
                    cliente.sacar(valor_saque)
                
                elif escolher_acao == "2":
                    valor_deposito = float(input("Insira o valor a ser depositado: "))
                    cliente.depositar(valor_deposito)
                elif escolher_acao == "3":
                    if cliente._tipo_conta == "Poupança":
                        print(f"Seu dinheiro rendeu R${cliente._saldo * 0.05}")
                        print(f"Saldo atual: {cliente._saldo + cliente._saldo * 0.05}")
                    else:
                        print("Sua conta não possui rendimento")
                elif escolher_acao == "4":
                    break
                else:
                    print("Escolha uma ação válida")
                resposta = input("Deseja realizar mais alguma ação? ").upper()
        print("Até mais")
        


        # # if segunda_acao == "1":
    

if __name__ == '__main__':
    main()