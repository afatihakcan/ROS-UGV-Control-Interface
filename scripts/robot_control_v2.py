#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot_control_v2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from geometry_msgs.msg import Twist
import roslaunch

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 320)
        MainWindow.setMinimumSize(QtCore.QSize(540, 320))
        MainWindow.setMaximumSize(QtCore.QSize(540, 320))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_linear = QtWidgets.QLabel(self.centralwidget)
        self.label_linear.setObjectName("label_linear")
        self.gridLayout.addWidget(self.label_linear, 0, 0, 1, 1)
        self.label_angular = QtWidgets.QLabel(self.centralwidget)
        self.label_angular.setObjectName("label_angular")
        self.gridLayout.addWidget(self.label_angular, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcd_linear = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_linear.setProperty("value", 0.0)
        self.lcd_linear.setObjectName("lcd_linear")
        self.horizontalLayout.addWidget(self.lcd_linear)
        self.lcd_angular = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_angular.setProperty("value", 0.0)
        self.lcd_angular.setObjectName("lcd_angular")
        self.horizontalLayout.addWidget(self.lcd_angular)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.label_speedometer = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_speedometer.setFont(font)
        self.label_speedometer.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_speedometer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speedometer.setObjectName("label_speedometer")
        self.gridLayout_2.addWidget(self.label_speedometer, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_left = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_left.setObjectName("pushButton_left")
        self.gridLayout_3.addWidget(self.pushButton_left, 3, 0, 1, 1)
        self.pushButton_right = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_right.setObjectName("pushButton_right")
        self.gridLayout_3.addWidget(self.pushButton_right, 3, 2, 1, 1)
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout_3.addWidget(self.pushButton_stop, 3, 1, 1, 1)
        self.label_control = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_control.setFont(font)
        self.label_control.setObjectName("label_control")
        self.gridLayout_3.addWidget(self.label_control, 0, 1, 1, 1)
        self.pushButton_go = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_go.setObjectName("pushButton_go")
        self.gridLayout_3.addWidget(self.pushButton_go, 2, 1, 1, 1)
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setObjectName("pushButton_back")
        self.gridLayout_3.addWidget(self.pushButton_back, 4, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_slideLin = QtWidgets.QLabel(self.centralwidget)
        self.label_slideLin.setObjectName("label_slideLin")
        self.gridLayout_5.addWidget(self.label_slideLin, 0, 0, 1, 1)
        self.horizontalSlider_linear = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_linear.setMinimum(5)
        self.horizontalSlider_linear.setMaximum(10)
        self.horizontalSlider_linear.setSingleStep(1)
        self.horizontalSlider_linear.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_linear.setObjectName("horizontalSlider_linear")
        self.gridLayout_5.addWidget(self.horizontalSlider_linear, 1, 0, 1, 1)
        self.lineEdit_lin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lin.setReadOnly(True)
        self.lineEdit_lin.setObjectName("lineEdit_lin")
        self.gridLayout_5.addWidget(self.lineEdit_lin, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_slideAng = QtWidgets.QLabel(self.centralwidget)
        self.label_slideAng.setObjectName("label_slideAng")
        self.gridLayout_6.addWidget(self.label_slideAng, 0, 0, 1, 1)
        self.horizontalSlider_angular = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_angular.setMinimum(5)
        self.horizontalSlider_angular.setMaximum(10)
        self.horizontalSlider_angular.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_angular.setObjectName("horizontalSlider_angular")
        self.gridLayout_6.addWidget(self.horizontalSlider_angular, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_6)
        self.lineEdit_ang = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ang.setReadOnly(True)
        self.lineEdit_ang.setObjectName("lineEdit_ang")
        self.verticalLayout_3.addWidget(self.lineEdit_ang)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout_8.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robot Control Interface v2"))
        self.label_linear.setText(_translate("MainWindow", "Linear X"))
        self.label_angular.setText(_translate("MainWindow", "Angular Z"))
        self.label_speedometer.setText(_translate("MainWindow", "              Speedometer            "))
        self.pushButton_left.setText(_translate("MainWindow", "Left"))
        self.pushButton_right.setText(_translate("MainWindow", "Right"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.label_control.setText(_translate("MainWindow", "Manuel Control"))
        self.pushButton_go.setText(_translate("MainWindow", "Go"))
        self.pushButton_back.setText(_translate("MainWindow", "Back"))
        self.label_slideLin.setText(_translate("MainWindow", "             Linear"))
        self.label_slideAng.setText(_translate("MainWindow", "           Angular"))
        self.pushButton.setText(_translate("MainWindow", "Open Camera"))
        
        rospy.init_node("gui_control_v2")
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 10)
        self.vel = Twist()
        rospy.Subscriber("/cmd_vel", Twist, self.velCallback)
        
        self.pushButton_stop.clicked.connect(self.robotStop)
        self.pushButton_go.clicked.connect(self.goForward)
        self.pushButton_back.clicked.connect(self.goBack)
        self.pushButton_left.clicked.connect(self.goLeft)
        self.pushButton_right.clicked.connect(self.goRight)
        self.pushButton.clicked.connect(self.cam_decide)
        
        self.cam_first = True
        self.cam_package = 'simple_apps'
        self.cam_exec = 'camera.py'
        self.cam_node = roslaunch.core.Node(self.cam_package, self.cam_exec)
        self.cam_launch = roslaunch.scriptapi.ROSLaunch()
        

        self.horizontalSlider_linear.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_linear.setTickInterval(1)
        self.horizontalSlider_angular.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_angular.setTickInterval(1)

        self.vel_lin = self.horizontalSlider_linear.value() / 10
        self.vel_ang = self.horizontalSlider_angular.value() / 10
        self.lineEdit_lin.setText(str(self.vel_lin))
        self.lineEdit_ang.setText(str(self.vel_ang))

        self.horizontalSlider_linear.valueChanged.connect(self.sliderLin)
        self.horizontalSlider_angular.valueChanged.connect(self.sliderAng)

        
        self.last_command = None


    def velCallback(self, msg):
        self.lcd_linear.setProperty("value", msg.linear.x)
        self.lcd_angular.setProperty("value", msg.angular.z)


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
        
        
    def cam_decide(self):
        if self.cam_first == True:
            self.cam_first = False
            self.pushButton.setText("Close Camera")
            #os.system("rosrun simple_apps camera.py")
            #self.node_pid = os.spawnv(P_NOWAIT, "rosrun", ["simple_apps", "camera.py"])
            self.cam_launch.start()
            self.cam_process = self.cam_launch.launch(self.cam_node)

        else:
            self.cam_first = True
            self.pushButton.setText("Open Camera")             
            #os.system("rosnode kill /robot_cam")
            #os.kill(self.node_pid, signal.SIGINT)
            self.cam_process.stop()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
