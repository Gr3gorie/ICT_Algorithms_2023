with open('input.txt', "r") as f:
    numbers = [int(x) for x in f.readline().split(",")]


def sort_list(nums):
    counts = [0, 0, 0]
    for num in nums:
        counts[num] += 1

    i = 0
    for j in range(3):
        while counts[j] > 0:
            nums[i] = j
            counts[j] -= 1
            i += 1

    return nums


with open('output.txt', "w") as f:
    f.write(str(sort_list(numbers)))
