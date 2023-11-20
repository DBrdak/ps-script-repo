import sys
from colorama import Fore, init as colorama_init
import keyboard
import ui_module as ui
import execute_module as exec

colorama_init(autoreset=True)

while True:
  try:
    answers = ui.display_user_interface()
    exec.consume_answers(
      answers["sln_name"],
      answers["services"],
      answers["libs"],
      answers["is_apigw_required"],
      answers["is_identity_server_required"],
      answers["is_client_at_init"],
      answers["is_test_dir_at_init"],
      answers["gh_username"]
    )   
    break
  except Exception as e:
    print(Fore.RED + str(e))
    continue