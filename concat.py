#write a function that will capitalize and sort a list alphabetically
def alpha(*args):
    args = [arg.upper() for arg in args]
    return sorted(args)


print(alpha("this" ,"does",  "work"))


def find_sum(a,b):
    return (a + b)

print(find_sum(a=5, b=4))