# Questão 4: Percentual de representação por estado

# Faturamento por estado
estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calculando o total
total_faturamento = sum(estados.values())

# Calculando o percentual por estado
for estado, valor in estados.items():
    percentual = (valor / total_faturamento) * 100
    print(f"{estado}: {percentual:.2f}%")
