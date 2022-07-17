from neuro import Neuro

inp = [[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]]
goal_pred = [0, 0, 1]

neuro = Neuro(inp, goal_pred)
neuro.calc(50)
import random
for _ in range(10):
    cvet = random.randint(0, 2)
    svetofor = [0, 0, 0]
    svetofor[cvet] = 1
    print(neuro.neuro_network(svetofor))