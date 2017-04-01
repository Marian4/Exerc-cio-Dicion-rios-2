dias = {}
def adicionarDia(dic,posicao,dia):
  dic[posicao] = dia
def exibirDias(dic):
  for i in range(1,8):
    print(i,"-",end=" ")
    print(dic[i])
opçao = eval(input("(1)-adicionar dia,(2)-exibir dias:"))
while opçao == 1 or opçao == 2:
  if opçao == 1:
    posição = eval(input("Qual a posição?"))
    dia = input("Qual o nome do dia?")
    adicionarDia(dias,posição,dia)
    print()
    opçao = eval(input("(1)-adicionar dia,(2)-exibir dias:"))
  elif opçao == 2:
    exibirDias(dias)
    print()
    opçao = 0