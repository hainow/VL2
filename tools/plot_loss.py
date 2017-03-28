import sys

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = 15, 5

def get_loss_data(file='/tmp/log.txt'):
    losses = []
    with open(file, 'r') as f:
        for line in f:
            fields = line.strip().split()
            if len(fields) <= 4:
                continue
            if fields[3] == 'solver.cpp:229]':
                losses.append(float(fields[-1]))
    print('Length of losses is {}'.format(len(losses)))
    return np.asarray(losses)

def process_losses(losses=None, window=20):
    """ Assuming display frequency is 5 iters, so we average every 20*5 = 100 iters"""
    num_splits = int(len(losses)/window)
    processed = np.split(losses[:num_splits * window], num_splits)
    p_losses = [np.average(x) for x in processed]
    print('Length of processed losses is now {}'.format(len(p_losses)))
    return p_losses

def plot_losses(p_losses=None):
    x = [(i+1)*100 for i in range(len(p_losses))]
    plt.plot(x, p_losses, color='r', marker='*', label='losses')
    plt.title("Loss value over iterations (averaged on a window of 100 iters)")
    plt.xlabel("iteration")
    plt.ylabel("loss value")
    plt.grid(True)
    xt = [i for i in x if i % 500 == 0]
    plt.xticks(xt, rotation=0, fontsize='10')
    # plt.yticks()
    plt.legend()
    # plt.savefig("loss.png")
    plt.show()

def main():
    losses = get_loss_data()
    print losses
    p_losses = process_losses(losses, 20)
    print p_losses
    plot_losses(p_losses)

if __name__ == "__main__":
    main()
