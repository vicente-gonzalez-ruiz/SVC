# SVC
A Symmetric Video Codec

Decoder's life:

    +---------+ +---------+ +---------+
    | Frame 0 | | Frame 1 | | Frame 2 |
    +---------+ +---------+ +---------+

1. Read Frame 0.
2. Read Frame 2.
3. Generate Prediction Frame 1.
4. Read Prediction Error Frame 1.
5. Generate Frame 1 as the addition of Prediction Frame 1 and Prediction Error Frame 1.

Encoder's life:

1. Write Frame 0.
2. Write Frame 2.
3. Generate a Prediction Frame 1.
4. Generate Prediction Error Frame 1 as the substraction of Prediction Frame 1 to Frame 1.
5. Write Prediction Error Frame 1.
