import os

os.system("sudo unshadow /etc/passwd /etc/shadow > unshadowed.txt")
os.system("sudo rm /home/ns-1/.john/john.pot")
os.system("john unshadowed.txt --user=ns-1")