n = 2**1000
string = str(n)

string_list = []
for i in range(0,len(string)):
    string_list.append(int(string[i]))

print(string_list)
print(sum(string_list))

