import sys

def main():
    if len(sys.argv) != 3:
        print("Uzycie: python main.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    print("Plik wejsciowy:", input_file)
    print("Plik wyjsciowy:", output_file)

if __name__ == "__main__":
    main()
