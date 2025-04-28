# sample distribution and sampling distribution

# A partir do que foi feito na Atividade 2 
# “Considerando o primeiro trabalho, defina um experimento em que dados são coletados de uma variável de interesse do seu trabalho”, 
# crie  uma população artificial dessa variável com uma distribuição Gaussiana e demonstre 
# sample distribution and sampling distribution. Faça avaliações de probabilidade de possíveis eventos.

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

def main():
    np.random.seed(42)

    populacao = np.random.normal(loc=10, scale=5, size=500)
    populacao = np.clip(populacao, 0, 27)

    plt.figure(figsize=(10,6))
    sns.histplot(populacao, bins=20, kde=True, color='skyblue', stat='density')
    plt.title('Distribuição da População - Pontuações PHQ-9')
    plt.xlabel('Pontuação PHQ-9')
    plt.ylabel('Densidade')
    plt.grid(True)
    plt.show()

    amostra = np.random.choice(populacao, size=30, replace=False)

    plt.figure(figsize=(10,6))
    sns.histplot(amostra, bins=10, kde=True, color='green', stat='density')
    plt.title('Distribuição Sample - Pontuações PHQ-9')
    plt.xlabel('Pontuação Questionario PHQ-9')
    plt.ylabel('Densidade')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
  main()