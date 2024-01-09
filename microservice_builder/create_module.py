import os
from pathlib import Path
import subprocess
from colorama import Fore

def create_service(sln_name, service_name, service_type):
    print(f"Creating service {service_name}...")

    os.chdir("src/Services")
    os.mkdir(f"{service_name}")
    os.chdir(f"{service_name}")
    subprocess.run(["dotnet", "new", "web", "-n", f"{service_name}.API", "-f", "net8.0"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "sln", f"../../../{sln_name}.sln","add", f"{service_name}.API/{service_name}.API.csproj"], stdout=subprocess.DEVNULL, shell=False)
    if(service_type == "c"):
        apply_clean_architecture_project_hierarchy(sln_name, service_name)
    os.chdir("../../..")

def apply_clean_architecture_project_hierarchy(sln_name, service_name):        
    subprocess.run(["dotnet", "new", "classlib", "-n", f"{service_name}.Application", "-f", "net8.0"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "new", "classlib", "-n", f"{service_name}.Domain", "-f", "net8.0"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "new", "classlib", "-n", f"{service_name}.Infrastructure", "-f", "net8.0"], stdout=subprocess.DEVNULL, shell=False)

    subprocess.run(["dotnet", "sln", f"../../../{sln_name}.sln","add", f"{service_name}.Application/{service_name}.Application.csproj"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "sln", f"../../../{sln_name}.sln","add", f"{service_name}.Domain/{service_name}.Domain.csproj"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "sln", f"../../../{sln_name}.sln","add", f"{service_name}.Infrastructure/{service_name}.Infrastructure.csproj"], stdout=subprocess.DEVNULL, shell=False)

    subprocess.run(["dotnet", "add", f"{service_name}.Application", "reference", f"{service_name}.Domain"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "add", f"{service_name}.Infrastructure", "reference", f"{service_name}.Application"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "add", f"{service_name}.API", "reference", f"{service_name}.Application"], stdout=subprocess.DEVNULL, shell=False)

def create_library_directory():
    os.chdir("src")
    os.mkdir("Shared")
    os.chdir("Shared")

def create_library(sln_name, lib_name): 
    print(f"Creating library {lib_name}...")

    subprocess.run(["dotnet", "new", "classlib", "-n", f"{lib_name}.Shared", "-f", "net8.0"], stdout=subprocess.DEVNULL, shell=False)    
    subprocess.run(["dotnet", "sln", f"../../{sln_name}.sln","add", f"{lib_name}.Shared/{lib_name}.Shared.csproj"], stdout=subprocess.DEVNULL, shell=False)

def create_api_gw(sln_name):
    print("Creating Ocelot API Gateway...")
    os.chdir("src")
    os.mkdir("ApiGateways")
    os.chdir("ApiGateways")
    subprocess.run(["dotnet", "new", "web", "-n", "OcelotApiGateway", "-f", "net8.0", "--force"], stdout=subprocess.DEVNULL, shell=False)
    Path("OcelotApiGateway/ocelot.Development.json").touch()
    subprocess.run(["dotnet", "restore", "OcelotApiGateway/OcelotApiGateway.csproj"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "add", "OcelotApiGateway/OcelotApiGateway.csproj", "package", "Ocelot", "--version", "20.0.0"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "restore", "OcelotApiGateway/OcelotApiGateway.csproj"], stdout=subprocess.DEVNULL, shell=False)

    subprocess.run(["dotnet", "sln", f"../../{sln_name}.sln","add", f"OcelotApiGateway/OcelotApiGateway.csproj"], stdout=subprocess.DEVNULL, shell=False)
    os.chdir("../..")
    
def create_identity_server(sln_name):
    print("Creating Identity Server...")
    os.chdir("src")
    os.mkdir("IdentityServer")
    os.chdir("IdentityServer")
    subprocess.run(["dotnet", "new", "isempty", "-n", "IdentityServer"], stdout=subprocess.DEVNULL, shell=False)
    subprocess.run(["dotnet", "sln", f"../../{sln_name}.sln","add", f"IdentityServer/IdentityServer.csproj"], stdout=subprocess.DEVNULL, shell=False)
    os.chdir("../..")

def create_tests(services, libs, is_identity_server_exists, sln_name):
    print("Creating tests file structure...")
    os.mkdir("tests")
    os.chdir("tests")
    for service in services:
        os.mkdir(f"{service["name"]}.Tests")
        subprocess.run(["dotnet", "new", "xunit", "-n", f"{service["name"]}.Tests", "-f", "net8.0"], stdout=subprocess.DEVNULL, shell=False)
        subprocess.run(["dotnet", "sln", f"../{sln_name}.sln","add", f"{service["name"]}.Tests/{service["name"]}.Tests.csproj"], stdout=subprocess.DEVNULL, shell=False)

    for lib in libs:
        os.mkdir(f"{lib["name"]}.Tests")
        subprocess.run(["dotnet", "new", "xunit", "-n", f"{lib["name"]}.Tests", "-f", "net8.0"], stdout=subprocess.DEVNULL, shell=False)
        subprocess.run(["dotnet", "sln", f"../{sln_name}.sln","add", f"{lib["name"]}.Tests/{lib["name"]}.Tests.csproj"], stdout=subprocess.DEVNULL, shell=False)

    if(is_identity_server_exists):
        os.mkdir(f"IdentityServer.Tests")
        subprocess.run(["dotnet", "new", "xunit", "-n", f"IdentityServer.Tests", "-f", "net8.0"], stdout=subprocess.DEVNULL, shell=False)
        subprocess.run(["dotnet", "sln", f"../{sln_name}.sln","add", f"IdentityServer.Tests/IdentityServer.Tests.csproj"], stdout=subprocess.DEVNULL, shell=False)

    os.chdir("..")

def create_client_app(client_app_name):
    print("Creating client app...")
    os.chdir("src")
    os.mkdir("ClientApp")
    os.chdir("ClientApp")
    print("Installing node modules...")
    subprocess.run(["npx", "create-react-app", f"{client_app_name}"], stdout=subprocess.DEVNULL, shell=True)
    print(Fore.GREEN + "Client app created!")
    os.chdir("../..")   

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