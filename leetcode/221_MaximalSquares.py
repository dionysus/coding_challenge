'''
221. Maximal Square
Difficulty: Medium
URL: https://leetcode.com/problems/maximal-square/

Given a 2D binary matrix filled with 0's and 1's, find the largest square 
containing only 1's and return its area.

Example:
Input:
  1 0 1 0 0
  1 0 1 1 1
  1 1 1 1 1
  1 0 0 1 0
Output: 4
'''

'''
idea:
keep track of current max size
iterate over each element,
if matrix[r,c] == 1: find largest possible square from this index
start at current max
stop if row remaining is less than current max size
'''

def maximalSquare(matrix):

  def getMaxSq(matrix, r, c, maxSq):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows - r <= maxSq or cols - c <= maxSq:
      return 0

    maxW = 0
    for i in range(c, cols):
      if matrix[r][i] == "1":
        maxW += 1
      else:
        break
    if maxW <= maxSq:
      return 0

    maxH = 0
    for i in range(r, rows):
      if matrix[i][c] == "1":
        maxH += 1
      else:
        break
    if maxH <= maxSq:
      return 0
    
    maxPos = min(maxH, maxW)
    i = 0
    while i < maxPos:
      # check row
      for col in range(c, c+i+1):
        if matrix[r+i][col] == "0":
          return i
      # check col
      for row in range(r, r+i+1):
        if matrix[row][c+i] == "0":
          return i
      i+=1

    return i

  rows = len(matrix)
  if rows == 0:
    return 0
  cols = len(matrix[0])
  # maxPos = min(rows, cols)
  if cols == 0: 
    return 0

  maxSq = 0
  for r in range(rows):
    for c in range(cols):
      if matrix[r][c] == "0":
        pass
      else:
        currMax = getMaxSq(matrix, r, c, maxSq)
        maxSq = max(maxSq, currMax)

  return maxSq**2

if __name__ == "__main__":
  # matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
  matrix = [["0","1"]]
  matrix = [
    ["1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","0"],
    ["1","1","1","1","1","1","1","0"],
    ["1","1","1","1","1","0","0","0"],
    ["0","1","1","1","1","0","0","0"]]
  res = maximalSquare(matrix)
  print(res)