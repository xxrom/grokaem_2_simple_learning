# gradient learning method

weight = 0.5
input = 0.5
goal_pred = 0.8

for iteration in range(20):
  pred = input * weight
  error = (pred - goal_pred)**2
  # THIS change the game!
  # gradient decant (scaled on the way!)
  direction_and_amount = (pred - goal_pred) * input

  weight -= direction_and_amount

  print('iteration %d, cubeError: %f, gradientError: %f, prediction: %f' %
        (iteration, error, direction_and_amount, pred))
