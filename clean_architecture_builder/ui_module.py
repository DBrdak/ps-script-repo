import os
import re
from colorama import Fore
from prompt_toolkit import prompt
import pyreadline3 as readline
from prompt_toolkit.completion import PathCompleter
    
def validated_input(text, valid_values):
    result = input('✅' + text)

    if result in valid_values or re.match(re.compile(valid_values), result):
        return result
    else:
        raise Exception("Invalid input!")
    
def display_user_interface():
  proj_name_pattern = r"^[a-zA-Z][a-zA-Z0-9_-]*$"
  print(Fore.BLUE + "Running .NET init clean architecture project")
  print("You are going to create new project on current path")

  current_working_directory = os.getcwd().__str__()

  sln_relative_path = prompt(f"Current working directory (Your project will be created here): {current_working_directory}\n> ", completer=PathCompleter())

  sln_path = os.path.join(current_working_directory, sln_relative_path)

  proj_name = validated_input("Project name: ", proj_name_pattern)

  return {"sln_path": sln_path, "proj_name": proj_name}