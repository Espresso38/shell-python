import sys


def main():
    
    valid_commands = []

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        if command == "exit 0":
            False
            sys.exit()
        elif command not in valid_commands:
            print(f"{command}: command not found")
            continue
        

if __name__ == "__main__":
    main()
