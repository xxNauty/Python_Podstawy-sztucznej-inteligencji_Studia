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

X = df.iloc[0:150, [0, 2]].values

for index in range(50, 100):
    X[index][0] += 3
    X[index][1] -= 2.5

D_0 = np.zeros(150)
D_1 = np.zeros(150)
D_2 = np.zeros(150)

for index in range(50):
    D_0[index] = 1
    D_1[index + 50] = 1
    D_2[index + 100] = 1

p0 = perceptronProsty()
p1 = perceptronProsty()
p2 = perceptronProsty()

p0.ustaw_prog(0.5)
p0.ustaw_wagi([0, 0, 0])
p0.ustaw_limit_iteracji(150)

p1.ustaw_prog(0.5)
p1.ustaw_wagi([0, 0, 0])
p1.ustaw_limit_iteracji(150)

p2.ustaw_prog(0.5)
p2.ustaw_wagi([0, 0, 0])
p2.ustaw_limit_iteracji(150)

hist0 = p0.proces_uczenia(X, D_0)
hist1 = p1.proces_uczenia(X, D_1)
hist2 = p2.proces_uczenia(X, D_2)

in0 = [5,1]
print(p0.odpowiedz(in0), p1.odpowiedz(in0), p2.odpowiedz(in0))

in1 = [9,1]
print(p0.odpowiedz(in1), p1.odpowiedz(in1), p2.odpowiedz(in1))

in2 = [8, 7]
print(p0.odpowiedz(in2), p1.odpowiedz(in2), p2.odpowiedz(in2))

# plt.plot(range(len(hist2)), hist2)
# plt.xlabel('Epoka')
# plt.ylabel('Liczba błędnych odpowiedzi')
# plt.show()

# plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='100 - setosa')
# plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='010 - versicolor')
# plt.scatter(X[100:150, 0], X[100:150, 1], color='green', marker='^', label='001 - virginica')
#
# plt.xlabel('sepal length [cm]')
# plt.ylabel('petal length [cm]')
# plt.legend(loc='upper left')
# plt.show()

