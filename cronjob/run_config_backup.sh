
#!/bin/bash

ansible-playbook -i /home/jdoe/cronjob1/inventory --vault-password-file /home/jdoe/cronjob1/password.txt /home/jdoe/cronjob1/13_icmp_mgt_int_test01.yml >> /home/jdoe/cronjob1/cronjob1_log.txt 2>&1
