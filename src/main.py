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
  inputMatr = Matrix([[1,3,4,15], [2,5,"",12], [7,6,11,14], [8,9,10,13]])
  print(inputMatr)
  print(checkBnB(inputMatr))