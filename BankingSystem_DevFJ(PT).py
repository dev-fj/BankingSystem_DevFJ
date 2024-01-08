#%%



def SistemaBancario():

    global extrato, saldo, limite

    while True:
            try:
                
                print("""
Se deseja Sacar -> Digite [1]
Se deseja Depositar -> Digite [2]
Se deseja acessar o Extrato -> Digite [3]
Para sair -> Digite [0]
                      
                      """)
                print("".center(80,"+"))
                print()
                t1 = int(input("Escolha uma opção: \n>"))

                if t1 == 1:
                    
                    if limite ==0:
                        templete("Você já chegou no limite de saques diários (3 por dia)")

                    elif saldo == 0:
                        templete("Você não possue dinheiro para sacar")
                    elif saldo > 0 and limite > 0:
                        while True:
                            try:
                                print()
                                print("Opção de saque".upper())
                                saque = float(input("""
Quanto deseja sacar? 
                                                    
Caso deseje voltar para o menu inicial, 
escreva qualquer letra e tecle Enter. 
                                                    
>"""))

                                if saque > 500:
                                    templete("Saque no máximo de R$500.00")

                                elif saque <= 0:
                                    templete("O valor do saque precisa ser maior que R$ 0,00")

                                elif (saque > 0) and (saldo < saque):
                                    templete("Boa tentativa.")

                                elif (saque > 0) and (saldo >=saque):
                                    saldo -= saque
                                    extrato += f"-R${saque:.2f}\n"
                                    limite -= 1

                                    templete(f"""
Saque de R${saque:.2f} efetuado. 
Saldo atual: R${saldo:.2f}""")
                                    break

                            except ValueError:
                                break
                    # else:
                    #     None

                elif t1 == 2:

                    while True:
                        try:
                            print()
                            print("Opção de depósito\n".upper())
                            deposito = float(input("""
Informe o valor do depósito: \n
                                                   
Caso deseje voltar para o menu inicial, 
escreva qualquer letra e tecle Enter.
                                                   
>"""))
                            


                            if deposito >= 0:
                                saldo += deposito
                                extrato += f"+R${deposito:.2f}\n"
                                templete(f"""
Depósito de R${deposito:.2f} efetuado.
Saldo atual: R${saldo:.2f}""")
                                break
                            else:
                                print("""
Valor incorreto. 
Tente um valor numérico positivo.
Exemplo: 50.00""")
                                
                        except ValueError:
                            break

                elif t1 == 3:

                    if extrato == "":
                        templete("""
                                    EXTRATO

                                    R$ 0,00
                                 """)

                    else:
                        templete(f"""
EXTRATO:
                                 
{extrato}

Saldo total de: R${saldo:.2f}""")
                        

                elif t1 == 0:
                    templete("""
                                Obrigado por vir. 
                        Seu Dinheiro está seguro conosco. 
                                 Volte sempre.""")
                    break

                else:
                    print("""
Eu preciso de um número entre 0 e 3
Favor digitar a opção desejada sem o uso de [ ].
Por exemplo: 1""")

            except ValueError:
                print("""
Eu preciso de um número.
Favor digitar a opção desejada sem o uso de [ ].
Por exemplo: 1 """)

    return

def templete(y):
    x = ""
    x += y
    logo1 = " Banco Python "
    print()
    print(logo1.center(80,'+'))
    print()
    print(x.center(80))
    print()
    print("".center(80,'+'))
    print()
    print()






extrato = ""
limite = 3
saldo = 0

templete("Nós do banco Python lhe damos boas-vindas ao banco dos seu $onho$ !")


SistemaBancario()