print("========================")

L = 4 # Number of levels of the pyramid
G = 4 # GOF size
i = 0
print("Generate the", L,"\b-levels pyramid of Frame ", 2*i)
while i<(G/2+1):
    print("Generate the", L, "\b-levels pyramid of Frames", 2*i+1, "and", 2*i+2)
    l = L
    while l>1:
        print("Create a prediction for the level", l-2, "of Frame", 2*i+1, "using the Level", l-1, "of the Frames", 2*i, "and", 2*i+2, "as references")
        print("Replace the Level", l-2, "of Frame", 2*i+1, "by the difference")
        print("Encode the Level", l-2, "of Frame", 2*i+1)

        l = l-1
    print("Generate the pyramid of differences for Frame", 2*i, "and encode it")
    i = i+1

