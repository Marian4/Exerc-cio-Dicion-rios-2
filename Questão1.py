dias = {}
def adicionarDia(dic,posicao,dia):
  dic[posicao] = dia
def exibirDias(dic):
  for i in range(1,8):
    print(i,"-",end=" ")
    print(dic[i])
op�ao = eval(input("(1)-adicionar dia,(2)-exibir dias:"))
while op�ao == 1 or op�ao == 2:
  if op�ao == 1:
    posi��o = eval(input("Qual a posi��o?"))
    dia = input("Qual o nome do dia?")
    adicionarDia(dias,posi��o,dia)
    print()
    op�ao = eval(input("(1)-adicionar dia,(2)-exibir dias:"))
  elif op�ao == 2:
    exibirDias(dias)
    print()
    op�ao = 0