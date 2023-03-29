import Def
import Def2
import numpy as np
import cv2

def decode(decode_img):
    hihi = Def2.ibin_huff(decode_img)
    #hihi = Def2.ibin_huff_error(decode_img)
    if hihi == "error":
        return "cantfixit"
    img_shape = hihi[0]
    n = hihi[1]
    h = int(img_shape[0]/8) #高 切割數量
    w = int(img_shape[1]/8) #寬 切割數量
    img3 = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
    inp_list = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
    temp02 = 0
            ###################################<<invHuffman>>##################################
    img5 = Def2.InvHuff(decode_img,h,w,n)
    #img5 = Def2.InvHuff_error(decode_img,h,w,n)
    if img5 == "error":
        return "cantfixit"

    o = 0
    for i in range(h):
        for j in range(w):
            inp_list[i][j] = img5[o]
            o+=1

    a = 0
    for i in range(h):
        for j in range(w):
            ###################################<<invDPCM>>##################################
            temp01 = inp_list[i][j][0] + temp02
            inp_list[i][j][0] = temp01
            temp02 = inp_list[i][j][0]
            #print(i,j)
            a+=1
            #print(a)
            #print(inp_list[i][j])
            ###################################<<invRLE>>##################################
            img3[i][j] = Def.InvRLE_AC(inp_list[i][j])

            ################################<<iZig-Zag>>#################################
            img3[i][j] = Def.izigzag(img3[i][j])
          
            ##############################<<IQuantization>>###############################
            img5 = img3[i][j]
            #img5 = Def.iquan(img5)
            img5 = Def.iquan_try(img5, 50)
            ###################################<<IDCT>>###################################
            img4 = np.asmatrix(img5)
            img4 = img4.astype(np.float32)
            #img4 = Def.iFDCT3(img4)
            img4 = Def.true_INVFDCT(img4)
            img4 += 128*np.ones((8,8))
            img3[i][j] = img4
            img3[i][j] = np.clip(img3[i][j],0,255)
            
    return img3
def combine_picture(img, h ,w ,rows, cols, channels): #組合並顯示圖片
    img_merge = [[0 for k1 in range(8)] for k2 in range(w)]
    for c in range(w):
        img_merge[c] = img[c][0]
        b = 1
        for a in range(w-1):
            img_merge[c] = np.hstack((img_merge[c],img[c][b]))
            b+=1

    img_merge1 = img_merge[0]
    e = 0
    f = 1
    for d in range(h-1):
        img_merge1 = np.vstack((img_merge1,img_merge[f]))
        e+=1 
        f+=1
    img_merge1 = np.transpose(img_merge1)
    img_merge1 = img_merge1.astype(np.uint8)
    img_merge1=img_merge1.reshape(rows, cols, channels)
    cv2.imshow('temp', img_merge1)
    #cv2.imwrite('pepper_Q=99.png', img_merge1)
    cv2.waitKey(0) 