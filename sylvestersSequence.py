__author__="Atalay Samet Ergen"
"""
In number theory, Sylvester's sequence is an integer sequence in which each member of the sequence is
the product of the previous members, plus one. The first few terms of the sequence are:
2, 3, 7, 43, 1807, 3263443, 10650056950807, 113423713055421844361000443 (sequence A000058 in the OEIS).
Reference: https://en.wikipedia.org/wiki/Sylvester%27s_sequence
"""
def sylvelsterSequence(n):
    product = 1
    for i in range(n):
        product *= sylvelsterSequence(i)
    return product + 1

print(sylvelsterSequence(8))
