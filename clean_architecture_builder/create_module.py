import os
import subprocess

from colorama import Fore


def create_project(sln_path, proj_name):
    
  if not os.path.isfile(sln_path):
    print(Fore.RED + "Solution not found")
    return

  print(f"Creating clean architecture project {proj_name}...")

  os.mkdir(f"{proj_name}")
  os.chdir(f"{proj_name}")
  subprocess.run(["dotnet", "new", "web", "-n", f"{proj_name}.API", "-f", "net8.0"], stdout=subprocess.DEVNULL, shell=False)
  subprocess.run(["dotnet", "sln", f"{sln_path}","add", f"{proj_name}.API/{proj_name}.API.csproj"], stdout=subprocess.DEVNULL, shell=False)
  apply_clean_architecture_project_hierarchy(sln_path, proj_name)
  os.chdir("..")
  print(Fore.GREEN + "Project created successfully")

def apply_clean_architecture_project_hierarchy(sln_path, proj_name):        
    subprocess.run(["dotnet", "new", "classlib", "-n", f"{proj_name}.Application", "-f", "net8.0"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "new", "classlib", "-n", f"{proj_name}.Domain", "-f", "net8.0"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "new", "classlib", "-n", f"{proj_name}.Infrastructure", "-f", "net8.0"], stdout=subprocess.DEVNULL, shell=False)

    subprocess.run(["dotnet", "sln", f"{sln_path}","add", f"{proj_name}.Application/{proj_name}.Application.csproj"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "sln", f"{sln_path}","add", f"{proj_name}.Domain/{proj_name}.Domain.csproj"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "sln", f"{sln_path}","add", f"{proj_name}.Infrastructure/{proj_name}.Infrastructure.csproj"], stdout=subprocess.DEVNULL, shell=False)

    subprocess.run(["dotnet", "add", f"{proj_name}.Application", "reference", f"{proj_name}.Domain"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "add", f"{proj_name}.Infrastructure", "reference", f"{proj_name}.Application"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "add", f"{proj_name}.API", "reference", f"{proj_name}.Application"], stdout=subprocess.DEVNULL, shell=False)
