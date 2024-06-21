import sys
import os
import subprocess
from pathlib import Path


def find_executable(cmd: str) -> str:
    path = os.environ.get("PATH")
    executable_dirs = path.split(":")
    for dir in executable_dirs:
        if os.path.exists(f"{dir}/{cmd}"):
            return f"{dir}/{cmd}"

def path_exist(my_path, cmd):
    if my_path.exists():
        os.chdir(my_path)
    else:
        print(f"{cmd}: {my_path}: No such file or directory")

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        input_command = input()
        cmd, *args = input_command.split(" ")
        command_types = {
            "echo": "builtin",
            "exit": "builtin",
            "type": "builtin",
            "pwd": "builtin"
        }
        if cmd == "echo":
            sys.stdout.write(" ".join(args) + "\n")
        elif cmd == "exit":
            sys.exit(0)
        elif cmd == "type":
            arg = args[0] if args else ""
            cmd_type = command_types.get(arg, "nonexistent")
            if cmd_type == "builtin":
                sys.stdout.write(f"{arg} is a shell builtin\n")
            else:
                path = find_executable(arg)
                if path:
                    sys.stdout.write(f"{arg} is {path}\n")
                else:
                    sys.stdout.write(f"{arg}: not found\n")
        elif cmd == "pwd":
            print(os.getcwd())
        elif cmd == "cd":
            link = "".join(args)
            my_path = Path(link)
            if "../" in link:
                substring = "../"
                count = link.count(substring)
                cdir = os.getcwd()
                lst_dir = link.split("/")
                new_dir = Path("/".join(lst_dir[:count]))
                path_exist(new_dir, cmd)
            elif "./" in link:
                cdir = os.getcwd()
                new_link = Path(cdir + link[2:])
                path_exist(new_link, cmd)
            else:
                path_exist(my_path, cmd)
            

        else:
            path = find_executable(cmd)
            if not path:
                sys.stdout.write(f"{input_command}: command not found\n")
            else:
                subprocess.run([cmd] + args)


if __name__ == "__main__":
    main()