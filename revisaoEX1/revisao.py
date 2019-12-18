from model.pessoa import Pessoa
def lista_pessoa():
    cab = ['nome', 'telefone', 'email','idade']
    pessoa = [
                ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]   
            ]
    
    maior = []
    menor = []

    for i in range(7):
        lista_pessoa = []
        for n in range(4):
            lista_pessoa.append(pessoa[n][i])
        if int(lista_pessoa[3]) >= 18:
            p = Pessoa(lista_pessoa[0],lista_pessoa[1],lista_pessoa[2],lista_pessoa[3])
            maior.append(p)
            print(maior)
        elif int(lista_pessoa[3]) <18:
            p = Pessoa(lista_pessoa[0],lista_pessoa[1],lista_pessoa[2],lista_pessoa[3])
            menor.append(p)
        
    return [maior, menor]



listas = lista_pessoa()

for lista in listas:
    for l in lista:
        print(f"\033[1;32m ---------------------- \033[m")
        print(f"Nome:{l.nome}")
        print(f"Telefone:{l.telefone}")
        print(f"Email:{l.email}")
        print(f"Idade:{l.idade}")
        if int(l.idade) >= 18:
           print("Maior de Idade!\n")
        else:
            print("Menor de Idade!")  
            

# 1 - Usando as 2 listas, fazer uma função que crie retorne uma lista com objetos de classe  Pessoa
# com os dados das pessoas com idade maior ou igua a 18 anos
#
#  2 - Imprima a lista resultante com um for imprimindo os dados da classe para cada pessoa criada 
# (usando o f-string)