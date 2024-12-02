
if __name__ == "__main__":
    f = open("input.txt", "r")
    tmp = f.read()
    tmp = tmp.split("\n")
    l1 = []
    l2 = [] 
    for pair in tmp:
        a,b = pair.split("   ")
        l1.append(int(a))
        l2.append(int(b))
    
    sum = 0

    for x in l1:
        num_of_times = 0
        for y in l2:
            if x == y:
                num_of_times += 1
        sum += x * num_of_times        
    
    print(sum)