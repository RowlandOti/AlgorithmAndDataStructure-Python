# There is a collection of N strings ( There can be multiple occurences of a particular string ).
# Each string's length is no more than 20 characters. There are also  queries.
# For each query Q, you are given a string, and you need to find out how many times this string occurs in the given collection of N strings.

print("**Number of Strings**")
N = int(input().strip())

arr_N = []
for i in range(N):
    arr_N.append(input().strip())

print("**Number of Queries**")
Q = int(input().strip())

arr_Q = []
for i in range(Q):
    arr_Q.append(input().strip())

word_freq = []
for i in range(Q):
    word = arr_Q[i]
    word_freq.append(0)
    if word in arr_N:
        word_freq[i] = arr_N.count(word)

for count in word_freq:
    print(count)