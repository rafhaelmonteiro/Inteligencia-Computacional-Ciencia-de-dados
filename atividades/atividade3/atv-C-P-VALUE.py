from math import comb

# Total de lançamentos da moeda
n = 5

# Probabilidade de cara sob hipótese nula (moeda justa)
p_cara = 0.5

# Todas as possibilidades de resultados possíveis (0 a 5 caras)
# Cada quantidade de caras tem um número de combinações
# Dados os valores conhecidos (por simetria da distribuição binomial)
combinacoes = {
    0: 1,   # 0 caras = 5 coroas
    1: 5,   # 1 cara  e 4 coroas
    2: 10,  # 2 caras e 3 coroas
    3: 10,  # 3 caras e 2 coroas
    4: 5,   # 4 caras e 1 coroa
    5: 1    # 5 caras
}

# Total de possibilidades é 2^5 = 32
total_possibilidades = 2 ** n

# Evento observado: 4 caras e 1 coroa
# Queremos o p-valor = P(4 caras) + P(5 caras) + P(1 cara)
eventos_relevantes = [0, 1, 4, 5]  

# Soma das probabilidades desses eventos
p_valor = sum(combinacoes[k] / total_possibilidades for k in eventos_relevantes)

# explicação passo a passo
print("Hipótese nula H0: a moeda não é especial (P(cara) = 0.5)")
print("Evento observado: 4 caras e 1 coroa")
print(f"Total de possibilidades: {total_possibilidades}")
print("Eventos tão raros ou mais raros que 4 caras:")
for k in eventos_relevantes:
    prob = combinacoes[k] / total_possibilidades
    print(f"- {k} caras: {combinacoes[k]} combinações → P = {prob:.4f}")

print(f"\np-valor = soma das probabilidades = {p_valor:.4f}")

# Condicional com base no valor critico do p-value 0.05 para rejeitar ou nao a hipotese nula
if p_valor < 0.05:
    print("→ p-valor < 0.05: Rejeitamos a hipótese nula. A moeda não é especial.")
else:
    print("→ p-valor ≥ 0.05: Não rejeitamos a hipótese nula. A moeda não é diferente de uma moeda normal.")