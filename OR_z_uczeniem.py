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



OR_z_uczeniem = perceptronProsty()

OR_z_uczeniem.ustaw_prog(0.5)
OR_z_uczeniem.ustaw_wagi([0.3, -0.5, 0.2])

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
D = [0, 1, 1, 1]

#------------------------------------------------

for Xi in X:
    print('X=', Xi, 'Y=', OR_z_uczeniem.odpowiedz(Xi))

print(OR_z_uczeniem.W)

#------------------------------------------------

OR_z_uczeniem.epoka_uczenia(X, D)

for Xi in X:
    print('X=', Xi, 'Y=', OR_z_uczeniem.odpowiedz(Xi))

print(OR_z_uczeniem.W)

#------------------------------------------------

OR_z_uczeniem.epoka_uczenia(X, D)

for Xi in X:
    print('X=', Xi, 'Y=', OR_z_uczeniem.odpowiedz(Xi))

print(OR_z_uczeniem.W)

#------------------------------------------------

OR_z_uczeniem.epoka_uczenia(X, D)

for Xi in X:
    print('X=', Xi, 'Y=', OR_z_uczeniem.odpowiedz(Xi))

print(OR_z_uczeniem.W)