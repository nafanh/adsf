def main():
  dim = int(input("Enter dimension: "))
  grid = []
  
  for i in range(dim):
    zeros = []
    for j in range(dim):
      zeros.append(0)
    grid.append(zeros)
  
main()
