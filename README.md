# Erdos-Gallai-theorem
A python script to test if a list of ints is a valid simple graph via the Erdős–Gallai theorem

A sequence of non-negative integers d_i >= ... >= d_n can be represented as the degree sequence of a finite simple graph on n vertices if and only if d_i + ... + d_n is even and

sum {i=1} to k = d_i <= (k(k-1) + (sum {j = k+1} to n min(d_i,k))

holds for every k in 1 <= k <= n.

Ref:
https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gallai_theorem
https://math.stackexchange.com/questions/1974997/confused-about-erdos-gallai-theorem
https://mathworld.wolfram.com/SimpleGraph.html 

Has some issues as of 2021/07/23