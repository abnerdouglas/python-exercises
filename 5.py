def inverter_string(s):
    invertida = ''
    for char in s:
        invertida = char + invertida
    return invertida

string = input("Informe uma string: ")
print("String invertida:", inverter_string(string))

'''
Explicação: A função inverter_string constrói a string invertida 
adicionando cada caractere na posição anterior.
'''