import numpy as np
import math
from math import cos, pi, floor
import random
def FDCT3(S):
    F = np.ones((8,8))
    M = []
    m0 = np.array([1/(2*math.sqrt(2)) for x in range (8)])
    m1 = [[0 for k1 in range(8)] for k2 in range(7)]
    for u0 in range(7):
        u = u0+1
        m1[u0] = np.array([0.5*math.cos(((2*v+1)*u*math.pi)/16) for v in range (8)])
    M = np.asmatrix(np.vstack((m0,m1)))
    F = M*S*np.transpose(M)
    return F

def quan(img): #要改用陣列表示省掉一個迴圈
    quan =np.array([[16,11,10,16,24,40,51,61],
                    [12,12,14,19,26,58,60,55],
                    [14,13,16,24,40,57,69,56],
                    [14,17,22,29,51,87,80,62],
                    [18,22,37,56,68,109,103,77],
                    [24,35,55,64,81,104,113,92],
                    [49,64,78,87,103,121,120,101],
                    [72,92,95,98,112,100,103,99]])
    quan = np.asmatrix(quan)
    for x in range(8):
        for y in range(8):
            img[x,y] = img[x,y]/quan[x,y]
    return img

def quan_try(img,Q): 
    if Q<1:
        Q=1
    elif Q>99:
        Q=99
    if Q<50:
        S = 5000/Q
    else:
        S = 200 - 2*Q
    new_quan = np.ones((8,8))
    base_quan=np.array([[16,11,10,16,24,40,51,61],
                        [12,12,14,19,26,58,60,55],
                        [14,13,16,24,40,57,69,56],
                        [14,17,22,29,51,87,80,62],
                        [18,22,37,56,68,109,103,77],
                        [24,35,55,64,81,104,113,92],
                        [49,64,78,87,103,121,120,101],
                        [72,92,95,98,112,100,103,99]])
    quan = np.asmatrix(base_quan)
    for x in range(8):
        for y in range(8):
            new_quan[x,y]=math.floor((quan[x,y]*S+50)/100)
            if new_quan[x,y]<1:
                new_quan[x,y]=1
            img[x,y] = img[x,y]/new_quan[x,y]
    return img
'''
aa = np.ones((8,8))*100
print(aa)
bb = quan_try(aa, 63)
print(bb)
cc = np.round_(bb,0)
print(cc)
'''
def zigzag(img):
    z = 0
    X = np.array([0,0,1,2,1,0,0,1,2,3,4,3,2,1,0,0,
                1,2,3,4,5,6,5,4,3,2,1,0,0,1,2,3,
                4,5,6,7,7,6,5,4,3,2,1,2,3,4,5,6,
                7,7,6,5,4,3,4,5,6,7,7,6,5,6,7,7])
    Y = np.array([0,1,0,0,1,2,3,2,1,0,0,1,2,3,4,5,
                4,3,2,1,0,0,1,2,3,4,5,6,7,6,5,4,
                3,2,1,0,1,2,3,4,5,6,7,7,6,5,4,3,
                2,3,4,5,6,7,7,6,5,4,5,6,7,7,6,7])
    Z = np.zeros((64))
    for i in range(64): 
            Z[z] = img[X[i],Y[i]]
            z += 1
    return Z

def RLE_AC(array1):
    array2 = array1
    array3 = [int(array2[0])]
    k = 0

    for i in range (63):
        #print(i)
        #print(array3)
        if array2[i+1] == 0:
            k += 1
            if  i+1 == 63:
                array3.append("EOB")
                break
        else:
            while k >= 16:
                array3.append([15,0])
                k -= 16
            array3.append([k,int(array2[i+1])])
            k = 0
        #print(k)
    return array3

def InvRLE_AC(array1): 
    array2 = array1
    array3 = [array2[0]]
    i = 1
    code_length = 1
    while code_length < 64:
        if array2[i] == [15,0]:
            array3.extend([0]*16)
            code_length += 16
            i+=1
        elif array2[i][0] == 'E':
            array3.extend([0]*(64 - len(array3)))
            code_length = 64
        else:
            array3.extend([0]*int(array2[i][0]))
            code_length += int(array2[i][0])
            array3.append(array2[i][1])
            code_length += 1
            i += 1
            
    return array3

