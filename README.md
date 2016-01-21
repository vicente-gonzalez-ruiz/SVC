# SVC
A Symmetric Video Codec

Decoder's life:

'''
+---------+
| Frame 0 | | Frame 1 
+---------+

1. Read a frame: F_i.
2. Perform a prediction for the frame in the middle:  
