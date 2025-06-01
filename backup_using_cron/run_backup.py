
#!/usr/bin/env python3

import subprocess

with open("/home/jdoe/ch14/.py_password.txt", "r") as file:
    password = file.read().strip()

command = f"ansible-playbook -i /home/jdoe/ch14/inventory --vault-password-file <(echo {password}) /home/jdoe/ch14/14_run_backup.yml >> /home/jdoe/ch14/cron_log.txt 2>&1"

subprocess.run(command, shell=True)
