def factorial(n):
    if n == 1:
        return 1
    if n > 1:
        return n * factorial(n-1)

n = factorial(100)
string = str(n)

string_list = []
for i in range(0,len(string)):
    string_list.append(int(string[i]))

# print(string_list)
print(sum(string_list))