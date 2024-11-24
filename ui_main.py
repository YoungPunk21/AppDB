# ui_main.py

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)

        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(20, 20, 80, 20))
        self.label_name.setText("Name:")
        
        
        self.input_name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_name.setGeometry(QtCore.QRect(120, 20, 200, 30))

        
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(20, 60, 80, 20))
        self.label_email.setText("Email:")
        
        
        self.input_email = QtWidgets.QLineEdit(self.centralwidget)
        self.input_email.setGeometry(QtCore.QRect(120, 60, 200, 30))

        
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(120, 100, 200, 30))
        self.button_add.setText("Add User")
        
        
        self.table_users = QtWidgets.QTableWidget(self.centralwidget)
        self.table_users.setGeometry(QtCore.QRect(20, 150, 550, 200))
        self.table_users.setColumnCount(3)
        self.table_users.setHorizontalHeaderLabels(["ID", "Name", "Email"])

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "User Database App"))
