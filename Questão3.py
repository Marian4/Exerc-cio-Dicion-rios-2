produtos = {}
def cadastrarProduto(dic,produto,preço):
  dic[produto] = preço
  print("Produto adicionado.\n")
def exibirProdutos(dic):
  print()
  print("-------------------------------------------------")
  produtos = dic.keys()
  for i in produtos:
    print(i,end=" ")
    print("- %.2f"%dic[i])
  print("-------------------------------------------------")
def removerProduto(dic,produto):
  del dic[produto]
  print("Produto removido.\n")
def exibirCaroProduto(dic):
  produto = ''
  caro = 0
  for i in dic:
    if dic[i] > caro:
      caro = dic[i]
      produto = i
  print("-------------------------------------------------")
  print(produto,'-',caro)
  print("-------------------------------------------------")
  print()
def exibirBaratoProduto(dic):
  produto = ''
  barato = 1000
  for i in dic:
    if dic[i] < barato :
      barato = dic[i]
      produto = i
  print("-------------------------------------------------")
  print(produto,'-',barato)
  print("-------------------------------------------------")
  print()
def menu():
  opçao = eval(input("(1)-Adicionar produto.\n(2)-Listar produtos.\n(3)-Remover produto.\n(4)-Exibir produto mais caro.\n(5)-Exibir produto mais barato.\n(6)-Sair.\n"))
  return opçao
opçao = menu()
while opçao > 0 and opçao < 6:
  if opçao == 1:
    produto = input("Produto:")
    preço = float(input("preço:"))
    cadastrarProduto(produtos,produto,preço)
    opçao = menu()
  elif opçao == 2:
    exibirProdutos(produtos)
    opçao = menu()
  elif opçao == 3:
    produto = input("Produto a ser removido:")
    removerProduto(produtos,produto)
    opçao = menu()
  elif opçao == 4:
    exibirCaroProduto(produtos)
    opçao = menu()
  elif opçao == 5:
    exibirBaratoProduto(produtos)
    opçao = menu()
print("Programa encerrado.")