empresa = {}
def adicionarFuncionario(dic,matricula,nome):
  dic[matricula] = nome
  print("Funcionário adicionado.")
def buscarFuncionario(dic,matricula):
  print("Funcionário:",dic[matricula])
def exibirFuncionarios(dic):
  print()
  matriculas = dic.keys()
  for i in matriculas:
    print(i,end=" ")
    print("-",dic[i])
opçao = eval(input("(1)-Adicionar funcionário.\n(2)-Buscar funcionário.\n(3)-Exibir funcionários.\n(4)-Sair.\n"))
while opçao >0 and opçao < 4:
  if opçao == 1:
    matricula = input("Matrícula:")
    nome = input("Nome Completo:")
    adicionarFuncionario(empresa,matricula,nome)
    opçao = eval(input("\n(1)-Adicionar funcionário.\n(2)-Buscar funcionário.\n(3)-Exibir funcionários.\n(4)-Sair.\n"))
  elif opçao == 2:
    matricula = input("Digite a matrícula do fucionário:")
    buscarFuncionario(empresa,matricula)
    opçao = eval(input("\n(1)-Adicionar funcionário.\n(2)-Buscar funcionário.\n(3)-Exibir funcionários.\n(4)-Sair.\n"))
  elif opçao == 3:
    exibirFuncionarios(empresa)
    opçao = eval(input("\n(1)-Adicionar funcionário.\n(2)-Buscar funcionário.\n(3)-Exibir funcionários.\n(4)-Sair.\n"))
print("\nPrograma encerrado.")