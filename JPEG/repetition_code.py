import random
import numpy as np
import matplotlib.pyplot as plt
##############encoder##################
def repeatition(inp_list):
    temp3=''
    for i in range(len(inp_list)):
        temp1 = inp_list[i]
        temp2 = temp1*3
        temp3 += temp2
    return temp3
###############decoder#################
def inv_repeatition(inp_list):
    i = 0
    zero_count = 0
    one_count = 0
    temp2 = ''
    while True:
        temp1 = inp_list[i:i+3]
        for j in range(3):
            if temp1[j]=='0':
                zero_count+=1
            else:
                one_count+=1
        if zero_count > one_count:
            temp2+='0'
        else:
            temp2+='1'
        i+=3
        if i == len(inp_list):
            break
        zero_count = 0
        one_count = 0
    return temp2


