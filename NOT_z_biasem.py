class perceptronProsty(object):

    def ustaw_prog(self, T):
        self.T = T

    def ustaw_wagi(self, W):
        self.W = W

    def suma_wazona(self, Xi):
        return Xi[0]*self.W[1] + 1*self.W[0]

    def odpowiedz(self, Xi):
        return 1 if self.suma_wazona(Xi) >= self.T else 0

NOT_z_biasem = perceptronProsty()

NOT_z_biasem.ustaw_prog(0.5)
NOT_z_biasem.ustaw_wagi([1, -1])

print(NOT_z_biasem.odpowiedz([1]))
print(NOT_z_biasem.odpowiedz([0]))