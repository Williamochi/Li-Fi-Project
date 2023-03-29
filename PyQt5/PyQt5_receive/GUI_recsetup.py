import numpy as np
import Def, cv2, Def2
import receive
import os
from GUI_receive import Ui_Receive
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, Qt
from PyQt5.QtWidgets import  QProgressBar, QVBoxLayout, QDialog, QPushButton

class MainWindow(QtWidgets.QMainWindow):
    progress_update = pyqtSignal(int)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.GUI = Ui_Receive()
        self.GUI.setupUi(self)
        self.GUI.pushButton_open.clicked.connect(self.open_clicked)
        self.GUI.pushButton_receive.clicked.connect(self.receive_clicked)
        self.box = QtWidgets.QMessageBox(self)
        self.directory = 'graph/'
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)


    def open_clicked(self):
        self.FilePath , self.FilterType = QtWidgets.QFileDialog.getOpenFileNames()
        try:
            temp_check = cv2.imread(self.FilePath[0])
            img_shape = temp_check.shape # 照片大小
            self.h = int(img_shape[0]/8)
            self.w = int(img_shape[1]/8) 
            self.Img_show_preview(self.FilePath[0])
        except:
            self.box.critical(self, 'Error', 'No File Selected!!')

    def receive_clicked(self):
        progress_dialog = ProgressDialog(self)
        progress_dialog.show()
        self.ser = receive.receive_setup()
        self.thread_jpeg = QThread()
        
        self.thread_jpeg.run = self.JPEG_inverse
        self.progress_update.connect(progress_dialog.progress_bar.setValue)
        self.thread_jpeg.finished.connect(progress_dialog.completeTransmission)
        self.thread_jpeg.start()

        # self.thread = TransmissionThread()

        # self.thread.ser = receive.receive_setup()
        # self.thread.start()
        # self.thread.progress_update.connect(progress_dialog.progress_bar.setValue)
        
        # self.thread.wait()
        # self.thread.finished.connect(progress_dialog.completeTransmission)
        
        # self.JPEG_inverse(self.thread.receive_word, self.thread.colormode)


    def Img_show_preview(self, Filepath):
        temp = QtGui.QPixmap(Filepath).scaled(512, 512)
        self.GUI.label_graphic.setPixmap(temp) 
        self.GUI.label_graphic.mousePressEvent = self.get_clicked_position
        self.Receive_CutPicture = self.cutPicture(Filepath)
    
    def Img_show_preview_side(self, Filepath):
        temp = QtGui.QPixmap(Filepath).scaled(256, 256)
        self.GUI.label_side_original.setPixmap(temp)
        

    def JPEG_inverse(self):
        self.counter = 0
        input_code = ''
        print ("Start receiving")          #prints the data for confirmation
        while(self.counter != 4):
            value = self.counter*25
            self.progress_update.emit(value)
            print(self.counter)
            self.receive_word, self.counter = receive.receive(self.ser, self.counter)
            input_code = input_code + self.receive_word
        print(self.counter)
        self.colormode = input_code[0:4]
        if self.colormode == '1010':
            self.colormode = 'L'
        else:
            self.colormode = 'RGB'
        input_code = input_code[4:] + '1'
        input_code = input_code.replace('131','')
        print(len(input_code))
        text_file = open("code.txt", "wt")
        n = text_file.write(input_code)
        text_file.close()  
        hihi = Def2.ibin_huff(input_code)
        img_shape = hihi[0]
        n = hihi[1]
        input_code = input_code[n:]
        if self.colormode == 'L':
            channels = 1            ###########
            self.rows = img_shape[0]
            self.cols = img_shape[1]
            self.Q_value = img_shape[2]
            self.GUI.rho.setText(f"ρ  = {self.Q_value}")
            self.h = int(self.rows/8) #高 切割數量
            self.w = int(self.cols/8) #寬 切割數量
            img3 = [[[[0 for k1 in range(self.w)] for k2 in range(self.w)] for k3 in range(self.w)] for k4 in range(self.w)]
            inp_list = [[[[0 for k1 in range(self.w)] for k2 in range(self.w)] for k3 in range(self.w)] for k4 in range(self.w)]
            temp02 = 0
                    ###################################<<invHuffman>>##################################
            img5 = Def2.InvHuff(input_code,self.h,self.w)
            o = 0
            for i in range(self.h):
                for j in range(self.w):
                    inp_list[i][j] = img5[o]
                    o+=1

            a = 0
            for i in range(self.h):
                for j in range(self.w):
                    ###################################<<invDPCM>>##################################
                    temp01 = inp_list[i][j][0] + temp02
                    inp_list[i][j][0] = temp01
                    temp02 = inp_list[i][j][0]
                    a+=1
                    ###################################<<invRLE>>##################################
                    img3[i][j] = Def.InvRLE_AC(inp_list[i][j])

                    ################################<<iZig-Zag>>#################################
                    img3[i][j] = Def.izigzag(img3[i][j])
                
                    ##############################<<IQuantization>>###############################
                    img5 = img3[i][j]
                    img5 = Def.iquan_try(img5, self.Q_value)
                    ###################################<<IDCT>>###################################
                    img4 = np.asmatrix(img5)
                    img4 = img4.astype(np.float32)
                    img4 = Def.iFDCT3(img4)
                    img4 += 128*np.ones((8,8))
                    img3[i][j] = img4
                    img3[i][j] = np.clip(img3[i][j],0,255)
            temp00 = Def.combine_picture(img3 ,self.h ,self.w ,self.rows ,self.cols ,channels)

        elif self.colormode == 'RGB':         ###########
            self.rows = img_shape[0]
            self.cols = img_shape[1]
            self.Q_value = img_shape[1]
            self.GUI.rho.setText(f"ρ  = {self.Q_value}")
            self.h = int(self.rows/8) #高 切割數量
            self.w = int(self.cols/8) #寬 切割數量
            for color in range(3):
                img3 = [[[[0 for k1 in range(self.w)] for k2 in range(self.w)] for k3 in range(self.w)] for k4 in range(self.w)]
                inp_list = [[[[0 for k1 in range(self.w)] for k2 in range(self.w)] for k3 in range(self.w)] for k4 in range(self.w)]
                temp02 = 0

                if color > 0:#CbCr
                    img5, codebook_count = Def2.InvHuff_CbCr(input_code,self.h,self.w)
                    input_code = input_code[codebook_count:]
                else:#Y
                    img5, codebook_count = Def2.InvHuff_CbCr(input_code,self.h,self.w)
                    input_code = input_code[codebook_count:]

                o = 0
                for i in range(self.h):
                    for j in range(self.w):
                        inp_list[i][j] = img5[o]
                        o+=1
                a = 0
                for i in range(self.h):
                    for j in range(self.w):
                        temp01 = inp_list[i][j][0] + temp02
                        inp_list[i][j][0] = temp01
                        temp02 = inp_list[i][j][0]
                        a+=1
                        img3[i][j] = Def.InvRLE_AC(inp_list[i][j])
                        img3[i][j] = Def.izigzag(img3[i][j])
                        img5 = img3[i][j]
                        img5 = Def.iquan_try(img5, self.Q_value)
                        img4 = np.asmatrix(img5)
                        img4 = img4.astype(np.float32)
                        img4 = Def.iFDCT3(img4)
                        img4 += 128*np.ones((8,8))
                        img3[i][j] = img4
                        img3[i][j] = np.clip(img3[i][j],0,255)
                if color == 0:
                    Y = img3
                    Y = Def.combine_code(Y, self.h, self.w, self.rows, self.cols, 1)
                    Y = Y.tolist()
                elif color == 1:
                    Cb = img3
                    Cb = Def.combine_code(Cb, self.h, self.w, self.rows, self.cols, 1)
                    Cb = Cb.tolist()
                else :
                    Cr = img3
                    Cr = Def.combine_code(Cr, self.h, self.w, self.rows, self.cols, 1)
                    Cr = Cr.tolist()

            temp00 = Def.YCbCr_to_RGB(Y, Cb, Cr, self.h, self.w)
        cv2.imwrite(os.path.join(self.directory, "receive.jpg"),temp00)
        self.Img_show_preview(os.path.join(self.directory, "receive.jpg"))


    def cutPicture(self, FilePath):
        self.photo = QtGui.QPixmap(FilePath)
        size = min(self.photo.width(), self.photo.height())
        self.photo = self.photo.copy(0, 0, size, size)
        img_piece = [[0 for k1 in range(self.h)]for k2 in range(self.w)]
        for x in range(self.w):
            for y in range(self.h):
                pieceImage = self.photo.copy(x*8, y*8, 8, 8)
                img_piece[x][y] = pieceImage
        return img_piece
    
    def __update_text_clicked_position(self, x, y):
        self.GUI.label_click_pos.setText(f"Clicked position = ({x}, {y})")
        self.GUI.label_norm_pos.setText(f"Normalized position = ({self.norm_x:.3f}, {self.norm_y:.3f})")
        self.GUI.label_real_pos.setText(f"Real position = ({int(x*self.w*8/512)}, {int(y*self.h*8/512)})")
    
    def get_clicked_position(self, event):
        x = event.pos().x()
        y = event.pos().y() 
        self.norm_x = x/self.GUI.label_graphic.width()
        self.norm_y = y/self.GUI.label_graphic.height()

        print(f"(x, y) = ({x}, {y}), normalized (x, y) = ({self.norm_x}, {self.norm_y})")
        try :
            temp = self.Receive_CutPicture[int(x*self.h/512)][int(y*self.w/512)]
            self.Img_show_preview_side(temp)
            self.__update_text_clicked_position(x, y)
        except:
            self.__update_text_clicked_position(x, y)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
            self, 'Warning', 'Do you want to save your changes before closing?',
            QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Cancel,
            QtWidgets.QMessageBox.Save)
        if reply == QtWidgets.QMessageBox.Save:
            # save file code here
            event.accept()
        elif reply == QtWidgets.QMessageBox.Discard:
            for filename in os.listdir(self.directory):
                file_path = os.path.join(self.directory, filename)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        print(f'{file_path} has been removed.')
                except OSError as e:
                    print(f'Error: {file_path} - {e.strerror}')
            event.accept()
        else:
            event.ignore()

class ProgressDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Progress')
        self.setFixedSize(300, 120)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(20, 20, 260, 25)

        self.close_button = QPushButton('Close', self)
        self.close_button.setGeometry(100, 60, 100, 30)
        self.close_button.hide()
        self.close_button.clicked.connect(self.accept)

        self.v_layout = QVBoxLayout(self)
        self.v_layout.addWidget(self.progress_bar)
        self.v_layout.addWidget(self.close_button)

        self.progress_bar.setValue(0)
        self.setModal(True)

    def completeTransmission(self):
        self.progress_bar.setValue(100)
        self.close_button.show()

    def closeEvent(self, event):
        event.ignore()
    
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

