with open('input.txt', "r") as f:
    numbers = [int(x) for x in f.readline().split(",")]


def minimize_hours(exams):
    n = len(exams)
    dp = [0] * n

    dp[0] = exams[0]
    dp[1] = exams[1]

    for i in range(2, n):
        if i % 2 == 1:
            dp[i] = exams[i] + dp[i-3]
        else:
            dp[i] = exams[i] + min(dp[i-2], dp[i-1])

    return dp[-1]


with open('output.txt', "w") as f:
    f.write(str(minimize_hours(numbers)))
