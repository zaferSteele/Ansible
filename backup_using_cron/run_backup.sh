#!/bin/bash

ansible-playbook -i /home/jdoe/ch14/inventory --vault-password-file /home/jdoe/ch14/sh_password.txt /home/jdoe/ch14/14_run_backup.yml >> /home/jdoe/ch14/run_backup_log.txt 2>&1
