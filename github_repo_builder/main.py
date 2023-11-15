import os
import subprocess
import sys
import keyboard
from colorama import Fore, init as colorama_init
    
def validated_input(text, valid_values):
    result = input('✅' + text)

    if result in valid_values or re.match(re.compile(valid_values), result):
        return result
    else:
        raise Exception("Invalid input!")
    
def on_esc_pressed(e):
    if e.name == 'esc':
        print("Exiting the application.")
        raise SystemExit

keyboard.hook(on_esc_pressed)

colorama_init(autoreset=True)

repo_name_pattern = r"^[a-zA-Z][a-zA-Z0-9_-]*$"

def get_github_username():
    input = shared.validated_input("Initialize React app? ([y]es/[n]o): ", ["y", "n"]).lower()

    print(Fore.YELLOW + "WARNING! You must pass username of currently logged github account, otherwise error will be thrown")
    username = input("Github username: ")
    return username

def create_git_repo(repo_name, username):
    print("Creating Git repo...")
    subprocess.run(["dotnet", "new", "gitignore"], stdout=subprocess.DEVNULL, shell=False)
    print("Adding current directory...")
    subprocess.run(["git", "init", "-b", "master"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["git", "add", "."], stdout=subprocess.DEVNULL, shell=False)
    print("Commiting changes...")
    subprocess.run(["git", "commit", "-m", "Initial commit"], stdout=subprocess.DEVNULL, shell=False)
    print("Pushing repo to Github")
    subprocess.run(["gh", "repo", "create", f"{repo_name}", "--private"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["git", "remote", "add", "github", f"https://github.com/{username}/{repo_name}.git"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["git", "push", "-u", "github", "master"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["git", "commit", "-m", "Initial commit"], stdout=subprocess.DEVNULL, shell=False)
    print("Creating development branch...")
    subprocess.run(["git", "checkout", "-b", "init-develop", "master"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["git", "push", "github", "init-develop"], stdout=subprocess.DEVNULL, shell=False)

current_working_directory = os.getcwd()

print(Fore.BLUE + f"Running github repo creator for directory: {current_working_directory}")
print(Fore.YELLOW + f"WARNING! Repository will be created with .NET support")
repo_name = validated_input("Repository name: ", repo_name_pattern)
