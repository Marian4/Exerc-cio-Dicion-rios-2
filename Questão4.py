turmas ={}
def calcularMedia(dic,nomeTurma,matricula):
  for a in dic[nomeTurma]:
    if a[0] == matricula:
      notas = a[1]
      soma = 0 
      for i in notas:
        soma += i 
      media = soma/len(notas)
      a.append(media)
  print("Média:%.1f"%media)
  print()
def adicionarTurma(dic,nomeTurma):
  dic[nomeTurma] = []
  print("Turma adicionada.")
  print()
def adicionarAlunoNotas(dic,nomeTurma,matricula,listaNotas):
  aluno = [matricula,listaNotas]
  dic[nomeTurma].append(aluno)
  print("Aluno(a) e notas adicionados.")
  print()
def CalcularMediaTurma(dic,nomeTurma):
  soma = 0
  alunos = 0
  for b in dic[nomeTurma]:
    soma += b[2]
    alunos += 1
  mediaTurma = soma/alunos
  print("Média da Turma:%.1f"%mediaTurma)
  print()
def menu():
  opçao = eval(input("(1)-Adicionar Turma.\n(2)-Adicionar Aluno e Notas.\n(3)-Calcular média de um Aluno.\n(4)-Calcular média de uma Turma.\n(5)-Sair.\nO que você deseja fazer?"))
  return opçao
valor = menu()
while valor >0 and valor <5:
  if valor == 1:
    nomeTurma = input("Nome da turma:")
    adicionarTurma(turmas,nomeTurma)
    valor = menu()
  elif valor == 2:
    nomeTurma = input("Digite o nome da turma na qual deseja adicionar esse aluno(a):")
    matricula = input("Digite a matricula do aluno(a):")
    notas = []
    quantNotas = eval(input("Quantas notas o aluno(a) tem?"))
    for k in range(quantNotas):
      if k == 0:
        nota = float(input("Primeira nota:"))
        notas.append(nota)
      else:
        nota = float(input("Próxima nota:"))
        notas.append(nota)
    adicionarAlunoNotas(turmas,nomeTurma,matricula,notas)
    valor = menu()
  elif valor == 3:
    matricula = input("Digite a matricula do aluno(a):")
    turma = input("Digite a turma do aluno(a):")
    calcularMedia(turmas,turma,matricula)
    valor = menu()
  elif valor == 4:
    print()
    print("-->Lembrando que para calcular a média da turma, a média de todos os alunos já deverão ter sido calculadas.")
    print()
    nomeTurma = input("Nome da Turma:")
    CalcularMediaTurma(turmas,nomeTurma)
    valor = menu()
print()
print("Programa encerrado.")
