import sys
import random
import math
import heapq
import numpy as np

max_iter = 10

def residue(A, S):
    sum = 0
    for i in range(len(A)):
        sum += A[i] * S[i]
    return abs(sum)

def karmarker_karp(A):
    heap = [-num for num in A]
    # print(heap)
    heapq.heapify(heap)

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        heapq.heappush(heap, a - b)
        # print(heap)

    return -heap[0]


def pp_karmarker_karp(A, P):
    n = len(A)
    A1 = [0] * n
    for i in range(n):
        j = P[i] - 1
        A1[j] += A[i]
        
    return karmarker_karp(A1)

def T(iter):
    return pow(10, 10) * pow(0.8, (iter // 300))

def generate_neighbor(seq, n):
    neighbor = seq.copy()
    i = random.randrange(0, n)
    neighbor[i] = -neighbor[i]

    if random.choice([True, False]):
        j = random.randrange(0, n)
        while j == i:
            j = random.randrange(0, n)
        neighbor[j] = -neighbor[j]
    return neighbor

def std_repeated_random(A):
    n = len(A)
    
    # Randomly generate some starting sequence
    seq = random.choices([1, -1], k=n)

    # Repeatedly generate sequences and take the better one
    for _ in range(1, max_iter):
        seq1 = random.choices([1, -1], k=n)
        if residue(A, seq1) < residue(A, seq):
            seq = seq1
    return residue(seq)

def std_hill_climbing(A):
    n = len(A)

    # Randomly generate some starting sequence
    seq = random.choices([1, -1], k=n)

    # Iterate over possible neighbors, only taking the better one
    for _ in range(1, max_iter):
        seq1 = generate_neighbor(seq, n)

        if residue(A, seq1) < residue(A, seq):
            seq = seq1
    
    return residue(seq)

def std_annealing(A):
    n = len(A)

    seq = random.choices([1, -1], k=n)
    seq2 = seq

    for i in range(1, max_iter):
        seq1 = generate_neighbor(seq, n)

        if residue(A, seq1) < residue(A, seq):
            seq = seq1
        else:
            prob = math.exp(-(residue(A, seq1) - residue(A, seq) / T(i)))
            if random.random() < prob:
                seq = seq1

        if residue(A, seq) < residue(A, seq2):
            seq2 = seq
    
    return residue(seq2)


def generate_neighbor_pp(p, n):
    i = random.randrange(0, n)
    j = random.randint(1, n)
    while p[i] == j:
        j = random.randint(1, n)
    p[i] = j
    return p


def pp_repeated_random(A):
    n = len(A)
    seq = random.choices(range(1, n), k=n)
    for _ in range(1, max_iter):
        print(seq)
        seq1 = random.choices(range(1, n), k=n)
        if pp_karmarker_karp(A, seq1) < pp_karmarker_karp(A, seq):
            seq = seq1

    return pp_karmarker_karp(seq)

def pp_hill_climbing(A):
    n = len(A)

    # Randomly generate some starting sequence
    seq = random.choices(range(0, n), k=n)

    # Iterate over possible neighbors, only taking the better one
    for _ in range(1, max_iter):
        seq1 = generate_neighbor_pp(seq, n)

        if pp_karmarker_karp(A, seq1) < pp_karmarker_karp(A, seq):
            seq = seq1
    
    return pp_karmarker_karp(seq)
    

def pp_annealing(A):
    n = len(A)

    seq = random.choices(range(1, n + 1), k=n)
    seq2 = seq

    for i in range(1, max_iter):
        seq1 = generate_neighbor_pp(seq, n)

        if pp_karmarker_karp(A, seq1) < pp_karmarker_karp(A, seq):
            seq = seq1
        else:
            prob = math.exp(-(pp_karmarker_karp(A, seq1) - pp_karmarker_karp(A, seq) / T(i)))
            if random.random() < prob:
                seq = seq1

        if pp_karmarker_karp(A, seq) < pp_karmarker_karp(A, seq2):
            seq2 = seq
    
    return pp_karmarker_karp(seq2)


def main():
    if len(sys.argv) == 1:
        #for testing!
        # print(karmarker_karp([10, 8, 7, 6, 5]))
        # print(pp_karmarker_karp([10, 8, 7, 6, 5], [1, 2, 2, 4, 5]))
        # print(generate_neighbor([1, -1, 1], 3))
        # print(std_hill_climbing([10, 8, 7, 6, 5]))
        print(pp_annealing([10, 8, 7, 6, 5]))
        return

    elif len(sys.argv) != 4:
        print("Usage: python script.py <flag> <algorithm> <inputfile>")
        sys.exit(1)
    
    try:
        flag, algorithm, inputfile = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    except ValueError:
        print("Error: flag and algorithm must be integers.")
        sys.exit(1)
    
    # TODO: does inputfile need to be changed
    A = []
    with open(inputfile, 'r') as file:
        A = np.array([int(line.strip()) for line in file])

    # TODO: bro i am running python 3.9.6 and don't have match.
    match algorithm:
        case 0:
            karmarker_karp(A)
        case 1:
            std_repeated_random(A)
        case 2:
            std_hill_climbing(A)
        case 3:
            std_annealing(A)
        case 11:
            pp_repeated_random(A)
        case 12:
            pp_hill_climbing(A)
        case 13:
            pp_annealing(A)

    #deal with reading input here
    #call our method here

if __name__ == "__main__":
    main()