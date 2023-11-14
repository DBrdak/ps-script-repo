import os
import subprocess
import create_module as factory
from colorama import Fore


def consume_answers(sln_name, services, libs, is_apigw_required, is_identity_server_required, is_client_at_init, is_test_dir_at_init, is_git_at_init):
    
    # Calling scripts for creating app
    print(Fore.GREEN + "Creating microservices application...")
    os.mkdir(f"{sln_name}")
    os.chdir(f"{sln_name}")
    # Create solution
    subprocess.run(["dotnet", "new", "sln"], stdout=subprocess.DEVNULL, shell=False)

    # Create project structure
    os.mkdir("src")
    os.mkdir("src/Services")

    for service in services:
        factory.create_service(sln_name, service["name"], service["architecture"])
        
    if(len(libs) > 0):
        for lib in libs:
            factory.create_library(sln_name, lib["name"])

    if(is_apigw_required == "y"):
        factory.create_api_gw(sln_name)

    if(is_identity_server_required == "y"):
        factory.create_identity_server(sln_name)

    if(is_client_at_init == "y"):
        factory.create_client_app(sln_name)

    if(is_test_dir_at_init == "y"):
        os.mkdir("tests")

    if(is_git_at_init == "y"):
        if(is_client_at_init == "y"):
            factory.create_git_repo(sln_name, sln_name)
        else:
            factory.create_git_repo(sln_name, None)

    print("Building solution...")

    subprocess.run(["dotnet", "build", f"{sln_name}.sln"], stdout=subprocess.DEVNULL, shell=False)

    print(Fore.GREEN + "Successfully created solution")