#!/bin/bash

ansible-playbook -i /etc/ansible/hosts/inventory.ini --vault-password-file /etc/ansible/hosts/cron/sh_password.txt /etc/ansible/hosts/cron/backup_running_cfg_scp.yml >> /home/user/cronsecure_log.txt 2>&1
