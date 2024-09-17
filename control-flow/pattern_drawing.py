size = int (input("Enter the size of the pattern:"))
side = size
while side > 0:
    side -= 1
    for num in range(1,size+1):
        print("*", end="")
    print("")
