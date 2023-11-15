import curses
import sys
from colorama import Fore, init as colorama_init
import keyboard
import ui_module as ui
import execute_module as exec

def on_esc_pressed(e):
    if e.name == 'esc':
        print("Exiting the application.")
        raise SystemExit

keyboard.hook(on_esc_pressed)


curses.curs_set(0)
curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)

colorama_init(autoreset=True)

while True:
  try:
    ui.input_select()
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
  except SystemExit:
     sys.exit()
  except Exception as e:
    print(Fore.RED + str(e))
    continue