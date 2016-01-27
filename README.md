# SVC
A Symmetric Video Codec

	+---------+ +---------+ +---------+
	| Frame 0 | | Frame 1 | | Frame 2 |
	+---------+ +---------+ +---------+

Decoder step:

1. Decode "Frame 0".
2. Decode "Frame 2".
3. Generate a prediction for "Frame 1".
4. Decode a prediction error for "Frame 1".
5. Generate "Frame 1" as the addition of the prediction for "Frame 1" and the prediction error for "Frame 1".

Encoder step:

1. Encode "Frame 0".
2. Encode "Frame 2".
3. Generate a prediction for "Frame 1".
4. Generate a prediction error for "Frame 1" as the substraction of the prediction for "Frame 1" to "Frame 1".
5. Encode the prediction error for "Frame 1".

	+---------+ 
	|         |
	| Level L |
	|         |
	+---------+
	+---------------------+
	|                     |
	|                     |
	|                     |
	|      Level L-1      |
	|                     |
	|                     |
	|                     |
	+---------------------+


Decode-frame procedure:

1. Decode "Level L".
2. Generate a prediction for "Level L-1" using "Level L".
3. Decode a prediction error for "Level L-1".
4. Generate "Level L-1" as the addition of the prediction for "Level L-1" and the prediction error for "Level L-1".
5. L <- L-1
6. Go to step 2.

Encode-frame procedure:

1. Generate "Level L" using "Level L-1".
2. Generate a prediction for "Level L-1" using "Level L".
3. Generate a prediction error for "Level L-1" as the substraction of the prediction for "Level L-1" to "Level L-1".
4. Encode the prediction error for "Level L-1".
5. L <- L+1.
6. Go to step 2.


	+------+------+------+
	|      |      |      |
	+------+------+------+
	|      |      |      |
	+------+------+------+
	|      |      |      |
	+------+------+------+
	|      |      |      |
	+------+------+------+

Decode-level procedure:

