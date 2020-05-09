import argparse
from scipy import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

#Generate arguments for max range number

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--maxnum", type=int)
args = parser.parse_args()

maxnum = args.maxnum 

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gen_prime_spiral(num_max):
    nums = np.linspace(2, num_max, num=num_max, dtype=int)
    nums = nums[1:]
    
    #Generate array of primes 

    primelist = [] #appendable list

    for num in nums:
        if is_prime(num):
            primelist.append(num)
        
    primes = np.array(primelist)
    
    #Generate polar plot of primes
    
    fig = plt.figure(figsize=(6,6))
    plt.style.use('dark_background')
    fig.patch.set_facecolor('black')
    
    ax1 = fig.add_subplot(111, projection='polar')
    ax1.scatter(primes, primes, s=1, c=primes, marker="*")
    ax1.axis('off')
    
    fig.tight_layout()
    fig.savefig("arch_spiral.png", transparent=False)
    plt.show()
    
gen_prime_spiral(maxnum)
