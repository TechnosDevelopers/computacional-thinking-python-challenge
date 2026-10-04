# 3 Funcionalidades

# Cadastro RAPIDO do doador
# Listar dados doador
# Registrar doação
# Consultar doação


programa_aberto = True
email = ""
telefone = ""
valor_doacao = 0

while programa_aberto:

    print("\n------------------MENU----------------------")
    print("-------------ESCOLHA UMA OPÇÃO--------------\n")

    print("1 - Cadastro")
    print("2 - Listar dados do doador")
    print("3 - Doar!")
    print("4 - Consultar doação")
    print("5 - Sair\n")

    opcao = int(input("Digite aqui: "))

    match opcao:
        case 1:
            print("-------------------------------")
            print("Você entrou no cadastro!")
            email = str(input("Digite seu email : "))
            telefone = str(input("Digite seu número (xx xxxxx-xxxx) : "))
            print("Cadastro realizado!")

        case 2:
            print("-------------------------------")
            print("Você entrou em listar dados do doador!")

            if email == "" and telefone == "":
                print("O doador não se cadastrou!")
            else:
             print(f"Email do doador: {email}")
             print(f"Telefone do doador: {telefone}")

        case 3:
            print("-------------------------------")


            if email == "" and telefone == "":
                print("O doador não se cadastrou!")

            else:
             print("Você entrou em doar!")

             valor_doacao = int(input("Qual valor você quer doar? "))

             if valor_doacao > 0:

                   s_ou_n = str(input(f"Você confiram que quer doar {valor_doacao} reais ? (S ou N) \n"))

                   if s_ou_n.capitalize() == "S" :
                    forma_de_pagamento = str(input("Qual será a forma de pagamento? \n"))
                    print(f"Você doou R$ {valor_doacao} reais no {forma_de_pagamento}")

                   elif s_ou_n.capitalize() == "N":
                    print("Doação cancelada.")
             else:
                    print("Valor invalido!")






        case 4:
            print("-------------------------------")
            print("Você entrou em consultar doação!")

            if valor_doacao == 0:
                print("Nenhuma doação foi realizada.")
            else:
                print(f"Valor da última doação: R$ {valor_doacao}")


        case 5:
            print("Você fechou o programa")
            programa_aberto = False


        case _:
            print("-------------------------------")
            print("Esse número é invalido!")
