
if __name__ == "__main__":
    f = open("input.txt", "r")
    tmp = f.read()
    tmp = tmp.split("\n")
    l1 = []
    l2 = [] 
    for pair in tmp:
        a,b = pair.split("   ")
        l1.append(a)
        l2.append(b)
    
    l1.sort()
    l2.sort()
    l3 = zip(l1,l2)

    sum = 0
    for x in l3:
        a,b = x
        distance = abs(int(a) - int(b))
        sum += distance

    print(sum)

            