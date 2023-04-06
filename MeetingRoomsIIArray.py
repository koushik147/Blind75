intervals = [[0,30],[15,20],[35,45]]
n = len(intervals)
result = 0
starts = []
ends = []

for start, end in intervals:
  starts.append(start)
  ends.append(end)

starts.sort()
ends.sort()

j = 0
for i in range(n):
  if starts[i] < ends[j]:
    result += 1
  else:
    j += 1

print(result)