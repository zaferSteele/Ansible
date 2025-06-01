#!/bin/bash

/usr/bin/ansible-playbook --vault-password-file /home/jdoe/password.txt /home/jdoe/repo1/ch13/13.2_backup_cronjob.yml
