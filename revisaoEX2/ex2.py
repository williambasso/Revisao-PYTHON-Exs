from model.produtos import Produtos
from dao.produtos_dao import ProdutosDao
lista = [['frutas', 'verduras', 'legumes', 'preço'],
         ['mamão', 'abacaxi', 'laranja', 'uva', 'pera', 'maçã', 'vergamota'],
         ['alface crespa', 'alface lisa', 'rúcula',
             'almeirão', 'repolho', 'salsinha', 'couve'],
         ['feijão', 'ervinha', 'lentilha', 'vagem',
             'feijão branco', 'grão de bico', 'soja'],
         [[10.00, 2.56, 5.25, 9.5, 10.05, 15, 5.75], [2.99, 2.95, 3.5, 3.25, 5.89, 2.9, 2.5],
          [9.0, 5.0, 7.5, 1.75, 10.9, 5.99, 3.55]
          ]
         ]

#variavel de controle para percorrer na lista
v = 0

#instanciando objeto do produto_dao/produtos
dao = ProdutosDao()
produtos = Produtos()

# FOR PARA FRUTAS!
#pegando o preço da fruta
for i in lista[4][0]:
    #setando a lista das frutas
    f = produtos.set_frutas(lista[1][v])
    #setando a lista do preço das frutas
    p = produtos.set_precos(i)
    #verificando se já existe no BD
    if dao.has_nome(produtos.frutas):
        print('Já existe cadastros!')
        break
    else:
        inserir = dao.inserir_frutas(produtos.frutas,produtos.preco)
    v += 1
    


# # FOR PARA VERDURAS!
v = 0
for i in lista[4][1]:
    f = produtos.set_verduras(lista[2][v])
    p = produtos.set_precos(i)

    if dao.has_nome(produtos.verduras):
        print('Já existe cadastros!')
        break
    else:
        inserir = dao.inserir_verduras(produtos.verduras,produtos.preco)
    v += 1
    
    


# # FOR PARA LEGUMES!
v = 0
for i in lista[4][2]:
    f = produtos.set_legumes(lista[3][v])
    p = produtos.set_precos(i)

    if dao.has_nome(produtos.legumes):
        print('Ja existe cadastros!')
        break
    else:
        inserir = dao.inserir_legumes(produtos.legumes,produtos.preco)
    
    v += 1

def listar_tipo(produtos):
    while True:
        print('BEM VINDO, selecione a opcao desejada')
        print('1 = Frutas')
        print('2 = Legumes')
        print('3 = Verduras')
        opcao = int(input())
        if opcao == 1:
            print(produtos.listar(opcao))
            print()
        elif opcao == 2:
            print(produtos.listar(opcao))
            print()
        elif opcao == 3:
            print(produtos.listar(opcao))
            print()
        else:
            break
        



listar_tipo(dao)
            

