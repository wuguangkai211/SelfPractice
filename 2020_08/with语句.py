import time

with open("2020_08/poem.txt") as f:
    for line in f:
        print(line, end='')
        time.sleep(2)
