import os
import sys
from colorama import Fore, init as colorama_init
import keyboard
import ui_module as ui
import create_module as factory

def on_esc_pressed(e):
    if e.name == 'esc':
        print("Exiting the application.")
        raise SystemExit

keyboard.hook(on_esc_pressed)

colorama_init(autoreset=True)

while True:
  try:
    answers = ui.display_user_interface()
    factory.create_project(answers["sln_path"], answers["proj_name"])
    break
  except SystemExit:
     break
  except Exception as e:
    print(Fore.RED + e)
    continue