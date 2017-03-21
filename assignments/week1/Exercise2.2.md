Exercise 2.2
--
Given a matrix such as A in Fig. 2.2.1, my algorithm would add the identity matrix of A to matrix A, then calculate A^(N-1) where N is the number of rows in A. I would then have the matrix to comepare against to find any given connection. For instance, given nodes I and J, I would examine row I and column J and evalute whether that item is gereater than 0. If it was, then there's a connection between those two nodes.
