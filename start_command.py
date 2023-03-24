import os
import random

# Define the path to the configuration file
CONFIG_FILE = os.path.expanduser("~/.my_commands")
colors = ["\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m", "\033[0;35m", "\033[0;36m"]

def print_color(text):
    color = random.choice(colors)
    print(f"{color}{text}\033[0m")

# Define the function to add a command to the configuration file
def add_command(command, description):
    with open(CONFIG_FILE, "a") as f:
        f.write(f"{command} # {description}\n")

# Define the function to display the available commands
def display_commands():
    with open(CONFIG_FILE, "r") as f:
        commands = f.readlines()
        print("==================================")
        for i, command in enumerate(commands):
            print_color(f"{i+1}. {command.strip()}")
        print("==================================")

# Define the function to execute a command
def execute_command(index):
    with open(CONFIG_FILE, "r") as f:
        commands = f.readlines()
        command = commands[index-1].split("#")[0].strip()
        os.system(command)

# Define the main function
def main():
    while True:
        print("1. Add command")
        print("2. Display commands")
        print("3. Execute command")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            command = input("Enter the command: ")
            description = input("Enter the description: ")
            add_command(command, description)
        elif choice == "2":
            display_commands()
        elif choice == "3":
            display_commands()
            index = int(input("Enter the index of the command to execute: "))
            execute_command(index)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

