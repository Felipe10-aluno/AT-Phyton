def converter_quilometros_para_metros(quilometros):
    metros = quilometros * 1000 
    return metros 
try:
    quilometros = float(input("Digite a distância em quilômetros: ")) 
    metros = converter_quilometros_para_metros(quilometros)
    print("metros:", metros) 
except ValueError: 
    print("Entrada inválida!")


#'1 a 3' ele faz a conversão de quilometros para metros algebricamante
#'5' o codigo pede o valor
#'6 a 9' ele imprime o resultado na tela
