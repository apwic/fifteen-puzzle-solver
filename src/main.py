from bnb import *

if __name__ == "__main__":
  # matr = Matrix();
  # print(matr)
  # print(matr.getElmt(15))
  # print(matr.getEmpty())
  # matr.move("up")
  # print(matr)
  # matr.move("down")
  # print(matr)
  # matr.move("right")
  # print(matr)
  # matr.move("left")
  # print(matr)

  # print(checkBnB(matr))
  inputMatr = Matrix([[1,2,3,4], [5,6,"",8], [9,10,7,11], [13,14,15,12]])
  # print(checkBnB(inputMatr))
  print(inputMatr)

  solve((inputMatr, 0))

  matr = Matrix()
  check = checkBnB(matr)

  if (check):
    solve((matr, 0))