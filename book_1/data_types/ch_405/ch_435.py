import os

for line in os.popen("df -h"):
    if "/dev/sda1" in line:
        print(line.rstrip())
