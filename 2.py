with open('input.txt', "r") as f:
    numbers = [int(x) for x in f.readline().split(",")]


def find_max_values(nums):
    max_values = []

    n = len(nums)

    for i in range(n - 2):
        window = nums[i:i + 3]
        max_value = max(window)
        max_values.append(max_value)

    return max_values


with open('output.txt', "w") as f:
    f.write(str(find_max_values(numbers)))
