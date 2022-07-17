from neuro import Neuro

inp = [8.4, 0.24, 1.1]
goal_pred = [1]

neuro = Neuro(inp, goal_pred)
neuro.calc(5)
print(neuro)
