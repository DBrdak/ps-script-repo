import re
from colorama import Fore
    
def validated_input(text, valid_values):
    result = input('✅' + text)

    if result in valid_values or re.match(re.compile(valid_values), result):
        return result
    else:
        raise Exception("Invalid input!")
    
def get_github_username():
    input = validated_input("Initialize React app? ([y]es/[n]o): ", ["y", "n"]).lower()

    if input == "y":
        print(Fore.YELLOW + "WARNING! You must pass username of currently logged github account, otherwise error will be thrown")
        username = input("Github username: ")
        return username
    else:
        return None

proj_sln_name_pattern = r"^[a-zA-Z][a-zA-Z0-9_-]*$"

def display_user_interface():
  print(Fore.BLUE + "Running .NET solution init for microservices architecture")
  print("You are going to create new application on current path")

  # Get data about solution
  sln_name = validated_input("Solution name: ", proj_sln_name_pattern)

  services = []
  libs = []

  i = 1

  # Get data about services
  while True:
      print(f"Configuring service no. {i}")
      service_name = validated_input(f"Service name: ", proj_sln_name_pattern)

      service_architecture = validated_input("Architecture ([m]onolith, [c]lean architecture): ", ["m", "c"])

      service = {
          "name": service_name,
          "architecture": service_architecture
      }

      services.append(service)

      more_services = validated_input("Add another service? ([y]es/[n]o): ", ["y", "n"])
      if(more_services.lower() == "y"): 
          i += 1
          continue
      else:
          i = 1
          break

  # Get data about shared libraries
  while True:
      is_lib_required = validated_input("Would you like to create shared library? ([y]es/[n]o): ", ["y", "n"])

      if(is_lib_required == "n"):
          break

      print(f"Configuring shared library no. {i}")
      lib_name = validated_input(f"Shared library name: ", proj_sln_name_pattern)

      lib = {
          "name": lib_name,
      }

      libs.append(lib)

      more_libs = validated_input("Add another library? ([y]es/[n]o): ", ["y", "n"])
      if(more_libs.lower() == "y"): 
          i += 1
          continue
      else:
          i = 0
          break
      
  # Get data about creating identity server
  is_identity_server_required = validated_input("Add Identity Server? ([y]es/[n]o): ", ["y", "n"]).lower() == "y"

  # Get data about creating api gateway
  is_apigw_required = validated_input("Add Ocelot API Gateway? ([y]es/[n]o): ", ["y", "n"]).lower() == "y"

  # Get data about tests
  is_test_dir_at_init = validated_input("Initialize tests direction at init? ([y]es/[n]o): ", ["y", "n"]).lower() == "y"

  # Get data about client side
  is_client_at_init = validated_input("Initialize React app? ([y]es/[n]o): ", ["y", "n"]).lower() == "y"

  #Get data about git
  gh_username = len(get_github_username()) > 0

  return {"sln_name": sln_name, 
          "services": services, 
          "libs": libs, 
          "is_identity_server_required": is_identity_server_required, 
          "is_apigw_required": is_apigw_required, 
          "is_test_dir_at_init": is_test_dir_at_init, 
          "is_client_at_init": is_client_at_init, 
          "gh_username": gh_username}