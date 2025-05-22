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

OR = perceptronProsty()
OR.ustaw_prog(0.5)
OR.ustaw_wagi([0, 1, 1])

print(OR.odpowiedz([0, 0]))
print(OR.odpowiedz([0, 1]))
print(OR.odpowiedz([1, 0]))
print(OR.odpowiedz([1, 1]))