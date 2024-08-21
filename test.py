from dominio.user import user
from dominio.tabuadas import tabuada
# Inserir nomes
print("Digite seu nome")
nome = input()

print("Digite o sobre nome")
sobre = input()

usuario = user(nome, sobre)

print(f'''Olá SR {usuario.exibir_user()}, seja muito Bem-Vindo. 
Digite o nome da sua tabuada de 1 a 10.''')

escolha = int(input())

print("=========================")

if escolha == 1:
    tabuadaDo1 = tabuada(1)
    tabuadaDo1.tabuada1_do_1()
elif escolha == 2:
    tabuadaDo2 = tabuada(2)
    tabuadaDo2.tabuada2_do_2()
elif escolha == 3:
    tabudaDo3 = tabuada(3)
    tabudaDo3.tabuada3_do_3()
elif escolha == 4:
    tabuadaDo4 = tabuada(4)
    tabuadaDo4.tabuada4_do_4()
elif escolha == 5:
    tabuadaDo5 = tabuada(5)
    tabuadaDo5.tabuada5_do_5()
elif escolha == 6:
    tabuadaDo6 = tabuada(6)
    tabuadaDo6.tabuada6_do_6()
elif escolha == 7:
    tabuadaDo7 = tabuada(7)
    tabuadaDo7.tabuada7_do_7()
elif escolha == 8:
    tabuadaDo8 = tabuada(8)
    tabuadaDo8.tabuada8_do_8()
elif escolha == 9:
    tabuadaDO9 = tabuada(9)
    tabuadaDO9.tabuada9_do_9()
elif escolha == 10:
    tabuadaDO10 = tabuada(10)
    tabuadaDO10.tabuada10_do_10()
else:
    print("Opção Invalida.")

print("=========================")