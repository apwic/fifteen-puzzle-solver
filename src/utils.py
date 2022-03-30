from matrix import *

def readFromFile(fileName):
  path = "./test/" + fileName

  try:
    matr = []
    countLine = 0
    with(open(path)) as f:
      for line in f:
        splitted = line.split(" ")
        try:
          row = [int(x) for x in splitted]
          matr.append(row)
          countLine += 1
        except:
          print("Element invalid")

    if countLine != 4:
      raise Exception("Invalid txt file")
    else:
      return Matrix(matr)

  except:
    print(f"{path} not found")