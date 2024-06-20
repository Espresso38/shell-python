import sys
import os


def main():
    
    valid_commands = ["echo", "exit", "type"]
    PATH = os.environ.get("PATH")

    paths = PATH.split(":")

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
                    continue
                elif lst_input[1] == "ls":
                    print(f"ls is {paths[0]}/ls")
                    continue
                elif lst_input[1] in paths[1]:
                    print(f"{lst_input[1]} is {paths[1]}/{lst_input[1]}")
                    continue
                else:
                    print(f"{lst_input[1]}: not found")
                    continue
        

if __name__ == "__main__":
    main()
