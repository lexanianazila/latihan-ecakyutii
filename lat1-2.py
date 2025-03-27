
for i in range(7):
    for j in range(8):
        if i == 0 or i == 6 :
            print("*", end=" ")
        elif j == 0 or j == 7 :
            print("*", end=" ")
        elif (i == 1 or i == 5) and (j <= 2 or j >= 5) :
            print("*", end=" ")
        elif (i == 2 or i == 4) and (j == 0 or j == 1 or j == 6 or j == 7) :
            print("*", end=" ")
        elif i == 3 and j == 0 :
            print("*", end=" ")
        else :
            print(" ", end=" ")
    print("")