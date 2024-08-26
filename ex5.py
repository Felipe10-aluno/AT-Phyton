def mdc(a, b):
   if b == 0: 
     return a 
   else: 
     return mdc(b, a % b) 
num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:")) 
resultado = mdc(num1, num2)
print("MDC:", resultado)


#'1 a 5' ele faz a definição algébrica de mmc
#'6 a 7' ele recebe os números
#'8 a 9' ele imprime o resultado 