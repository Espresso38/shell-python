import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    input = input()

    command_list = []
    command = input[1]
    if command not in command_list:
        print(f"{command}: command not found")

if __name__ == "__main__":
    main()
