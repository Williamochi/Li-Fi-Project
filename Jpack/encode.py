import Def
import Def2
import numpy as np
def encode(encode_img,h, w):
    img = np.transpose(encode_img) 
    img1 = np.split(img, h, axis=1) #水平切
    img3 = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
    temp02 = 0
    for i in range(w):#每一片水平的再縱切
        img2 = np.dsplit(img1[i], w)
        for j in range(w):#每一格再丟入img3
            img3[i][j] = img2[j]
    #img3 = resized_image.astype(np.float32)
    for i in range(h):
        for j in range(w):
            img4 = np.asmatrix(img3[i][j])
            img4 = img4.astype(np.float32)
            img4 -= 128*np.ones((8,8))
            #img4 = Def.FDCT3(img4)
            img4 = Def.true_FDCT(img4)

            img3[i][j] = img4
            #img3[i][j] = Def.quan(img3[i][j])
            img3[i][j] = Def.quan_try(img3[i][j], 50)
            
            img3[i][j] = np.round_(img3[i][j],0)
            img3[i][j] = Def.zigzag(img3[i][j])

            img3[i][j] = Def.RLE_AC(img3[i][j])

    ######################DPCM#####################
            temp = img3[i][j][0] - temp02
            temp02 = img3[i][j][0]
            img3[i][j][0] = temp
            #print(i,j)
            #print(img3[i][j])
    ##################Huff+combine###################
            img3[i][j] = Def2.Huff(img3[i][j])

        img3[i] = ''.join(img3[i])
    img3 = ''.join(img3)
    height = h*8
    width = w*8
    bin_height = Def2.bin_huff(height)
    bin_width = Def2.bin_huff(width)
    img3 = bin_height + bin_width + img3
    return img3
