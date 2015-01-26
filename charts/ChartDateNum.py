#this script is created for ---- draw the hist which date on the X ticks.
__author__ = 'fandongyun'

import numpy as np
from matplotlib import pyplot as plt


def plot_wave(days_list, num_list, file_name):
    plt.figure(figsize=(12, 8))
    plt.plot(range(len(days_list)), num_list)
    #plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.xticks(range(len(days_list)), str(days_list))
    plt.tight_layout()
    plt.savefig("./output/" + file_name)
    if __name__ == "__main__":
        plt.show()

def plot_hist(days_list, num_list, file_name):
    plt.figure(figsize=(12, 8))
    #plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.hist(num_list,bins=len(num_list))
    plt.xticks(range(len(days_list)), str(days_list))
    plt.tight_layout()
    plt.savefig("./output/" + file_name)
    if __name__ == "__main__":
        plt.show()


if __name__ == "__main__":
    import calendar
    date_list = []
    for i in calendar.Calendar().itermonthdates(2014,3):
        date_list.append(str(i))
    import random
    nums = [random.randint(100,500) for x in range(len(date_list))]
    plot_wave(date_list, nums,"DateNum_wave.jpg")
    plot_hist(date_list, nums,"DateNum_hist.jpg")

