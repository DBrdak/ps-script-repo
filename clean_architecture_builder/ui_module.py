from colorama import Fore


def validated_input(text, valid_values):
  result = input(text)

  if result in valid_values or re.match(re.compile(valid_values), result):
      return result
  else:
      raise Exception("Invalid input!")
    

def display_user_interface():
  proj_name_pattern = r"^[a-zA-Z][a-zA-Z0-9_-]*$"
  print(Fore.BLUE + "Running .NET init clean architecture project")
  print("You are going to create new project on current path")

  sln_path = validated_input("Solution path: ", "*.sln")

  proj_name = validated_input("Project name: ", proj_name_pattern)

  return {"sln_path": sln_path, "proj_name": proj_name}