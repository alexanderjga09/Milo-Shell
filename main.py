import sys
import os


def main() -> None:
    status = True

    while status:
        try:
            prompt = f"{(path:= os.getcwd())}$> "
            line = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            # Graceful exit on Ctrl-D / Ctrl-C
            print()
            break

        if not line:
            continue

        parts = line.split()
        if parts[0] != "milo":
            continue

        match parts[1].lower():
            case "execute" | "exec":
                try:
                    os.startfile(parts[2])
                    print("\n")

                except FileNotFoundError:
                    print(f"Error: File '{parts[2]}' not found.\n")
                
                except IndexError:
                    print("Error: Missing arguments for 'milo execute'. Usage: milo execute <file_path>\n")
            
            case "close" | "cl":
                try:
                    os.kill(int(parts[2]))
                except (IndexError, ValueError):
                    print("Error: Missing or invalid process ID for 'milo close'. Usage: milo close <pid>\n")

            case "quit":
                status = False


if __name__ == "__main__":
    main()