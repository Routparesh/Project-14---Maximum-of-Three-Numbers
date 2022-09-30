def max_of_three(n_1, n_2, n_3):
  if n_1 > n_2 or n_3:
    return n_1
  elif n_2 > n_1 or n_1:
    return n_2
  else:
    return n_3
print(max_of_three(2,3,4))