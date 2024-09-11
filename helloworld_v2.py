# A second version of the initial test program for the class.
# The program takes any number of command line arguments (>0).
# Outputs "Hello, [name]!" for each argument separately.

import sys

def main():

    # If no arguments provided - display usage and exit
    if len(sys.argv) < 2:
        print("Usage: python helloworld_v2.py <name>")
        sys.exit(1)


    # Greet each person separately
    for i in range(1, len(sys.argv)):
        print("Hello " + sys.argv[i] + "!")

if __name__ == "__main__":
    main()