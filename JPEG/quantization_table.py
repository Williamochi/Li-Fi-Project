import numpy as np

def quan_try(img,Q): #要改用陣列表示省掉一個迴圈
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
            new_quan[x,y]=(quan[x,y]*S+50)/100
            img[x,y] = img[x,y]/quan[x,y]
    return img


