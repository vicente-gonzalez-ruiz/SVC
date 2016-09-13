# SVC: A Symmetric Video Codec

A SVC is based on the idea that both, the encoder and the decoder, have the same intelligence and therefore, only those pieces of information that can not be predicted by the encoder (and the decoder) are represented in the code-stream, which can also include the prediction algorithm.

## Image pyramid:

Input:
S = number of spatial resolutions.

## Analyze-step:

~~~
+---------+ +---------+ +---------+
|  F[2i]  | | F[2i+1] | | F[2i+2] |
+---------+ +---------+ +---------+
~~~

Input:
L = number of spatial resolutions.
F[] = the sequence of frames to encode.

Output:
The code-stream.

Algorithm:
0. l <- L. i <- 0.
1. Generate the L-levels pyramid of frame F[2i], ranging them from n-1 (the smaller one) to 0 (the larger one).
2. Generate the L-levels pyramid of frames F[2i+1] and F[2i+2], ranging them from n-1 to 0.
3. Create a prediction for Level l-2 of F[2i+1] using the Level l-1 of F[2i] and F[2i+2] as references, and replace the Level l-2 of Frame 2i+1 by the differences.
4. Encode the Prediction Error l-2 (level l-2).
5. l <- l-1.
6. Go to 3, while l > 0.
7. l <- L.
5. Generate the pyramid of differences for Frame 2i. Encode it.
6. i <- i+2 and go to 2, until reached the end of the GOF.

## Analyze-step:


      +-----------+    +-----------+    +-----------+ 
      |           |    |           |    |           |
    +-|     A     |    |     B     |    |     C     |-+
    | |           |    |           |    |           | |
    | +-----------+    +-----------+    +-----------+ |
    |       |                |                |       |
    |   subsample        subsample        subsample   | Step 1
    |       |                |                |       |
    |       v                v                v       |
    |    +-----+          +-----+          +-----+    |
    |    |     |          |     |          |     |    |
    |    +-----+          +-----+          +-----+    |
    |       |                |                |       |
    |  interpolate      interpolate      interpolate  | Step 2
    |       |                |                |       |
    |       v                v                v       |
    | +-----------+    +-----------+    +-----------+ |
    | |     ~     | ME |     ~     | ME |     ~     | |
    | |     A     |<---|     B     |--->|     C     | | Step 3
    | |           |    |           |    |           | |
    | +-----------+    +-----------+    +-----------+ |
                             |
			     v
			  +----+
                          | MD |
                          +----+

    |       |                |                |       |
    +-> substract   selective substract   substract <-+  Step 4
            |                |                |
            v                v                v
      +-----------+    +-----------+    +-----------+
      |      ~    | MC |           | MC |      ~    |
      |    A-A    |--->|     X     |<---|    C-C    | Step 5
      |           |    |           |    |           |
      +-----------+    +-----------+    +-----------+


X has I, P and B blocks (which can be of any size). An I-block is used
when the entropy of the I-block (B-B') is smaller or equal than the
entropy of the MC version of that block. A P-block if the entropy of the P

## Synthesize-step:
                     +-----------+
                     |           |
                     |     X     |
                     |           |
                     +-----------+
                           ^
                           |
                      add residue                   Step 5
                           |
    +-----------+    +-----------+    +-----------+
    |           | MC |	         | MC |           |
    |     A     |--->|           |<---|     C     | Step 4
    |           |    |           |    |           |
    +-----------+    +-----------+    +-----------+
          ^                ^                ^
	  |                |                |
     add residue     selective copy    add residue  Step 3
	  |                |                |
    +-----------+    +-----------+    +-----------+ 
    |           | ME |           | ME |           |
    |           |<---|     B     |--->|           | Step 2
    |           |    |           |    |           |
    +-----------+    +-----------+    +-----------+
          ^                ^                ^
          |                |                |
     interpolate      interpolate      interpolate  Step 1
          |                |                |
       +-----+          +-----+	         +-----+
       | 2i  |          |2i+1 |	         |2i+2 |
       +-----+          +-----+	         +-----+


A pixel in X can have different origins: A (MC), B (selective copy), C
(MC), (A+B)/2 (MC), etc. This decission need to be done at step 1 and
should be taken into account the entropy of the residue pixels (result
of the difference between the original pixels in B and the prediction)
with respect to those pixels in B.


0. l <- L.
1. Decode the Level l-1 of Frame 2i.
2. Decode the Level l-1 of Frame 2i+2.
3. Create a prediction for the Level l-2 of Frame 2i+1 using the Level l-1 of Frames 2i and 2i+2 as references.
4. Decode the (residue) level L-2 of Frame 2i+1. Add the prediction to it.
5. l <- l-1. Go to 1, while l > 0. l <- L.
6. i <- i+2 and go to 2, until reached the end of the GOF.



1. Generate Frame_0.Level_L and Frame_2.Level_L.
2. Estimate the motion between the prvious cjhennels.
3. 

Conseguir ceros mediante interpolacion y luego usar codificacion aritmetica un un modelo probabilistico de orden 0. Ver si es posible usar el nivel L para estimar el movimiento usado en el L-1 (como imagen, no como residuo, que puede estar muy mermado). La idea es no transmitir los vectores de movimiento.

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

1. Generate a prediction for "Level L-1" using "Level L" (for example, using bilinear interpolation or information -- represented in a compact form -- that will be avaiable when Level L-1 is decoded).
2. Decode a prediction error for "Level L-1".
3. Generate "Level L-1" as the addition of the prediction for "Level L-1" and the prediction error for "Level L-1".
4. L <- L - 1
5. Go to step 1.

Encode-frame procedure:

1. Generate "Level L" by using "Level L-1".
2. Generate a prediction for "Level L-1" using "Level L" (using the same method than the used by the decoder).
3. Generate a prediction error for "Level L-1" as the substraction of the prediction for "Level L-1" to "Level L-1".
4. Encode the prediction error for "Level L-1".
5. L <- L + 1.
6. Go to step 2.


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


	+-----+
	|  A  |
	+-----+

	+-----+-----+
	|  B  |  C  |
	+-----+-----+
	|  D  |  E  |
	+-----+-----+

Decode-level procedure:

0. A has been decoded in the previous iteration.
2. Generate a prediction for B, C, D and E using A (for example, B=C=D=E=A).
3. Decode a prediction error for B, C, D and E.
4. Generate B, C, D and E as the addition of the prediction error for B, C, D, and E plus the prediction for B, C, D and E.

Encode-level procedure:

1. Generate a prediction for B, C, D and E by using A (for example, B=C=D=E=A).
2. Generate a prediction error for B, C, D, ane E by substracting the prediction for B, C, D and E to B, C, D and E.
3. Encode the prediction error for B, C, D and E.

There is not a dependency between sub-pyramids of the same level.

[1] http://www.drdobbs.com/image-compression-using-laplacian-pyrami/184403435?pgno=12
[2] http://persci.mit.edu/pub_pdfs/imagedata81.pdf
[3] http://persci.mit.edu/pub_pdfs/pyramid83.pdf
[4] http://collaboration.cmc.ec.gc.ca/science/rpn/biblio/ddj/Website/articles/CUJ/1997/9712/perry/perry.htm
[5] http://www1.icsi.berkeley.edu/~stellayu/publication/doc/2009egmsISVC.pdf
[6] http://www2.ensc.sfu.ca/grad/theses/masters/Dave_Houlding_MASc_94.pdf
