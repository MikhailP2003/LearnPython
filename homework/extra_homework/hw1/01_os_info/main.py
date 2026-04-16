import platform
import sys


def main():
    with open("os_info.txt", "w", encoding="utf-8") as file:
        file.write(f"OS info is \n{platform.system()}\nPython version is {sys.version}")


if __name__ == "__main__":
    main()