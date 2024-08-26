def insertion_sort(lista): 
  for i in range(1, len(lista)): 
    chave = lista[i]
    j = i - 1 
    while j >= 0 and chave < lista[j]:
       lista[j + 1] = lista[j]
       j -= 1
       lista[j + 1] = chave 
lista=list()
i=1 
while i<=10: 
 elem = int(input("Digite um elemento da lista:"))
 lista.append(elem) 
 i+=1 
 print(lista) 
 insertion_sort(lista) 
 print(lista)

 
 #'1 a 9' o código faz os processos para a inserção da lista
 #'10 a 17'o código imprimi na tela os resultados da lista para o usuário 