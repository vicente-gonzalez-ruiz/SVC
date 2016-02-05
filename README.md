# SVC: A Symmetric Video Codec

## Analyze-step procedure:

		+----------+ +------------+ +------------+
		| Frame 2i | | Frame 2i+1 | | Frame 2i+2 |
		+----------+ +------------+ +------------+

0. l <- L. i <- 0.
1. Generate the L-levels pyramid of Frame 2i.
2. Generate the L-levels pyramid of Frames 2i+1 and 2i+2.
3. Create a prediction for the Level l-2 of Frame 2i+1 using the Level l-1 of Frames 2i and 2i+2 as references, and replace the Level l-2 of Frame 2i+1 by the differences· Encode the Level l-2 of Frame 2i+1.
4. l <- l-1. Go to 3, while l > 0. l <- L.
5. Generate the pyramid of differences for Frame 2i. Encode it.
6. i <- i+2 and go to 2, until reached the end of the GOF.

## Synthesize-step procedure:

   		   +-----+      +-----+	     +-----+
		   |     |      |     |	     |     |
		   +-----+      +-----+	     +-----+
		      |                         |
		 interpolate               interpolate
		      +                         +
	           residue                   residue
		      |                         |
		      v                         v
		+-----------+ +----------+ +----------+ 
		|           | |	         | |          |
 		|           | |          | |          |
		|           | |          | |          |
		+-----------+ +----------+ +----------+


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
