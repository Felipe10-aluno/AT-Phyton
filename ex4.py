def maior3(a, b, c):
 if a >= b and a >= c:
   return a 
 elif b >= c: 
   return b
 else: return c

n1=int(input("Digite um número:")) 
n2=int(input("Digite um número:")) 
n3=int(input("Digite um número:")) 
resultado = maior3(n1,n2,n3) 
print(resultado)


#'2 a 6': ele realiza a equação para descobrir qual será o maior número
#'8 a 10': ele recebe os números
#'11 a 12' ele imprime o resultado

