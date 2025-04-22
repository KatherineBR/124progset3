import sys
import random
import math

max_iter = 10

def residue(A, S):
    sum = 0
    for i in range(len(A)):
        sum += A[i] * S[i]
    return sum
    

def std_repeated_random(A):
    n = len(A)
    
    # Randomly generate some starting sequence
    seq = random.choices([1, -1], k=n)

    # Repeatedly generate sequences and take the better one
    for _ in range(1, max_iter):
        seq1 = random.choices([1, -1], k=n)
        if residue(seq1) < residue(seq):
            seq = seq1
    return seq

def std_hill_climbing(A):
    n = len(A)

    # Randomly generate some starting sequence
    seq = random.choices([1, -1], k=n)

    # Iterate over possible neighbors, only taking the better one
    for _ in range(1, max_iter):
        i = random.randint(1, n)
        j = random.randint(1, n)
        while j == i:
            j = random.randint(1, n)
        if random.choice([True, False]):
            seq[i] = -seq[i]
        seq[j] = -seq[j]
    
    return seq

def std_annealing(A):
    n = len(A)

    seq = random.choices([1, -1], k=n)
    seq2 = seq

    for i in range(1, max_iter):
        # Get a random neighbor of seq
        seq1 = seq
        i = random.randint(1, n)
        j = random.randint(1, n)
        while j == i:
            j = random.randint(1, n)
        if random.choice([True, False]):
            seq1[i] = -se1[i]
        seq1[j] = -seq1[j]

        if residue(seq1) < residue(seq):
            seq = seq1
        else:
            prob = math.exp(-(residue(seq1) - residue(seq) / T(i)))

        if residue(seq) < residue(seq2):
            seq2 = seq
    
    return seq2


def pp_repeated_random(n):
    pass

def pp_hill_climbing(n):
    pass

def pp_annealing(n):
    pass

def main():
    if len(sys.argv) == 0:
        #for testing!
        pass
    elif len(sys.argv) != 4:
        print("Usage: python script.py <flag> <algorithm> <inputfile>")
        sys.exit(1)

    try:
        flag, algorithm, inputfile = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    except ValueError:
        print("Error: flag and algorithm must be integers.")
        sys.exit(1)

    #deal with reading input here
    #call our method here

if __name__ == "__main__":
    main()