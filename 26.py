def max_tasks(nums):
    count, countm = 1, 1
    for i in range(len(nums) - 1):
        if nums[i + 1] == nums[i] + 1:
            count += 1
            countm = max(count, countm)
        else:
            count = 1
    return countm
file = open('26_19256.txt')
data = {}
N = int(file.readline())
for _ in range(N):
    id, task = [int(x) for x in file.readline().split()]
    if id in data:
        data[id].add(task)
    else:
        data[id] = {task}
file.close()

countm = 0
for id in data:
    countm = max(countm, max_tasks(sorted(data[id])))
mid = 0
for id in sorted(data):
    if max_tasks(sorted(data[id])) == countm:
        mid = id
        break
print(mid, countm)


