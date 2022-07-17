DEFAULT_ALPHA = 0.01


class Neuro:
    def __init__(self, in_put: list, out_put: list, alpha: float = None):
        self.in_put = in_put
        self.out_put = out_put
        self.alpha = alpha or DEFAULT_ALPHA
        self.weight = [[1 for i in range(len(in_put))] for j in range(len(out_put))]
        self.pred = None
        self.error = None
        self.delta = None
        self.weight_delta = None

    def calc(self, count_iter: int = 10000):
        for iteration in range(count_iter):

            self.pred = self.neuro_network(self.in_put, self.weight)
            self.error = [0 for i in range(len(self.in_put))]
            self.delta = [0 for i in range(len(self.in_put))]
            self.weight_delta = [[1 for i in range(len(self.in_put))] for j in range(len(self.out_put))]

            for i in range(len(self.out_put)):
                self.delta[i] = self.pred[i] - self.out_put[i]
                self.error[i] = self.delta[i] ** 2
                for j in range(len(self.delta)):
                    self.weight_delta[i][j] = self.in_put[j] * self.delta[i]

            for i in range(len(self.weight)):
                for j in range(len(self.weight[0])):
                    self.weight[i][j] -= self.weight_delta[i][j] * self.alpha

    def neuro_network(self, inp, weight):
        output = [0 for i in range(len(self.out_put))]

        for i in range(len(weight)):
            output[i] = self.w_sum(inp, weight[i])

        return output

    @staticmethod
    def w_sum(a, b):
        output = 0

        for i in range(len(a)):
            output += a[i]*b[i]

        return output

    def __str__(self):
        str = ''
        for key, item in self.__dict__.items():
            str += f'{key}: {item}\n'
        return f"{str}"
