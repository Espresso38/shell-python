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
            if command.startswith("type"):
                cmd = command.split(" ")[1]
                cmd_path = None
                paths = PATH.split(":")
                for path in paths:
                    if os.path.isfile(f"{path}/{cmd}"):
                        cmd_path = f"{path}/{cmd}"
                if cmd in valid_commands:
                    sys.stdout.write(f"{cmd} is a shell builtin\n")
                elif cmd_path:
                    sys.stdout.write(f"{cmd} is {cmd_path}\n")
                else:
                    sys.stdout.write(f"{cmd} not found\n")
                sys.stdout.flush()
                continue
        

if __name__ == "__main__":
    main()
