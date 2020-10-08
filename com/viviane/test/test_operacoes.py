def  fun(x):
  return x + 3
def teste_positivo():
  assert fun(10) == 13
def teste_negativo():
  assert fun(-7) == -4
def teste_zero():
  assert fun (0) == 3