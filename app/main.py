import sys


def main():
    
    valid_commands = []

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        if command not in valid_commands:
            print(f"{command}: command not found")
            continue
        elif command == "exit 0":
            False
            sys.exit()

if __name__ == "__main__":
    main()
