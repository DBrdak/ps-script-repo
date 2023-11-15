import os
import subprocess
import create_module as factory
from colorama import Fore
from github_repo_builder.main import create_git_repo


def consume_answers(sln_name, services, libs, is_apigw_required, is_identity_server_required, is_client_at_init, is_test_dir_at_init, gh_username):
    print(Fore.GREEN + "Creating microservices application...")
    os.mkdir(f"{sln_name}")
    os.chdir(f"{sln_name}")
    subprocess.run(["dotnet", "new", "sln"], stdout=subprocess.DEVNULL, shell=False)

    os.mkdir("src")
    os.mkdir("src/Services")

    for service in services:
        factory.create_service(sln_name, service["name"], service["architecture"])
        
    if(len(libs) > 0):
        for lib in libs:
            factory.create_library(sln_name, lib["name"])

    if(is_apigw_required):
        factory.create_api_gw(sln_name)

    if(is_identity_server_required):
        factory.create_identity_server(sln_name)

    if(is_client_at_init):
        factory.create_client_app(sln_name)

    if(is_test_dir_at_init):
        factory.create_tests(services, libs, is_identity_server_required)

    if(len(gh_username)):
        factory.create_git_repo(sln_name, gh_username)

    print("Building solution...")

    subprocess.run(["dotnet", "build", f"{sln_name}.sln"], stdout=subprocess.DEVNULL, shell=False)

    print(Fore.GREEN + "Successfully created solution")