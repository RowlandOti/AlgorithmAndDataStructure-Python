# Complete the function below.
import os


def get_sum_patterns(lower_of_num, target, partial=[], match_list=[]):
    s = sum(partial)

    # if (s > target):
    # return

    if (s == target):
        match_list.append(partial)

    for j in range(len(lower_of_num)):
        n = lower_of_num[j]
        remaining = lower_of_num[j + 1:]
        get_sum_patterns(remaining, target, partial + [n], match_list)

    return len(match_list)


def consecutive(target):
    sum_pattern_count = 0
    lower_of_target = list(range(1, target))
    partials = []
    for i, n in enumerate(lower_of_target):
        partials += [n]
        s = sum(partials)

        if (s > target):
            return

        if (s == target):
            print(partials)
            sum_pattern_count += 1

    return sum_pattern_count


if __name__ == "__main__":
    num = int(input());

    res = consecutive(num);
    print(res)
