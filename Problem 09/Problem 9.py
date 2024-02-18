# for all a,b,c in range(0,1000), check if a^2+b^2=c^2
found_triplet = False
for a in range(0,1000):
    if found_triplet:
        break
    for b in range(a+1,1000):
        for c in range(b+1,1000):
            if a+b+c <= 1000:
                if a**2 + b**2 == c**2 and a+b+c < 1000:
                    print(str(a)+", "+str(b)+", "+str(c))
            if a**2 + b**2 == c**2 and a+b+c == 1000:
                print("Found the triplet which is "+str(a)+", "+str(b)+", "+str(c))
                print(a*b*c)
                found_triplet = True
                break
