with open('input.txt', "r") as f:
    numbers = [int(x) for x in f.readline().split(",")]


def find_missing_number(nums):
    n = len(nums)

    for i in range(n):
        while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


with open('output.txt', "w") as f:
    f.write(str(find_missing_number(numbers)))
