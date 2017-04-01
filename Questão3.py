produtos = {}
def cadastrarProduto(dic,produto,pre�o):
  dic[produto] = pre�o
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
  op�ao = eval(input("(1)-Adicionar produto.\n(2)-Listar produtos.\n(3)-Remover produto.\n(4)-Exibir produto mais caro.\n(5)-Exibir produto mais barato.\n(6)-Sair.\n"))
  return op�ao
op�ao = menu()
while op�ao > 0 and op�ao < 6:
  if op�ao == 1:
    produto = input("Produto:")
    pre�o = float(input("pre�o:"))
    cadastrarProduto(produtos,produto,pre�o)
    op�ao = menu()
  elif op�ao == 2:
    exibirProdutos(produtos)
    op�ao = menu()
  elif op�ao == 3:
    produto = input("Produto a ser removido:")
    removerProduto(produtos,produto)
    op�ao = menu()
  elif op�ao == 4:
    exibirCaroProduto(produtos)
    op�ao = menu()
  elif op�ao == 5:
    exibirBaratoProduto(produtos)
    op�ao = menu()
print("Programa encerrado.")