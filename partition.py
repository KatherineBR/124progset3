def main():
    if len(sys.argv) == 0:
        #for testing!
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