Week 1 Homework
--
Due Monday, August 29 at 11:55pm.

* Exercise 2.2
* Write the following Python program.
 * The program will output 100 letters per line, on 10 lines.  It will output *nothing else*.
 * The first letter is always "I".
 * The subsequent letters will be generated with the following probabilities:
 * P(_ | I) = 1
 * P(a | _) = 0.5
 * P(l | _) = 0.5
 * P(m | a) = 0.4
 * P(_ | m) = 0.8
 * P(! | m) = 0.2
 * P(l | a) = 0.6
 * P(i | l) = 1
 * P(v | i) = 0.95
 * P(e | v) = 1
 * P(n | i) = 0.05
 * P(e | n) = 1
 * P(! | e) = 1
 * P(_ | !) = 0.7
 * P(I | !) = 0.2
 * P(! | !) = 0.1
 
Submit your Python file (week1.py)  The header of your file should be the following:

"""

My Name

my_identikey1234

my_email@colorado.edu

Week 1

"""
