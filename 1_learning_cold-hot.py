weight = 0.1
# Delta for changing weight in NN and learning!
lr = 0.01


def neural_network(input, weight):
  prediction = input * weight
  return prediction


# Inputs
number_of_toes = [8.5]
# Answers for each input
win_or_lose_binary = [1]  # correct answers: 0 - lose , 1 - win

input = number_of_toes[0]
correctAns = win_or_lose_binary[0]

# Get prediction from NN
pred = neural_network(input, weight)

# Calc cube Error!
error = (pred - correctAns)**2
print('error = %.04f' % error)

# FIND UP and DOWN predictions for current NN
# Increase weight in NN and check Error
pred_up = neural_network(input, weight + lr)
error_up = (pred_up - correctAns)**2
print('error_up (+lr) = %.05f' % error_up)

# Decres weight in NN and check Error
pred_down = neural_network(input, weight - lr)
error_down = (pred_down - correctAns)**2
print('error_down (-lr) = %0.05f' % error_down)

# COMPARE and LEARN NN
print('old weight = %.05f' % weight)
if (error > error_down or error > error_up):
  if error_down < error_up:
    print('go down (-lr)')
    weight -= lr
  if error_up < error_down:
    print('go up (+lr)')
    weight += lr

print('new weight = %.05f' % weight)