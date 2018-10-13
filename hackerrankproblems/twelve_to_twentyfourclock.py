# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Sample Input 07:05:45PM and sample Output is 19:05:45


def timeConversion(s):
    time_components = s.split(':')
    print(time_components)


print("**What is time in 12-hour system?**")
s = input().strip()
result = timeConversion(s)
print(result)
