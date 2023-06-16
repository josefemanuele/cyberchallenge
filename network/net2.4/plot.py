import matplotlib.pyplot as plt

with open('draw.txt') as file:
    for line in file.readlines():
        command = line.strip().split(',')
        start = [command[3], command[4]]
        end = [command[5], command[6]]
        plt.plot(start, end)
    plt.show()
