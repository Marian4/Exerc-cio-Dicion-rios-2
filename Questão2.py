empresa = {}
def adicionarFuncionario(dic,matricula,nome):
  dic[matricula] = nome
  print("Funcion�rio adicionado.")
def buscarFuncionario(dic,matricula):
  print("Funcion�rio:",dic[matricula])
def exibirFuncionarios(dic):
  print()
  matriculas = dic.keys()
  for i in matriculas:
    print(i,end=" ")
    print("-",dic[i])
op�ao = eval(input("(1)-Adicionar funcion�rio.\n(2)-Buscar funcion�rio.\n(3)-Exibir funcion�rios.\n(4)-Sair.\n"))
while op�ao >0 and op�ao < 4:
  if op�ao == 1:
    matricula = input("Matr�cula:")
    nome = input("Nome Completo:")
    adicionarFuncionario(empresa,matricula,nome)
    op�ao = eval(input("\n(1)-Adicionar funcion�rio.\n(2)-Buscar funcion�rio.\n(3)-Exibir funcion�rios.\n(4)-Sair.\n"))
  elif op�ao == 2:
    matricula = input("Digite a matr�cula do fucion�rio:")
    buscarFuncionario(empresa,matricula)
    op�ao = eval(input("\n(1)-Adicionar funcion�rio.\n(2)-Buscar funcion�rio.\n(3)-Exibir funcion�rios.\n(4)-Sair.\n"))
  elif op�ao == 3:
    exibirFuncionarios(empresa)
    op�ao = eval(input("\n(1)-Adicionar funcion�rio.\n(2)-Buscar funcion�rio.\n(3)-Exibir funcion�rios.\n(4)-Sair.\n"))
print("\nPrograma encerrado.")