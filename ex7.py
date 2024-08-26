def maior_menor(lista):
 maior = lista[0]
 menor = lista[0] 
 for elemento in lista:
   if elemento > maior:
    maior = elemento 
   elif elemento < menor: menor = elemento
 return maior, menor
lista=list()
i=1 
while i<=10: 
 elem = int(input("Digite um elemento da lista:")) 
 lista.append(elem)
 i+=1
 print(lista) 
maior, menor = maior_menor(lista) 
print("Maior:", maior) 
print("Menor:", menor)


#'1 a 11' o codigo pede 10 valores e analisa, e os organiza na lista, separando o maior e o menor, para a exibição mais tarde no código
#'12 a 18' ele pede os valores e os imprime na tela para apresentar o resultado