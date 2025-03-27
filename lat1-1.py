
for i in range(5):
    for j in range(5):
        if j == 0 or j == 4 or i == 5 // 2:
            print("*", end=" ")
        elif (i == 1 or i == 3) and (j == 1 or j == 3) :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")