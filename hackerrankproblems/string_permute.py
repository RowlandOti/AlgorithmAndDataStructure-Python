# Aim is to find the no, of the differnt ways we can write the order of the characters in a String


# Method 1
def recPermute(rest, so_far="", permutes=[]):
    if (rest == []):
        permutes.append(so_far)
        return

    for i in range(len(rest)):
        next = so_far + rest[i]
        remaining = rest[0:i] + rest[i + 1:]
        recPermute(remaining, next, permutes)

    return permutes


permutable_string = input().strip()

permutations = recPermute(list(permutable_string))
print("Permutations are:  {}".format(permutations))
print("Total of {} permuations for {}".format(len(permutations), permutable_string))


# Method 2 using factorial
def factorial(num):
    if (num == 0):
        return 1
    return num * factorial(num -1)

def findNumPermutes(base_string):
    print("Total of {} permuations for {}".format(factorial(len(base_string)), base_string))


findNumPermutes("abcd")