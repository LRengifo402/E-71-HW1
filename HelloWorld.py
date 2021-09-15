# Hello World with single argument
import sys

if __name__ == '__main__':
    # Read arguments - if arguments found, assign the second position to variable 'name'
    # If no arguments found, assign 'World' to the variable 'name'.

    if len(sys.argv) >= 2:
        name = sys.argv[1]
    else:
        name = 'World'
    print('Hello, ' + name + '!')
