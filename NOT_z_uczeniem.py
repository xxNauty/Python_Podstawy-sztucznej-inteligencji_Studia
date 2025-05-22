class perceptronProsty(object):

    def ustaw_prog(self, T):
        self.T = T

    def ustaw_wagi(self, W):
        self.W = W

    def suma_wazona(self, Xi):
        wynik_sumy_wazonej = 1*self.W[0]
        for index in range(0, len(Xi)):
            wynik_sumy_wazonej += Xi[index]*self.W[index + 1]
        return wynik_sumy_wazonej

    def odpowiedz(self, Xi):
        return 1 if self.suma_wazona(Xi) >= self.T else 0

    def epoka_uczenia(self, X, D):
        for index in range(0, len(X)):
            Xi = X[index]
            Di = D[index]

            Yi = self.odpowiedz(Xi)
            blad = Di - Yi

            self.W[0] = self.W[0] + 1*blad
            for index in range(0, len(Xi)):
                self.W[index + 1] += Xi[index]*blad



NOT_z_uczeniem = perceptronProsty()

NOT_z_uczeniem.ustaw_prog(0.5)
NOT_z_uczeniem.ustaw_wagi([0, 0])

X = [[0], [1]]
D = [1, 0]

#------------------------------------------------

for Xi in X:
    print('X=', Xi, 'Y=', NOT_z_uczeniem.odpowiedz(Xi))

print(NOT_z_uczeniem.W)

#------------------------------------------------

NOT_z_uczeniem.epoka_uczenia(X, D)

for Xi in X:
    print('X=', Xi, 'Y=', NOT_z_uczeniem.odpowiedz(Xi))

print(NOT_z_uczeniem.W)

#------------------------------------------------

NOT_z_uczeniem.epoka_uczenia(X, D)

for Xi in X:
    print('X=', Xi, 'Y=', NOT_z_uczeniem.odpowiedz(Xi))

print(NOT_z_uczeniem.W)

#------------------------------------------------

NOT_z_uczeniem.epoka_uczenia(X, D)

for Xi in X:
    print('X=', Xi, 'Y=', NOT_z_uczeniem.odpowiedz(Xi))

print(NOT_z_uczeniem.W)