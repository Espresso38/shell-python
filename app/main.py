import sys


def main():
    
    valid_commands = ["echo"]

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
        

if __name__ == "__main__":
    main()
