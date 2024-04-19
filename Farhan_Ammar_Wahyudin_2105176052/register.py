# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import image_qrc, sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(377, 316)
        Form.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 351, 251))
        self.widget.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 91, 21))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../Downloads/hoyo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 40, 351, 41))
        self.widget_2.setStyleSheet("background-color:rgb(78, 164, 220)")
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(130, 10, 101, 21))
        self.label_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 181, 21))
        self.label_2.setStyleSheet("border-bottom: 1px solid;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(80, 120, 181, 21))
        self.label_3.setStyleSheet("border-bottom: 1px solid;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(80, 150, 181, 21))
        self.label_4.setStyleSheet("border-bottom: 1px solid;")
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(80, 180, 181, 16))
        self.checkBox.setObjectName("checkBox")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(50, 210, 251, 31))
        self.widget_3.setStyleSheet("background-color:rgb(78, 164, 220)")
        self.widget_3.setObjectName("widget_3")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(100, -4, 61, 41))
        self.label_6.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 351, 41))
        self.frame.setStyleSheet("image: url(:/img/img/hoyo.png)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Buat Akun"))
        self.label_2.setText(_translate("Form", "Username/email"))
        self.label_3.setText(_translate("Form", "Password"))
        self.label_4.setText(_translate("Form", "Confirm Password"))
        self.checkBox.setText(_translate("Form", "Show Password"))
        self.label_6.setText(_translate("Form", "Register"))
import image_qrc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
