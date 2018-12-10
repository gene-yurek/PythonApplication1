from math import cos, radians
import numpy
import matplotlib.pyplot as plt
#from array import *


# Create a string with spaces proportional to a cosine of x in degrees
def make_dot_string(x):
    rad = radians(x)                             # cos works with radians
    numspaces = int(20 * cos(radians(x)) + 20)   # scale to 0-40 spaces
    st = ' ' * numspaces + 'o'                   # place 'o' after the spaces
    return st

def main():

    #dice_size = 6
    ##sum_dice = [[0]*dice_size for i in range(dice_size)]
    #sum_dice = numpy.zeros(shape=(dice_size, dice_size))
    #sum_count =[0] * 2 * dice_size

    #for i in range(dice_size):
    #    for j in range(dice_size):
    #        sum_dice[i][j] = i+1 + j+1
    #        print(str(i+1) + " + " + str(j+1) + " is " + str(sum_dice[i][j]))
    #        sum_count[i+j] += 1

    #for i in range(len(sum_count)):
    #    if sum_count[i] > 0:
    #        print("occurance of " + str(i+2) + " is " + str(sum_count[i]))

    #for i in range(0, 1800, 12):
    #    s = make_dot_string(i)
    #    print(s)
    x = numpy.arange(0, 3 * numpy.pi, 0.001)
    y_sin = numpy.sin(x)
    y_cos = numpy.cos(x)

    plt.plot(x, y_sin)
    plt.plot(x, y_cos)

    plt.xlabel('x axis label')
    plt.ylabel('y axix label')
    plt.title('Sine and Cosine')
    plt.legend(['Sine', 'Cosine'])
    plt.show()
main()