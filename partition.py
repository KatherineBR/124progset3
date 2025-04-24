import sys
import random
import math
import heapq
import numpy as np

max_iter = 10000

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
    # print(n)
    
    # Randomly generate some starting sequence
    seq = [random.choice([1, -1]) for _ in range(n)]

    loweringcount = 0
    # Repeatedly generate sequences and take the better one
    for _ in range(max_iter):
        seq1 = [random.choice([1, -1]) for _ in range(n)]
        if residue(A, seq1) < residue(A, seq):
            seq = seq1
            loweringcount += 1
    # print(loweringcount)
    return residue(A, seq)

def std_hill_climbing(A):
    n = len(A)

    # Randomly generate some starting sequence
    seq = [random.choice([1, -1]) for _ in range(n)]

    # Iterate over possible neighbors, only taking the better one
    loweringcount = 0
    for _ in range(max_iter):
        seq1 = generate_neighbor(seq, n)

        if residue(A, seq1) < residue(A, seq):
            seq = seq1
            loweringcount += 1

    # print(loweringcount)
    return residue(A, seq)

def std_annealing(A):
    n = len(A)

    seq = [random.choice([-1, 1]) for _ in range(n)]
    seq2 = seq

    for i in range(max_iter):
        seq1 = generate_neighbor(seq, n)

        if residue(A, seq1) < residue(A, seq):
            seq = seq1
        else:
            prob = math.exp(-(residue(A, seq1) - residue(A, seq) / T(i)))
            if random.random() < prob:
                seq = seq1

        if residue(A, seq) < residue(A, seq2):
            seq2 = seq
    
    return residue(A, seq2)


def generate_neighbor_pp(p, n):
    new_p = p.copy()
    i = random.choice(range(n)) # randrange is inclusive, exclusive
    j = random.choice(range(n)) 
    while new_p[i] == j:
        j = random.choice(range(n)) 
    new_p[i] = j
    return new_p


def pp_repeated_random(A):
    n = len(A)
    seq = [random.choice(range(n)) for _ in range(n)]
    for _ in range(max_iter):
        seq1 = [random.choice(range(n)) for _ in range(n)]
        if pp_karmarker_karp(A, seq1) < pp_karmarker_karp(A, seq):
            seq = seq1

    return pp_karmarker_karp(A, seq)

def pp_hill_climbing(A):
    n = len(A)

    # Randomly generate some starting sequence
    seq = [random.choice(range(n)) for _ in range(n)]
    # print("seq: " + str(seq))

    # Iterate over possible neighbors, only taking the better one
    lowercounter = 0
    for _ in range(max_iter):
        seq1 = generate_neighbor_pp(seq, n)
        # print("seq: " + str(seq))
        # print("seq1: " + str(seq1))
        # print("karmarker diff: " + str(pp_karmarker_karp(A, seq1) - (pp_karmarker_karp(A, seq))))
        if pp_karmarker_karp(A, seq1) < pp_karmarker_karp(A, seq):
            lowercounter += 1
            seq = seq1
    # print(lowercounter)
    
    return pp_karmarker_karp(A, seq)
    

def pp_annealing(A):
    n = len(A)

    seq = [random.choice(range(n)) for _ in range(n)]
    seq2 = seq

    for i in range(max_iter):
        seq1 = generate_neighbor_pp(seq, n)

        if pp_karmarker_karp(A, seq1) < pp_karmarker_karp(A, seq):
            seq = seq1
        else:
            prob = math.exp(-(pp_karmarker_karp(A, seq1) - pp_karmarker_karp(A, seq) / T(i)))
            if random.random() < prob:
                seq = seq1

        if pp_karmarker_karp(A, seq) < pp_karmarker_karp(A, seq2):
            seq2 = seq
    
    return pp_karmarker_karp(A, seq2)


def main():
    if len(sys.argv) == 1:
        #for testing!
        # print(residue([10,12,5,8], [-1, 1, 1, -1]))
        # print(pp_repeated_random([10, 8, 1, 7, 6, 5]))
        # print(karmarker_karp([10, 8, 7, 6, 5]))
        # print(pp_karmarker_karp([10, 8, 7, 6, 5], [1, 2, 2, 4, 5]))
        # print(generate_neighbor_pp([2, 2, 1], 3))
        # print(std_hill_climbing([10, 8, 7, 6, 5]))
        # print(pp_annealing([10, 8, 7, 6, 5]))

        # Task 2
        data = []
        instance = [0] * 7
        for i in range(1):
            A = [random.choice(range(10**12)) for _ in range(n)]
            # print(A)
            instance[0] = karmarker_karp(A)
            instance[1] = std_repeated_random(A)
            instance[2] = std_hill_climbing(A)
            instance[3] = std_annealing(A)
            instance[4] = pp_repeated_random(A)
            instance[5] = pp_hill_climbing(A)
            instance[6] = pp_annealing(A)
            data.append(instance)
        print(data)
        return

    elif len(sys.argv) != 4:
        print("Usage: python script.py <flag> <algorithm> <inputfile>")
        sys.exit(1)
    
    try:
        flag, algorithm, inputfile = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    except ValueError:
        print("Error: flag and algorithm must be integers.")
        sys.exit(1)
    
    A = []
    with open(inputfile, 'r') as file:
        A = np.array([int(line.strip()) for line in file])

    # TODO: bro i am running python 3.9.6 and don't have match.
    match algorithm:
        case 0:
            print(karmarker_karp(A))
        case 1:
            print(std_repeated_random(A))
        case 2:
            print(std_hill_climbing(A))
        case 3:
            print(std_annealing(A))
        case 11:
            print(pp_repeated_random(A))
        case 12:
            print(pp_hill_climbing(A))
        case 13:
            print(pp_annealing(A))

if __name__ == "__main__":
    main()