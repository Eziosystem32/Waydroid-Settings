

from PyQt5 import QtCore, QtGui, QtWidgets
from Bin.Code_wd import *
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(693, 419)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 681, 311))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 120, 80, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(StartButton.on_button_clicked)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 120, 80, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(StopButton.on_button_clicked)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 120, 80, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(RestartButton.on_button_clicked)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(480, 120, 80, 24))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(FreezeButton.on_button_clicked)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(40, 50, 311, 16))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab, "")
        self.Properties = QtWidgets.QWidget()
        self.Properties.setObjectName("Properties")
        self.checkBox_2 = QtWidgets.QCheckBox(self.Properties)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 50, 491, 22))
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_2 = QtWidgets.QLabel(self.Properties)
        self.label_2.setGeometry(QtCore.QRect(30, 210, 161, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.Properties)
        self.lineEdit.setGeometry(QtCore.QRect(190, 180, 41, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox_5 = QtWidgets.QCheckBox(self.Properties)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 140, 341, 22))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox = QtWidgets.QCheckBox(self.Properties)
        self.checkBox.setGeometry(QtCore.QRect(30, 20, 341, 22))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_4 = QtWidgets.QCheckBox(self.Properties)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 110, 591, 22))
        self.checkBox_4.setObjectName("checkBox_4")
        self.label = QtWidgets.QLabel(self.Properties)
        self.label.setGeometry(QtCore.QRect(30, 180, 161, 16))
        self.label.setObjectName("label")
        self.checkBox_3 = QtWidgets.QCheckBox(self.Properties)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 80, 601, 22))
        self.checkBox_3.setObjectName("checkBox_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Properties)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 210, 41, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tabWidget.addTab(self.Properties, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 350, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 350, 80, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 340, 241, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QtCore.QRect(30, 340, 241, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 693, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Define a timer to periodically check the status
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.check_status)
        self.timer.start(2000)  # Check every 2 seconds

    def check_status(self):
        # Command to check the status
        command = ["waydroid", "status"]
        result = subprocess.run(command, capture_output=True, text=True)
        first_line = result.stdout.split('\n')[0]
        # Update the label text based on the status
        if "RUNNING" in first_line:
            self.label_4.setText("Waydroid status: Running")
        else:
            self.label_4.setText("Waydroid status: Stopped")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Waydroid properties"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p>properties</p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Start"))
        self.pushButton_4.setText(_translate("MainWindow", "Stop"))
        self.pushButton_5.setText(_translate("MainWindow", "Restart"))
        self.pushButton_6.setText(_translate("MainWindow", "Freeze"))
        self.label_3.setText(_translate("MainWindow", "This is where you manage your waydroid container"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Manage"))
        self.checkBox_2.setText(_translate("MainWindow", "Workaround to display the cursor in multi-windows mode on certain compositors."))
        self.label_2.setText(_translate("MainWindow", "Adjust the width padding."))
        self.checkBox_5.setText(_translate("MainWindow", "Permit Android direct access to hot-plugged devices."))
        self.checkBox.setText(_translate("MainWindow", "Enable window integration with the desktop"))
        self.checkBox_4.setText(_translate("MainWindow", "Allow the Waydroid container to sleep after the display timeout when no apps are active."))
        self.label.setText(_translate("MainWindow", "Adjust the height padding."))
        self.checkBox_3.setText(_translate("MainWindow", "Swap the color space from RGBA to BGRA (effective only with specific patched versions of Mutter)."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Properties), _translate("MainWindow", "Properties"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.label_4.setText(_translate("MainWindow", "Waydroid status:"))
        # Command to check the status
        command = ["waydroid", "status"]
        result = subprocess.run(command, capture_output=True, text=True)
        first_line = result.stdout.split('\n')[0]
        # Update the label text based on the status
        if "RUNNING" in first_line:
            running = True
            self.label_4.setText("Waydroid status: Running")
        else:
            running = False
            self.label_4.setText("Waydroid status: Stopped")
            # Sleep for a while before checking again
            # Define a timer to periodically check the status
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.check_status)
            self.timer.start(2000)  # Check every 2 seconds

if __name__ == "__main__":
    
    import sys
    import threading
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    status_thread = threading.Thread(target=ui.check_status)
    status_thread.start()
    status_thread = threading.Thread(target=ui.check_status)
    ui.check_status()
    MainWindow.show()
    sys.exit(app.exec_())
  
