import json

with open("dados.json", "r") as f:
    dados = json.load(f)
    
# Encontra o menor e maior valor do faturamento    
vals = [dado["valor"] for dado in dados if dado["valor"] != 0]
val_menor = min(vals)
val_maior = max(vals)

# Calcula a média mensal
soma = sum(vals)
dias_c_faturamento = len(vals)
media_m = soma / dias_c_faturamento

# Conta o número de dias com faturamento acima da média mensal
dias_acima = sum(1 for valor in vals if valor > media_m)

print(f"menor valor de faturamento: {val_menor:.2f}")
print(f"Maior valor de faturamento: {val_maior:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima}")
