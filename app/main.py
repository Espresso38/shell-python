import sys
import os
import subprocess
from pathlib import Path
import urllib.request
import shutil


def find_executable(cmd: str) -> str:
    path = os.environ.get("PATH")
    executable_dirs = path.split(":")
    for dir in executable_dirs:
        if os.path.exists(f"{dir}/{cmd}"):
            return f"{dir}/{cmd}"
    return None


def path_exist(my_path: Path, cmd: str):
    if my_path.exists() and my_path.is_dir():
        os.chdir(my_path)
    else:
        print(f"{cmd}: {my_path}: No such file or directory")
        sys.stdout.flush()


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        input_command = input().strip()
        if not input_command:
            continue
        cmd, *args = input_command.split()
        command_types = {
            "echo": "builtin",
            "exit": "builtin",
            "type": "builtin",
            "pwd": "builtin",
            "cd": "builtin",
        }
        
        #Print text
        if cmd == "echo":
            sys.stdout.write(" ".join(args) + "\n")
        
        #Exit programm
        elif cmd == "exit":
            sys.exit(0)
        
        #Check for builtin commands
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
        
        #Return current directory
        elif cmd == "pwd":
            print(os.getcwd())
        elif cmd == "cd":
            if (len(args) == 0) or (args[0] == "~"):
                new_path = Path.home()
            else:
                link = args[0]
                new_path = Path(link).expanduser().resolve()
            path_exist(new_path, cmd)
        
        #Create new directory
        elif cmd == "mkdir":
            if not os.path.exists(args[1]):
                os.mkdir(args[1])
            else:
                print("Directory already exists.")
        
        #Show files in current directory
        elif cmd == "ls":
            obj = os.scandir()
            for file in obj:
                if file.is_dir() or file.is_file():
                    print(file.name, end= " ")
            print()
        
        #Download file from link
        elif cmd == "wget":
            url = args[0]
            file_path = args[0].split("/")[-1]
            urllib.request.urlretrieve(url, file_path)
        
        #Remove file or directory
        elif cmd == "rm":
            if os.path.isfile(args[0]):
                os.remove(args[0])
            elif os.path.isdir(args[0]):
                shutil.rmtree(args[0])
        
        #If nothing matches
        else:
            path = find_executable(cmd)
            if not path:
                sys.stdout.write(f"{input_command}: command not found\n")
            else:
                subprocess.run([cmd] + args)


if __name__ == "__main__":
    main()
