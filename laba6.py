b = input("input string")
def reverse(b):
    a = ""
    for i in range(1, len(b)+1):
        a += b[len(b) - i]
    return a
print(reverse(b))