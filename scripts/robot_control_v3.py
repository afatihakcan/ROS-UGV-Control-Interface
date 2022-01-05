#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot_control_v3.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 as cv
import time



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
#        MainWindow.resize(699, 792)
        MainWindow.resize(699, 283)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(699, 283))
        MainWindow.setMaximumSize(QtCore.QSize(699, 792))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_cam = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cam.setGeometry(QtCore.QRect(80, 180, 161, 41))
        self.pushButton_cam.setObjectName("pushButton_cam")
        self.frame = QtWidgets.QLabel(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 270, 640, 480))
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setText("")
#        self.frame.setPixmap(QtGui.QPixmap("../../../../İndirilenler/640x480-black-solid-color-background.jpg"))
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 261, 121))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_speedometer = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_speedometer.setFont(font)
        self.label_speedometer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speedometer.setObjectName("label_speedometer")
        self.verticalLayout.addWidget(self.label_speedometer)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_linear = QtWidgets.QLabel(self.widget)
        self.label_linear.setAlignment(QtCore.Qt.AlignCenter)
        self.label_linear.setObjectName("label_linear")
        self.horizontalLayout.addWidget(self.label_linear)
        self.label_angular = QtWidgets.QLabel(self.widget)
        self.label_angular.setAlignment(QtCore.Qt.AlignCenter)
        self.label_angular.setObjectName("label_angular")
        self.horizontalLayout.addWidget(self.label_angular)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lcd_linear = QtWidgets.QLCDNumber(self.widget)
        self.lcd_linear.setObjectName("lcd_linear")
        self.horizontalLayout_2.addWidget(self.lcd_linear)
        self.lcd_angular = QtWidgets.QLCDNumber(self.widget)
        self.lcd_angular.setObjectName("lcd_angular")
        self.horizontalLayout_2.addWidget(self.lcd_angular)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(370, 20, 296, 204))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_control = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_control.setFont(font)
        self.label_control.setAlignment(QtCore.Qt.AlignCenter)
        self.label_control.setObjectName("label_control")
        self.verticalLayout_5.addWidget(self.label_control)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_go = QtWidgets.QPushButton(self.widget1)
        self.pushButton_go.setObjectName("pushButton_go")
        self.gridLayout.addWidget(self.pushButton_go, 0, 1, 1, 1)
        self.pushButton_left = QtWidgets.QPushButton(self.widget1)
        self.pushButton_left.setObjectName("pushButton_left")
        self.gridLayout.addWidget(self.pushButton_left, 1, 0, 1, 1)
        self.pushButton_stop = QtWidgets.QPushButton(self.widget1)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout.addWidget(self.pushButton_stop, 1, 1, 1, 1)
        self.pushButton_right = QtWidgets.QPushButton(self.widget1)
        self.pushButton_right.setObjectName("pushButton_right")
        self.gridLayout.addWidget(self.pushButton_right, 1, 2, 1, 1)
        self.pushButton_back = QtWidgets.QPushButton(self.widget1)
        self.pushButton_back.setObjectName("pushButton_back")
        self.gridLayout.addWidget(self.pushButton_back, 2, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_slideLin = QtWidgets.QLabel(self.widget1)
        self.label_slideLin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slideLin.setObjectName("label_slideLin")
        self.horizontalLayout_3.addWidget(self.label_slideLin)
        self.label_slideAng = QtWidgets.QLabel(self.widget1)
        self.label_slideAng.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slideAng.setObjectName("label_slideAng")
        self.horizontalLayout_3.addWidget(self.label_slideAng)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalSlider_linear = QtWidgets.QSlider(self.widget1)
        self.horizontalSlider_linear.setMinimum(5)
        self.horizontalSlider_linear.setMaximum(10)
        self.horizontalSlider_linear.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_linear.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_linear.setTickInterval(1)
        self.horizontalSlider_linear.setObjectName("horizontalSlider_linear")
        self.horizontalLayout_4.addWidget(self.horizontalSlider_linear)
        self.horizontalSlider_angular = QtWidgets.QSlider(self.widget1)
        self.horizontalSlider_angular.setMinimum(5)
        self.horizontalSlider_angular.setMaximum(10)
        self.horizontalSlider_angular.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_angular.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_angular.setTickInterval(1)
        self.horizontalSlider_angular.setObjectName("horizontalSlider_angular")
        self.horizontalLayout_4.addWidget(self.horizontalSlider_angular)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_lin = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_lin.setObjectName("lineEdit_lin")
        self.horizontalLayout_5.addWidget(self.lineEdit_lin)
        self.lineEdit_ang = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_ang.setObjectName("lineEdit_ang")
        self.horizontalLayout_5.addWidget(self.lineEdit_ang)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robot Control Interface v3"))
        self.pushButton_cam.setText(_translate("MainWindow", "Open Camera"))
        self.label_speedometer.setText(_translate("MainWindow", "Speedometer"))
        self.label_linear.setText(_translate("MainWindow", "Linear X"))
        self.label_angular.setText(_translate("MainWindow", "Angular Z"))
        self.label_control.setText(_translate("MainWindow", "Manual Control"))
        self.pushButton_go.setText(_translate("MainWindow", "Go"))
        self.pushButton_left.setText(_translate("MainWindow", "Left"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.pushButton_right.setText(_translate("MainWindow", "Right"))
        self.pushButton_back.setText(_translate("MainWindow", "Back"))
        self.label_slideLin.setText(_translate("MainWindow", "Linear"))
        self.label_slideAng.setText(_translate("MainWindow", "Angular"))
        
        rospy.init_node("gui_control_v3")
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 10)
        self.vel = Twist()
        rospy.Subscriber("/cmd_vel", Twist, self.velCallback)
        rospy.Subscriber("/camera/rgb/image_raw", Image, self.camCallback)
        self.bridge = CvBridge()
        
        self.pushButton_stop.clicked.connect(self.robotStop)
        self.pushButton_go.clicked.connect(self.goForward)
        self.pushButton_back.clicked.connect(self.goBack)
        self.pushButton_left.clicked.connect(self.goLeft)
        self.pushButton_right.clicked.connect(self.goRight)
        self.pushButton_cam.clicked.connect(lambda: self.cam_decide(MainWindow))
        
        self.cam_first = True
        self.frame.hide()
        
        self.vel_lin = self.horizontalSlider_linear.value() / 10
        self.vel_ang = self.horizontalSlider_angular.value() / 10
        self.lineEdit_lin.setText(str(self.vel_lin))
        self.lineEdit_ang.setText(str(self.vel_ang))

        self.horizontalSlider_linear.valueChanged.connect(self.sliderLin)
        self.horizontalSlider_angular.valueChanged.connect(self.sliderAng)
        
        self.last_command = None


    def minimize(self, MainWindow):
#        _translate = QtCore.QCoreApplication.translate
#        self.frame.deleteLater()
        self.frame.close()
        MainWindow.resize(699, 283)
#        MainWindow.setWindowTitle(_translate("MainWindow", "closed")) #debug
        self.pushButton_cam.setText("Open Camera")
 
    def maximize(self, MainWindow):
#        _translate = QtCore.QCoreApplication.translate
        MainWindow.resize(699, 792)
        self.frame.show()
#        self.frame = QtWidgets.QLabel(self.centralwidget)
#        self.frame.setGeometry(QtCore.QRect(30, 270, 640, 480))
#        self.frame.setMinimumSize(QtCore.QSize(0, 0))
#        self.frame.setText("")    
        self.pushButton_cam.setText("Close Camera")
    

    def cam_decide(self, MainWindow):
        if self.cam_first == True:
            self.cam_first = False
            self.maximize(MainWindow)
            
        else:
            self.setupUi(MainWindow)
            self.cam_first = True
            self.minimize(MainWindow)
            
    
    def convert_cv_qt(self, img):
#    """Convert from an opencv image to QPixmap"""
        rgb_image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)


    def camCallback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, "bgr8") #rgb8 last
