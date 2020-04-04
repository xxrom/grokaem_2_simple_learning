weight = 0.5
input = 0.5
goal_prediction = 0.8

step_amount = 0.001

count = 0

while count < 1101:
  count += 1
  prediction = input * weight
  error = (prediction - goal_prediction)**2

  print('Step %s, Error: %s , Prediction: %s' %
        (str(count), str(error), str(goal_prediction)))

  if (abs(error) < 1.0e-10):
    break

  up_pred = input * (weight + step_amount)
  up_error = (up_pred - goal_prediction)**2

  down_pred = input * (weight - step_amount)
  down_error = (down_pred - goal_prediction)**2

  if (down_error < up_error):
    weight -= step_amount
  if (down_error > up_error):
    weight += step_amount
