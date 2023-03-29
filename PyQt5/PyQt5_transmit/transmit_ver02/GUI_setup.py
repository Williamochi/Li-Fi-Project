import numpy as np
import transmit_pyfirmata
import GUI_imgjpeg_rgb
import GUI_imgjpeg_gray
import os
from PIL import Image
from GUI_transmit import Ui_Transmit
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, Qt
from PyQt5.QtWidgets import  QProgressBar, QVBoxLayout, QDialog, QPushButton

class MainWindow(QtWidgets.QMainWindow):
    progress_update = pyqtSignal(int)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.GUI = Ui_Transmit()
        self.GUI.setupUi(self)
        self.GUI_setup()
        
    def GUI_setup(self):
        self.GUI.spinBox_Q.setValue(50) 
        self.spinbox_prevalue = self.GUI.spinBox_Q.value()
        self.directory = 'graph/'

        self.GUI.pushButton_confirm.clicked.connect(self.confirm_clicked) 
        self.GUI.pushButton_open.clicked.connect(self.Open_Clicked)
        self.GUI.pushButton_DCT.clicked.connect(self.Img_DCT_clicked)
        self.GUI.pushButton_transmit.clicked.connect(self.transmit_Clicked)
        self.box = QtWidgets.QMessageBox(self)
        
    def Open_Clicked(self):
        self.FilePath , self.FilterType = QtWidgets.QFileDialog.getOpenFileNames()
        OutputFilename = "Outputimg"
        try:
            temp_check = Image.open(self.FilePath[0])
            self.temp_check_mode = temp_check.mode
            if self.temp_check_mode == 'L':
                self.Img_Input = GUI_imgjpeg_gray.Img_JPEG(self.FilePath, OutputFilename, self.GUI.spinBox_Q.value())
            elif self.temp_check_mode =='RGB':
                self.Img_Input = GUI_imgjpeg_rgb.Img_JPEG(self.FilePath, OutputFilename, self.GUI.spinBox_Q.value())

            self.Img_show_L(self.FilePath[0], self.Img_Input.rows, self.Img_Input.cols)
            self.Img_Input.JPEG_remain(self.GUI.spinBox_Q.value())
        except:
            self.box.critical(self, 'Error', 'No File Selected!!')

    def Img_show_L(self,FilePath, len, wid):
        self.scene_1 = QtWidgets.QGraphicsScene()
        self.img = QtGui.QPixmap(FilePath)
        img_w = 512                         # 顯示圖片的寬度
        img_h = 512                          # 顯示圖片的高度
        self.img = self.img.scaled(img_w, img_h, QtCore.Qt.KeepAspectRatio)
        dx = int(abs((self.GUI.graphicsView_graphicL.width() - img_w))-3 / 2)        # 修正公式
        dy = int(abs((self.GUI.graphicsView_graphicL.height()  - img_h))-3 / 2)
        self.scene_1.setSceneRect(dx, dy, 512, 512)
        self.scene_1.addPixmap(self.img)

        self.GUI.graphicsView_graphicL.setScene(self.scene_1)
        self.GUI.graphicsView_graphicL.mousePressEvent = self.get_clicked_position
        self.side_CutPicture = self.cutPicture(FilePath)
        self.DCT_CutPicture = self.cutPicture(os.path.join(self.directory,self.Img_Input.OutputFilename + "DCT.jpg"))
        self.OutPut_CutPicture = self.cutPicture(os.path.join(self.directory,self.Img_Input.OutputFilename + "R1.jpg"))

    def Img_show_R(self, inpfile):
        self.scene_2 = QtWidgets.QGraphicsScene()
        self.img2 = QtGui.QPixmap(inpfile)
        img_w = 512                         # 顯示圖片的寬度
        img_h = 512                          # 顯示圖片的高度
        self.img2 = self.img2.scaled(img_w, img_h, QtCore.Qt.KeepAspectRatio)
        dx = int(abs((self.GUI.graphicsView_graphicR.width() - img_w))-3 / 2)        # 修正公式
        dy = int(abs((self.GUI.graphicsView_graphicR.height()  - img_h))-3 / 2)
        self.scene_2.setSceneRect(dx, dy, 512, 512)
        
        self.scene_2.addPixmap(self.img2)
        self.GUI.graphicsView_graphicR.setScene(self.scene_2)
        self.GUI.graphicsView_graphicR.mousePressEvent = self.get_clicked_position

    def Img_show_side(self, Filepath):
        temp = QtGui.QPixmap(Filepath).scaled(139, 139)
        self.GUI.label_side_original.setPixmap(temp)

    def Img_show_DCT(self, Filepath):
        temp = QtGui.QPixmap(Filepath).scaled(139, 139)
        self.GUI.label_side_DCT.setPixmap(temp)
    
    def Img_show_OutPut(self, Filepath):
        temp = QtGui.QPixmap(Filepath).scaled(139, 139)
        self.GUI.label_side_zigzag.setPixmap(temp)

    def Img_DCT_clicked(self):
        try:
            self.Img_Input.JPEG_DCT()
            if self.GUI.pushButton_DCT.isChecked() == True: 
                self.Img_show_R(os.path.join(self.directory,self.Img_Input.OutputFilename + "DCT.jpg")) 
            else:
                self.scene_2.clear()
        except:
            self.box.critical(self, 'Error', 'No File Selected!!')

    def confirm_clicked(self):
        try:
            if self.spinbox_prevalue != self.GUI.spinBox_Q.value():
                self.Img_Input.JPEG_remain(self.GUI.spinBox_Q.value())
                self.spinbox_prevalue = self.GUI.spinBox_Q
            if self.GUI.pushButton_DCT.isChecked() == True:
                self.GUI.pushButton_DCT.toggle()
            self.Img_show_R(os.path.join(self.directory,self.Img_Input.OutputFilename + "R1.jpg")) 
        except:
            self.box.critical(self, 'Error', 'No File Selected!!')
    
    def transmit_Clicked(self):

        progress_dialog = ProgressDialog(self)
        progress_dialog.show()

        # try:
        value_to_transmit = self.Img_Input.JPEG_transmit(self.GUI.spinBox_Q.value())
        self.SENDING, self.blink = transmit_pyfirmata.transmit_setup(value_to_transmit, self.temp_check_mode)
        self.thread_transmit = QThread()
        self.thread_transmit.run = self.trasmit_to_arduino
        self.progress_update.connect(progress_dialog.progress_bar.setValue)
        self.thread_transmit.finished.connect(progress_dialog.completeTransmission)
        self.thread_transmit.start()
        # except:
        #     self.box.critical(self, 'Error', 'No File Selected!!')
    
    def trasmit_to_arduino(self):
        i = 0
        count = 0
        print("Hello world")
        while(i < len(self.SENDING)):
            value = count*25
            print(count)
            print(i)
            self.progress_update.emit(value)
            count, i = transmit_pyfirmata.transmit(self.SENDING, self.blink, count, i)

    def cutPicture(self, FilePath):
        self.photo = QtGui.QPixmap(FilePath)
        size = min(self.photo.width(), self.photo.height())
        self.photo = self.photo.copy(0, 0, size, size)
        img_piece = [[0 for k1 in range(self.Img_Input.h)]for k2 in range(self.Img_Input.w)]
        for x in range(self.Img_Input.w):
            for y in range(self.Img_Input.h):
                pieceImage = self.photo.copy(x*8, y*8, 8, 8)
                img_piece[x][y] = pieceImage
        return img_piece

    def __update_text_clicked_position(self, x, y):
        self.GUI.label_click_pos.setText(f"Clicked position = ({x}, {y})")
        self.GUI.label_norm_pos.setText(f"Normalized position = ({self.norm_x:.3f}, {self.norm_y:.3f})")
        self.GUI.label_real_pos.setText(f"Real position = ({int(x*self.Img_Input.cols/512)}, {int(y*self.Img_Input.rows/512)})")
    
    def get_clicked_position(self, event):
        x = event.pos().x()
        y = event.pos().y() 
        self.norm_x = x/self.GUI.graphicsView_graphicL.width()
        self.norm_y = y/self.GUI.graphicsView_graphicL.height()

        print(f"(x, y) = ({x}, {y}), normalized (x, y) = ({self.norm_x}, {self.norm_y})")
        try :
            temp = self.side_CutPicture[int(x*self.Img_Input.h/512)][int(y*self.Img_Input.w/512)]
            temp_DCT = self.DCT_CutPicture[int(x*self.Img_Input.h/512)][int(y*self.Img_Input.w/512)]
            temp_OutPut = self.OutPut_CutPicture[int(x*self.Img_Input.h/512)][int(y*self.Img_Input.w/512)]
            #print(int(x*self.Img_Input.h/512), int(y*self.Img_Input.w/512))
            self.Img_show_side(temp)
            self.Img_show_DCT(temp_DCT)
            self.Img_show_OutPut(temp_OutPut)
            self.__update_text_clicked_position(x, y)
            print("success")
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

# class TransmissionThread(QThread):
#     progress_update = pyqtSignal(int)

#     def __init__(self):
#         super().__init__()
#         self.value = 0
#         self.SENDING = None
#         self.blink = None

#     def run(self):
#         i = 0
#         count = 0
#         print("Hello world")
#         while(i < len(self.SENDING)):
#             self.value = count*25
#             print(count)
#             print(i)
#             self.progress_update.emit(self.value)
#             count, i = transmit_pyfirmata.transmit(self.SENDING, self.blink, count, i)
            


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
#Form.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
#Form.setFixedSize(Form.width(),Form.height())