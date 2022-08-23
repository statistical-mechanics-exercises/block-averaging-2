import matplotlib.pyplot as plt
import numpy as np

# Read in the energies from a file
eng = np.loadtxt("energies")[:,1]

# Create a list with 10 elements that you will use to hold the average eneriges
av_eng = 10*[0]

# Your code goes here
bsize = int( len(eng) / 10 )
for i in range(10) :
    av_eng[i] = sum( eng[bsize*i:bsize*(i+1)] ) / bsize


# This will draw a graph of your energies
x = np.linspace( 1, 10, 10 )
plt.plot( x, av_eng, 'ko')
plt.xlabel("Index")
plt.ylabel("Energy / natural units")
plt.savefig( "block_averages.png")
