from colorama import Fore, init as colorama_init
import ui_module as ui
import create_module as factory

colorama_init(autoreset=True)

answers = ui.display_user_interface()

factory.create_project(answers["sln_path"], answers["proj_name"])