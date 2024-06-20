import sys


def main():
    
    valid_commands = ["echo"]

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
        else:
            if "echo" in command:
                list_of_text = command.split()
                output = " ".join(list_of_text[1:])
                print(output)
        

if __name__ == "__main__":
    main()
