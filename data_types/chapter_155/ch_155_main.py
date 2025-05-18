import sys
import os
from memory_profiler import profile

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

@profile
def doo():
    with open(
        "/mnt/cedfd553-f07c-4741-b2af-1d196ba43a6a/projects/algo/chapter_155/ch_155_file.txt"
    ) as file:

        for index, string in enumerate(file):
            if index == 2:
                print("Номер строки {}, Содержимое: {}".format(index, string))
                break



doo()