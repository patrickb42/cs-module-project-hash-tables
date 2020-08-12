my_dict = {'a': 'z', 'b': 'c', 'd': 'z', 'e': 'f'}
def a_func(a, b):
  print(a, b)
  return a
sorted(my_dict, key=a_func)
