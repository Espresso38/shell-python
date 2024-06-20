import sys


def main():
    
    valid_commands = ["echo", "exit", "type"]

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        lst_input = command.split()
        if lst_input[0] == "exit":
            False
            sys.exit()
        elif lst_input[0] not in valid_commands:
            print(f"{command}: command not found")
            continue
        else:
            if lst_input[0] == "echo":
                output = " ".join(lst_input[1:])
                print(output)
            elif lst_input[0] == "type":
                if lst_input[1] in valid_commands:
                    print(f"{lst_input[1]} is a shell builtin")
        

if __name__ == "__main__":
    main()
