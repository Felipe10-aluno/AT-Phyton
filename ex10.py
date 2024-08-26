def obter_ultimo_elemento(lista): 
  if lista: 
    return lista[-1]
  else: return None 
lista=list()
i=1 
while i<=5: 
 elem = int(input("Digite um elemento da lista:"))
 lista.append(elem)
 i+=1 
 print(lista) 
 ultimo_elemento = obter_ultimo_elemento(lista) 
 print("Último elemento da lista:", ultimo_elemento)


#'1 a 7' ele basicamente faz o sistema de lista, e retorna o último elemento
#'8 a 13' o código basicamente imprime os resultados para o usuário