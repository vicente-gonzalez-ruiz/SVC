L = 4 # Number of levels of the pyramid
G = 8 # GOF size
i = 0
l = L
while i<G:
    print("Generate the", L,"\b-levels pyramid of Frame ", 2*i)
    print("Generate the", L, "\b-levels pyramid of Frames", 2*i+1, "and", 2*i+2)
    while l>0:
        print("Create a prediction for the level", l-1, "of Frame", 2*i+1, "using the Level", l-1, "of the Frames", 2*i, "and", 2*i+1, "as references")
        print("Replace the Level", l-2, "of Frame", 2*i+1, "by the difference")
        print("Encode the Level", l-2, "of Frame", 2*i+1)

        l = l-1
        print("Generate the pyramid of differences for Frame", 2*i, "and encode it")

    i = i+2
