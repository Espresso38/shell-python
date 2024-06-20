import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()

    sys.stdout(f"{command}: command not found")

if __name__ == "__main__":
    main()
