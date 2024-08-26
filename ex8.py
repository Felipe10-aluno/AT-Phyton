def dobrar_lista(lista): 
  nova_lista = []
  for elemento in lista:
    novo_elemento = elemento * 2 
    nova_lista.append(novo_elemento) 
    return nova_lista 
lista=list()
i=1
while i<=10:
 elem = int(input("Digite um elemento da lista:")) 
 lista.append(elem)
 i+=1 
print(lista) 
nova_lista = dobrar_lista(lista)
print(nova_lista)

#'1 a 9' o codigo basicamente faz a analise dos 10 elementos da lista para a duplicação da mesma
#'10 a 15' o codigo recebe os valores e os imprime na tela, para o resultado 