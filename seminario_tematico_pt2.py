import time

def particao(vetor, inicio, final):
  pivo = vetor[final]
  time.sleep(1.0)
  i = inicio - 1

  for j in range(inicio, final):
    if vetor[j] <= pivo:
      i += 1
      vetor[i], vetor[j] = vetor[j], vetor[i]
  vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
  return i + 1

def quick_sort(vetor, inicio, final):
  print(*vetor, sep=' - ')
  if inicio < final:
    posicao = particao(vetor, inicio, final)
    # Esquerda
    quick_sort(vetor, inicio, posicao - 1)
    # Direito
    quick_sort(vetor, posicao + 1, final)
  return vetor


Fila = ['39','19','40','850','60',] 
menu = '---------- MENU FILA ----------\n\
1 - Inserir na Fila \n\
2 - Remover da Fila \n\
3 - Informar um resumo dos dados da Fila \n\
4 - Informar o PRIMEIRO da Fila \n\
5 - Indicar se a fila está vazia \n\
6 - Terminar o sistema \n\
7 - Ordenar a Fila (QUICK)'

def Gerenciador_de_fila(*args, **kwargs):
    for pessoa in args:
        Fila.append(pessoa)
    if kwargs.get('remover'):
        Fila.pop(0) if Fila else print('\nA fila está vazia')
    if kwargs.get('quantidade'):
        print('\nA lista está vazia!') if len(Fila) == 0 else print(f'\nA lista tem {len(Fila)} pessoas')
    if kwargs.get('consultar_primeiro'):
        print(Fila[0])
    if kwargs.get('informar_resumo'):
        print(*Fila, sep=' - ' )
    if kwargs.get('ordenar_fila'):
        quick_sort(Fila, 0, len(Fila) - 1)

while True:
    print(menu)
    opcao = int(input('Escolha uma opção: '))
    print(f'{"-"*65}')
    Gerenciador_de_fila(str(input('Digite o nome da pessoa: '))) if opcao == 1 else ''
    Gerenciador_de_fila(remover=True) if opcao == 2 else ''
    Gerenciador_de_fila(informar_resumo=True) if opcao == 3 else ''
    Gerenciador_de_fila(consultar_primeiro=True) if opcao == 4 else ''
    Gerenciador_de_fila(quantidade=True) if opcao == 5 else ''
    if opcao == 6:
        break
    Gerenciador_de_fila(ordenar_fila=True) if opcao == 7 else ''
    print('Opção inválida') if opcao not in range(1,8) else ''
