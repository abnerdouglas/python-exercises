import json

dados = '''
{
    "faturamento_diario": [200.0, 0.0, 150.0, 300.0, 0.0, 50.0, 600.0]
}
'''

faturamento = json.loads(dados)["faturamento_diario"]

# Filtra os dias com faturamento
faturamento_filtrado = [valor for valor in faturamento if valor > 0]

menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)
media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

dias_acima_da_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)

print(f"Menor faturamento: R${menor_faturamento}")
print(f"Maior faturamento: R${maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

'''
Explicação: O código filtra os dias com faturamento e, em seguida, calcula o menor e maior valor, 
a média mensal e o número de dias com faturamento superior à média.
'''