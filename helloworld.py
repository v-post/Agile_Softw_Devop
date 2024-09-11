# The initial test program for the class.
# The program takes one command-line argument (a name).
# Outputs "Hello, [name]!" to the console.

import sys

def main():

    # If no arguments provided - display usage and exit
    if len(sys.argv) < 2:
        print("Usage: python helloworld.py <name>")
        sys.exit(1)

    # Greet the person
    print("Hello, " + sys.argv[1] + "!")

if __name__ == "__main__":
    main()