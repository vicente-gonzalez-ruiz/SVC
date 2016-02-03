L = 4
l = L
i = 0
print("Generate the", L,"\b-levels pyramid of Frame ", 2*i)
print("Generate the", L, "\b-levels pyramid of Frames", 2*i+1, "and", 2*i+2)
print("Create a prediction for the level", l-1, "of Frame", 2*i+1, "using the Level", l-1, "of the Frames", 2*i, "and", 2*i+1, "as references")
print("Replace the Level", l-2, "of Frame", 2*i+1, "by the difference")
print("Encode the Level", l-2, "of Frame", 2*i+1)
