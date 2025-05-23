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

        return historia_uczenia

AND = perceptronProsty()

AND.ustaw_prog(0.5)
AND.ustaw_wagi([0.3, -0.5, 0.2])

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
D = [0, 0, 0, 1]

historia_uczenia = AND.proces_uczenia(X, D)
print(historia_uczenia)



