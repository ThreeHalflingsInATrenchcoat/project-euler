"""triangle = 59
73 41
52 40 09
26 53 06 34
10 51 87 86 81
61 95 66 57 25 68
90 81 80 38 92 67 73
30 28 51 76 81 18 75 44
84 14 95 87 62 81 17 78 58
21 46 71 58 02 79 62 39 31 09"""

with open('067_triangle.txt','r',encoding='utf_8') as file:
    triangle = file.read().strip()

triangle = [[int(num) for num in row.split(' ')] for row in triangle.split('\n')]

for i in range(len(triangle)):
    print(triangle[i])

for i in reversed(range(len(triangle) - 1)):
    for j in range(i + 1):
        left = triangle[i+1][j]
        right = triangle[i+1][j+1]
        triangle[i][j] += max(left, right)

print(triangle[i][j])