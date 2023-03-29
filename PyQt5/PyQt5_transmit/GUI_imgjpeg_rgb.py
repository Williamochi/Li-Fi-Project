
import Def, cv2, Def2
import numpy as np
import copy
import os

class Img_JPEG():
    def __init__(self, FilePath, OutputFilename, Q_value):
        self.OutputFilename = OutputFilename
        self.directory = 'graph/'
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        img_input = cv2.imread(FilePath[0],3)
        img_shape = img_input.shape # 照片大小
        self.rows = img_shape[0]
        self.cols = img_shape[1]
        self.h = int(img_shape[0]/8) #高 切割數量
        self.w = int(img_shape[1]/8) #寬 切割數量
        self.channels = 3
        img_input=img_input.reshape(self.rows, self.cols, self.channels)
        self.JPEG_init(img_input, Q_value)
    
    def JPEG_init(self, img0, Q_value):
        Y = 0.2990*img0[:,:,2] + 0.578*img0[:,:,1] + 0.1140*img0[:,:,0]
        Cb = -0.1687*img0[:,:,2] -0.3313*img0[:,:,1]+0.5*img0[:,:,0] + 128*np.ones((self.rows, self.cols))
        Cr = 0.5*img0[:,:,2] - 0.4187*img0[:,:,1] - 0.0813*img0[:,:,0] + 128*np.ones((self.rows, self.cols))
        self.ImgAfterZigzag = [[[[0 for k1 in range(self.w)] for k2 in range(self.w)] for k3 in range(self.w)] for k4 in range(self.w)]
        temp00 = [[[[0 for k1 in range(self.w)] for k2 in range(self.w)] for k3 in range(self.w)] for k4 in range(self.w)]
        for color in range(3):
            
            if color == 0:
                img0 = Y 
            if color == 1:
                img0 = Cb
            if color == 2:
                img0 = Cr
            img1 = np.split(img0, self.h, axis=1)
            img3 = [[[[0 for k1 in range(self.w)] for k2 in range(self.w)] for k3 in range(self.w)] for k4 in range(self.w)]
           
            for i in range(self.w):
                img2 = np.vsplit(img1[i], self.w)
                for j in range(self.w):
                    img3[i][j] = img2[j]
            for i in range(self.h):
                for j in range(self.w):
                    img4 = np.asmatrix(img3[i][j])
                    img4 = img4.astype(np.float32)
                    img4 -= 128*np.ones((8,8))
                    img4 = Def.true_FDCT(img4)
                    temp00[i][j] = img4
            if color == 0:
                DCT_Y = copy.deepcopy(temp00)
                DCT_Ytemp = Def.combine_code(DCT_Y, self.h, self.w, self.rows, self.cols, 1)
                DCT_Ytemp = DCT_Ytemp.tolist()
            if color == 1:
                DCT_Cb = copy.deepcopy(temp00)
                DCT_Cbtemp = Def.combine_code(DCT_Cb, self.h, self.w, self.rows, self.cols, 1)
                DCT_Cbtemp = DCT_Cbtemp.tolist()
            if color == 2:
                DCT_Cr = copy.deepcopy(temp00)
                DCT_Crtemp = Def.combine_code(DCT_Cr, self.h, self.w, self.rows, self.cols, 1)
                DCT_Crtemp = DCT_Crtemp.tolist()
                
        self.ImgAfterDCT = [DCT_Y, DCT_Cb, DCT_Cr]
        self.JPEG_remain(Q_value)
        self.temp_DCT = Def.YCbCr_to_RGB(DCT_Ytemp, DCT_Cbtemp, DCT_Crtemp, self.h, self.w)
        self.JPEG_DCT()
    
    def JPEG_DCT(self):
        cv2.imwrite(os.path.join(self.directory,self.OutputFilename + "DCT.jpg") , self.temp_DCT)
    
    def JPEG_transmit(self, Q_value):
        temp002 = copy.deepcopy(self.ImgAfterDCT)
        imgsum = ""
        for color in range(3):
            if color == 0:
                img3 = temp002[0] 
            if color == 1:
                img3 = temp002[1]
            if color == 2:
                img3 = temp002[2]
            temp02 = 0
            for i in range(self.h):
                for j in range(self.w):
                    img3[i][j] = Def.quan_try(img3[i][j], Q_value)
                    img3[i][j] = np.round_(img3[i][j],0)
                    img3[i][j] = Def.zigzag(img3[i][j])
                    img3[i][j] = Def.RLE_AC(img3[i][j])
                    temp = img3[i][j][0] - temp02
                    temp02 = img3[i][j][0]
                    img3[i][j][0] = temp

                    img3[i][j] = Def2.Huff_Y(img3[i][j])

                img3[i] = ''.join(img3[i])
            img3 = ''.join(img3)
            imgsum += img3
        height = self.h*8
        width = self.w*8
        bin_height = Def2.bin_huff(height)
        bin_width = Def2.bin_huff(width)
        Qtemp = Def2.bin_huff(Q_value)
        imgsum = bin_height + bin_width + Qtemp + imgsum

        joined_imgsum = Def.divide_string(imgsum)
        return joined_imgsum


    def JPEG_remain(self, Q_value):
        temp03 = copy.deepcopy(self.ImgAfterDCT)
        for color in range(3):
            if color == 0:
                temp_remain = temp03[0] 
            if color == 1:
                temp_remain = temp03[1]
            if color == 2:
                temp_remain = temp03[2]
            for i in range(self.h):
                for j in range(self.w):
                    temp_remain[i][j] = Def.quan_try(temp_remain[i][j], Q_value)
                    temp_remain[i][j] = np.round_(temp_remain[i][j],0)
                    img5 = temp_remain[i][j]
                    img5 = Def.iquan_try(img5, Q_value)
                    img4 = np.asmatrix(img5)
                    img4 = img4.astype(np.float32)
                    img4 = Def.iFDCT3(img4)
                    img4 += 128*np.ones((8,8))
                    temp_remain[i][j] = img4
                    temp_remain[i][j] = np.clip(temp_remain[i][j],0,255)

            if color == 0:
                Y = temp_remain
                Y = Def.combine_code(Y, self.h, self.w, self.rows, self.cols, 1)
                Y = Y.tolist()
            elif color == 1:
                Cb = temp_remain
                Cb = Def.combine_code(Cb, self.h, self.w, self.rows, self.cols, 1)
                Cb = Cb.tolist()
            else :
                Cr = temp_remain
                Cr = Def.combine_code(Cr, self.h, self.w, self.rows, self.cols, 1)
                Cr = Cr.tolist()
        temp04 = Def.YCbCr_to_RGB(Y, Cb, Cr, self.h, self.w)
        cv2.imwrite(os.path.join(self.directory,self.OutputFilename + "R1.jpg"),temp04)
