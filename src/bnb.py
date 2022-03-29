from matrix import *

"""
find matrix elmt
that is j < i and posisi(j) > posisi(i)
"""
def kurang(matrix : Matrix, i):
  if (i == 16):
    iPos = matrix.getEmpty()
  else:
    iPos = matrix.pos(i)
  kur = 0

  for x in range(1,i):
    if (matrix.pos(x) > iPos):
      kur += 1;

  print(f"Kurang[{i}] = {kur}")
  return kur

"""
check if matrix is solveable
"""
def checkBnB(matrix : Matrix):
  kur = 0

  for i in range(1, 17):
    kur += kurang(matrix, i)

  check = kur + matrix.X()
  print(f"{check} = {kur} + {matrix.X()}")

  if (check % 2 == 0):
    return True
  else:
    return False
