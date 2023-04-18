# valor de faturamento mensal de cada estado
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

# cálculo do valor total mensal
valor_total = sp + rj + mg + es + outros

# cálculo do perc de representação de cada estado
perc_sp = (sp / valor_total) * 100
perc_rj = (rj / valor_total) * 100
perc_mg = (mg / valor_total) * 100
perc_es = (es / valor_total) * 100
perc_outros = (outros / valor_total) * 100

# exibição dos resultados
print(f"Perc de representação de SP: {perc_sp:.2f}%")
print(f"Perc de representação de RJ: {perc_rj:.2f}%")
print(f"Perc de representação de MG: {perc_mg:.2f}%")
print(f"Perc de representação de ES: {perc_es:.2f}%")
print(f"Perc de representação de outros estados: {perc_outros:.2f}%")