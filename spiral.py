def top(grid,row,col,dim,end):
  square = dim**2
  for i in range(col, end,-1):
    grid[row][i] = square
    square -= 1


def lCol(grid,row,col,dim,start):
  square = dim ** 2 - dim + 1
  for i in range(start,row+1):
    grid[i][col] = square
    square -= 1


def bot(grid,row,col,dim,end):
  square  = dim ** 2 - (3*dim) + 3
  for i in range(col,end,-1):
    grid[row][i] = square
    square += 1


def rCol(grid,row,col,dim,end):
  square= dim ** 2 - (3*dim) + 3
  for i in range(row,end,-1):
    grid[i][col] = square
    square -= 1


def neighbors(grid, num):
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == num:
        if (i > 0 and i < len(grid) - 1) and (j >0 and j < len(grid)-1):
          print(grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1], end="\n")
          print(grid[i][j - 1], grid[i][j], grid[i][j + 1], end="\n")
          print(grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1], end="\n")
        else:
          print("Number of Outer Edge.")




def main():
  dim = int(input("Enter dimension: "))
  grid = []

  for i in range(dim):
    zeros = []
    for j in range(dim):
      zeros.append(0)
    grid.append(zeros)


  topLimit = dim
  limit = topLimit // 2
  count = 0
  col = topLimit - 1
  row = 0
  end = -1
  while count < limit:
    top(grid, row, col, topLimit, end)
    topLimit -= 2
    col -= 1
    row += 1
    end += 1
    count += 1

  leftLimit = dim
  countLimit = leftLimit // 2
  countLeft = 0
  colLeft = 0
  rowLeft = leftLimit - 1
  start = 0

  while countLeft < countLimit:
    lCol(grid, rowLeft, colLeft, leftLimit,start)
    start += 1
    leftLimit -= 2
    countLeft += 1
    colLeft += 1
    rowLeft -= 1


  botLimit = dim
  countLimitBot = botLimit // 2
  countBot = 0
  colBot = botLimit-1
  rowBot = botLimit-1
  start = 0
  while countBot < countLimitBot:
    bot(grid,rowBot,colBot,botLimit,start)
    countBot += 1
    start += 1
    botLimit -= 2
    colBot -= 1
    rowBot -= 1

  rightLimit = dim
  countLimitRight = rightLimit // 2
  countRight = 0
  colRight = rightLimit - 1
  rowRight = rightLimit-1
  end = 0
  while countRight < countLimitRight:
    rCol(grid,rowRight,colRight,rightLimit,end)
    end += 1
    colRight -= 1
    rowRight -= 1
    countRight += 1
    rightLimit -= 2

  grid[dim//2][dim//2] = 1

  print()
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      print(grid[row][col], end=' ')
    print()


  num = int(input("Enter number in spiral: "))
  neighbors(grid,num)



main()