#        self.img = QImage(self.img, self.img.shape[1], self.img.shape[0], self.img.strides[0], QImage.Format_RGB888)
        qt_img = self.convert_cv_qt(img)
        
#        if not self.cam_first == True:
#            self.frame.setPixmap(QtGui.QPixmap.fromImage(self.img))
#            self.frame.setPixmap(qt_img)
        self.frame.setPixmap(qt_img)
        if not self.cam_first == True:
            self.frame.show()
        else:
            self.frame.hide()
        time.sleep(0.001)

    def velCallback(self, msg):
        self.lcd_linear.setProperty("value", msg.linear.x)
        self.lcd_angular.setProperty("value", msg.angular.z)
        time.sleep(0.001)


    def sliderLin(self):
        self.vel_lin = self.horizontalSlider_linear.value() / 10
        self.lineEdit_lin.setText(str(self.vel_lin))
        if not self.last_command == None :
            call_func = getattr(self, self.last_command)
            call_func()

    def sliderAng(self):
        self.vel_ang = self.horizontalSlider_angular.value() / 10
        self.lineEdit_ang.setText(str(self.vel_ang))
        if not self.last_command == None :
            call_func = getattr(self, self.last_command)
            call_func()

        
    def robotStop(self):
        self.vel.linear.x = 0.0
        self.vel.angular.z = 0.0
        self.pub.publish(self.vel)
        self.last_command = None
#        self.show_vel()

    def goForward(self):
        self.vel.linear.x = self.vel_lin
        self.vel.angular.z = 0.0
        self.pub.publish(self.vel)
        self.last_command = "goForward"
#        self.show_vel()

    def goBack(self):
        self.vel.linear.x = -self.vel_lin
        self.vel.angular.z = 0.0
        self.pub.publish(self.vel)
        self.last_command = "goBack"
#        self.show_vel()

    def goLeft(self):
        self.vel.linear.x = 0.0
        self.vel.angular.z = self.vel_ang
        self.pub.publish(self.vel)
        self.last_command = "goLeft"
#        self.show_vel()

    def goRight(self):
        self.vel.linear.x = 0.0
        self.vel.angular.z = -self.vel_ang
        self.pub.publish(self.vel)
        self.last_command = "goRight"
#        self.show_vel()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
