import numpy as np
from scipy.stats import t, norm

# dados da frequência cardíaca de 50 mulheres
batimentos = np.array([
    100, 74, 74, 78, 70, 67, 85, 72, 69, 65,
    80, 79, 81, 90, 91, 87, 86, 83, 68, 70,
    75, 77, 72, 66, 85, 76, 88, 71, 70, 74,
    69, 67, 73, 80, 78, 76, 71, 90, 92, 88,
    84, 82, 89, 73, 65, 66, 78, 85, 90, 75
])

n = len(batimentos)
media = np.mean(batimentos)
desvio_padrao = np.std(batimentos, ddof=1)
grau_liberdade = n - 1  

# Nível de confiança
nivel_confianca = 0.95
t_critical = t.ppf(nivel_confianca, grau_liberdade)

# Intervalo de confiança
margem_erro = t_critical * (desvio_padrao / np.sqrt(n))
limite_inferior = media - margem_erro
limite_superior = media + margem_erro

print("Intervalo de Confiança para a MÉDIA:")
print(f"Média amostral: {media:.2f}")
print(f"IC 95%: ({limite_inferior:.2f}, {limite_superior:.2f})")


# Intervalo de Confiança para PROPORÇÃO
n = len(batimentos)
bpm_limite = 100

# número de mulheres com BPM >= 100
sucessos = np.sum(batimentos >= bpm_limite)
p = sucessos / n

confidence_level = 0.95

# z crítico
z_critical = norm.ppf(confidence_level)

# Intervalo de confiança
erro_padrao = np.sqrt(p * (1 - p) / n)
margem_erro = z_critical * erro_padrao
limite_inferior = p - margem_erro
limite_superior = p + margem_erro

print("Intervalo de Confiança para a PROPORÇÃO:")
print(f"Proporção amostral (p): {p:.4f}")
print(f"z crítico: {z_critical:.4f}")
print(f"IC 95%: ({limite_inferior:.4f}, {limite_superior:.4f})")