def izigzag(Z):
    z = 0
    X = np.array([0,0,1,2,1,0,0,1,2,3,4,3,2,1,0,0,
                1,2,3,4,5,6,5,4,3,2,1,0,0,1,2,3,
                4,5,6,7,7,6,5,4,3,2,1,2,3,4,5,6,
                7,7,6,5,4,3,4,5,6,7,7,6,5,6,7,7])
    Y = np.array([0,1,0,0,1,2,3,2,1,0,0,1,2,3,4,5,
                4,3,2,1,0,0,1,2,3,4,5,6,7,6,5,4,
                3,2,1,0,1,2,3,4,5,6,7,7,6,5,4,3,
                2,3,4,5,6,7,7,6,5,4,5,6,7,7,6,7])
    img = np.zeros((8,8))
    for i in range(64): 
            img[X[i],Y[i]] = Z[z]
            z += 1
    return img

def iquan(img):
    iquan =np.array([[16,11,10,16,24,40,51,61],
                     [12,12,14,19,26,58,60,55],
                     [14,13,16,24,40,57,69,56],
                     [14,17,22,29,51,87,80,62],
                     [18,22,37,56,68,109,103,77],
                     [24,35,55,64,81,104,113,92],
                     [49,64,78,87,103,121,120,101],
                     [72,92,95,98,112,100,103,99]])
    iquan = np.asmatrix(iquan)
    for x in range(8):
        for y in range(8):
            img[x,y] = img[x,y]*iquan[x,y]
    return img

def iquan_try(img,Q): 
    if Q<1:
        Q=1
    elif Q>99:
        Q=99
    if Q<50:
        S = 5000/Q
    else:
        S = 200 - 2*Q
    new_iquan = np.ones((8,8))
    base_iquan=np.array([[16,11,10,16,24,40,51,61],
                        [12,12,14,19,26,58,60,55],
                        [14,13,16,24,40,57,69,56],
                        [14,17,22,29,51,87,80,62],
                        [18,22,37,56,68,109,103,77],
                        [24,35,55,64,81,104,113,92],
                        [49,64,78,87,103,121,120,101],
                        [72,92,95,98,112,100,103,99]])
    iquan = np.asmatrix(base_iquan)
    for x in range(8):
        for y in range(8):
            new_iquan[x,y]=math.floor((iquan[x,y]*S+50)/100)
            if new_iquan[x,y]<1:
                new_iquan[x,y]=1
            img[x,y] = img[x,y]*new_iquan[x,y]
    return img

def iFDCT3(S1):
    f = np.ones((8,8))
    M = []
    m0 = np.array([1/(2*math.sqrt(2)) for x in range (8)])
    m1 = [[0 for k1 in range(8)] for k2 in range(7)]
    for u0 in range(7):
        u = u0+1
        m1[u0] = np.array([0.5*math.cos(((2*v+1)*u*math.pi)/16) for v in range (8)])
    M = np.asmatrix(np.vstack((m0,m1)))
    f = np.transpose(M)*S1*M
    return f

def error_check(list1, list2):
    for k in range(32):
        for h in range(32):
            if list1[k][h] != list2[k][h]:
                print("出現錯誤, 原輸入{}位置[{},{}] ==> {}".format(list1[k][h], k,h, list2[k][h]))

def AAN_FDCT(v):
    #vector = np.transpose(vector)
    C = [math.cos(math.pi / 16 * i) for i in range(8)]
    S = [1 / (4 * val) for val in C]
    S[0] = 1 / (2 * math.sqrt(2))
    A = [None,C[4],C[2] - C[6],C[4],C[6] + C[2],C[6]]
    a0 = v[0] + v[7]
    a1 = v[1] + v[6]
    a2 = v[2] + v[5]
    a3 = v[3] + v[4]
    a4 = v[3] - v[4]
    a5 = v[2] - v[5]
    a6 = v[1] - v[6]
    a7 = v[0] - v[7]
	
    b0 = a0 + a3
    b1 = a1 + a2
    b2 = a1 - a2
    b3 = a0 - a3
    b4 = -a4 - a5
    b5 = (a5 + a6) * A[3]
    b6 = a6 + a7

    c0 = b0 + b1
    c1 = b0 - b1
    c2 = (b2 + b3) * A[1]
    c3 = (b4 + b6) * A[5]

    d4 = -b4 * A[2] - c3
    d6 = b6 * A[4] - c3

    e2 = c2 + b3
    e3 = b3 - c2
    e5 = b5 + a7
    e7 = a7 - b5

    f4 = d4 + e7
    f5 = e5 + d6
    f6 = e5 - d6
    f7 = e7 - d4
    matrix = [
        S[0] * c0,
        S[1] * f5,
        S[2] * e2,
        S[3] * f7,
        S[4] * c1,
        S[5] * f4,
        S[6] * e3,
        S[7] * f6
    ]
    matrix = np.vstack(matrix)
    return matrix
