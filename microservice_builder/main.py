from colorama import init as colorama_init
import ui_module as ui
import execute_module as exec

colorama_init(autoreset=True)

answers = ui.display_user_interface()

exec.consume_answers(
  answers["sln_name"],
  answers["services"],
  answers["libs"],
  answers["is_apigw_required"],
  answers["is_identity_server_required"],
  answers["is_client_at_init"],
  answers["is_test_dir_at_init"],
  answers["is_git_at_init"]
)