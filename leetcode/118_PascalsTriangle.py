#Given numRows, generate the first numRows of Pascal's triangle.

#For example, given numRows = 5,
#Return

#[
#     [1],
#    [1,1],
#   [1,2,1],
#  [1,3,3,1],
# [1,4,6,4,1]
#]


def generate(numRows):

	list = []

	for row in range (0, numRows):
		list.append([])
		for place in range (0, row+1):
			if place == 0 or place == row:
				list[-1].append(1)
			else:
 				list[-1].append(list[-2][place]+list[-2][place-1])
	return list

print generate(6)		
