# The initial test program for the class.
# The program takes one command-line argument (a name).
# Outputs "Hello, [name]!" to the console.

import sys

def main():

    # Arguments passed
    print("Hello " + sys.argv[1] + "!")

if __name__ == "__main__":
    main()