def AAN_INVFDCT(v):
    #vector = np.transpose(vector)
    C = [math.cos(math.pi / 16 * i) for i in range(8)]
    S = [1 / (4 * val) for val in C]
    S[0] = 1 / (2 * math.sqrt(2))
    A = [None,C[4],C[2] - C[6],C[4],C[6] + C[2],C[6]]
    c0 = v[0] / S[0]
    f5 = v[1] / S[1]
    e2 = v[2] / S[2]
    f7 = v[3] / S[3]
    c1 = v[4] / S[4]
    f4 = v[5] / S[5]
    e3 = v[6] / S[6]
    f6 = v[7] / S[7]

    d4 = (f4 - f7) / 2
    d6 = (f5 - f6) / 2
    e5 = (f5 + f6) / 2
    e7 = (f4 + f7) / 2

    a7  = (e5 + e7) / 2
    b3 = (e2 + e3) / 2
    b5 = (e5 - e7) / 2
    c2 = (e2 - e3) / 2

    b0 = (c0 + c1) / 2
    b1 = (c0 - c1) / 2

    c3 = (d4 - d6) * A[5]  # Different from original
    b4 = (d4 * A[4] - c3) / (A[2] * A[5] - A[2] * A[4] - A[4] * A[5])
    b6 = (c3 - d6 * A[2]) / (A[2] * A[5] - A[2] * A[4] - A[4] * A[5])

    a6 = b6 - a7
    a5 = b5 / A[3] - a6
    a4 = -a5 - b4
    b2 = c2 / A[1] - b3

    a0 = (b0 + b3) / 2
    a1 = (b1 + b2) / 2
    a2 = (b1 - b2) / 2        
    a3 = (b0 - b3) / 2         
    imatrix = [
        (a0 + a7) / 2,
        (a1 + a6) / 2,
        (a2 + a5) / 2,
        (a3 + a4) / 2,
        (a3 - a4) / 2,
        (a2 - a5) / 2,
        (a1 - a6) / 2,
        (a0 - a7) / 2]
    imatrix = np.vstack(imatrix)
    return imatrix
def true_FDCT(matrix):
    temp_matrix = AAN_FDCT(matrix)
    temp_matrix = np.transpose(temp_matrix)
    temp2_matrix = AAN_FDCT(temp_matrix)
    return temp2_matrix
def true_INVFDCT(matrix):
    temp_matrix = AAN_INVFDCT(matrix)
    temp_matrix = np.transpose(temp_matrix)
    temp2_matrix = AAN_INVFDCT(temp_matrix)
    return temp2_matrix
'''
img4 = 255*np.ones((8,8))
print(FDCT3(img4))
aa = true_FDCT(img4)
print(aa)
bb = true_INVFDCT(aa)
print(bb)
'''
def PSNR(new, old):
    sum = 0
    for i in range(32):
        for j in range(32):
            for k in range(8):
                for l in range(8):
                    old_element = old[i][j][0][k,l]
                    new_element = new[i][j][k][0,l]
                    diff = (new_element - old_element)**2
                    sum += diff
                    #print(i, j , k, l)
    #print(sum)
    MSE = sum/(256*256)
    #print(MSE)
    PSNR = 20*math.log10(255/math.sqrt(MSE))
    
    return PSNR


def NoiseChannel(inp_array, ErrorRate):  #(要產生錯誤的陣列, 錯誤率[百分比%])
    inp_array = list(inp_array)
    for i in range(len(inp_array)):
        dice = random.uniform(0, 100)
        if dice <= ErrorRate:
            if inp_array[i] == '1':
                inp_array[i] = '0'
            else:
                inp_array[i] = '1'
    inp_array = ''.join(inp_array)
    return inp_array

