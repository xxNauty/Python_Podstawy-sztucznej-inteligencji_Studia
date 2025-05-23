import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class perceptronProsty(object):

    def ustaw_prog(self, T):
        self.T = T

    def ustaw_wagi(self, W):
        self.W = W

    def suma_wazona(self, Xi):
        wynik_sumy_wazonej = 1 * self.W[0]
        for index in range(0, len(Xi)):
            wynik_sumy_wazonej += Xi[index] * self.W[index + 1]
        return wynik_sumy_wazonej

    def odpowiedz(self, Xi):
        return 1 if self.suma_wazona(Xi) >= self.T else 0

    def epoka_uczenia(self, X, D):
        liczba_bledow = 0
        for index in range(0, len(X)):
            Xi = X[index]
            Di = D[index]

            Yi = self.odpowiedz(Xi)
            blad = Di - Yi

            self.W[0] = self.W[0] + 1 * blad
            for index in range(0, len(Xi)):
                self.W[index + 1] += Xi[index] * blad
            liczba_bledow += 1 if blad != 0.0 else 0
        return liczba_bledow

    def proces_uczenia(self, X, D):
        historia_uczenia = []

        while 1:
            liczba_blednych_odpowiedzi = self.epoka_uczenia(X, D)
            historia_uczenia.append(liczba_blednych_odpowiedzi)
            if liczba_blednych_odpowiedzi == 0.0:
                break

            if len(historia_uczenia) >= self.n_iter:
                break

        return historia_uczenia

    def ustaw_limit_iteracji(self, n_iter):
        self.n_iter = n_iter

link = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

df = pd.read_csv(link, header=None, encoding='utf-8')

X = df.iloc[0:100, [0, 2]].values

plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='0 - setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='0 - setosa')

plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()

D = df.iloc[0:100, 4].values
D = np.where(D == 'Iris-setosa', 0, 1)

neuron = perceptronProsty()
neuron.ustaw_prog(0.5)
neuron.ustaw_wagi([0, 0, 0])
neuron.ustaw_limit_iteracji(50)

historia_uczenia = neuron.proces_uczenia(X, D)
# print(historia_uczenia)

print(neuron.odpowiedz([5.25, 1.0]))
print(neuron.odpowiedz([5.0, 4.0]))