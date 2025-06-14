import subprocess

with open("/etc/ansible/hosts/cron/py_password.txt", "r") as file:
    password = file.read().strip()

command= f"sudo ansible-playbook -i /etc/ansible/hosts/inventory.ini --vault-password-file <(echo {password}) /etc/ansible/hosts/cron/backup_running_cfg_scp.yml >> /home/user/cronsecurepy_log.txt 2>&1"

subprocess.run(command, shell=True)