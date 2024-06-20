import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    commands = input()
    for command in commands:
        sys.stdout.write(f"{command}: command not found\n")

if __name__ == "__main__":
    main()
