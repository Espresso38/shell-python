import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    input()

    command_list = []
    command = sys.argv[1]
    if command not in command_list:
        print(f"{command}: command not found")

if __name__ == "__main__":
    main()
