weight = 0.5
goal_pred = 0.8
inp = 0.5
alpha_const = 0.01
for _ in range(20):
    pred = inp * weight
    error = (pred - goal_pred) ** 2
    direction_and_amount = (pred - goal_pred) * inp
    weight -= direction_and_amount*alpha_const
    
    print("Error:", error, "Prediction:", pred, "Weight:", weight)