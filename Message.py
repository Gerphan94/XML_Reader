from PyQt5 import QtCore, QtGui, QtWidgets
from Main_Setup import init_icon

class MsgForm(object):
    def __init__(self, Dialog):
        self.Dialog = Dialog
        self.setupUi()
        pass
    
    def setupUi(self):
        self.Dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.Dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        # self.Dialog.setMinimumSize(220, 130)
        # self.Dialog.setMaximumHeight(130)

        Background = QtWidgets.QFrame()
        Background.setObjectName("Background")
        main_l = QtWidgets.QVBoxLayout(self.Dialog)
        main_l.setContentsMargins(0,0,0,0)
        main_l.addWidget(Background)
        Background.setStyleSheet("""
                    #Background {
                        border-radius: 15px;
                    }
                    """)
        Background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Background.setFrameShadow(QtWidgets.QFrame.Raised)


        self.msgText = QtWidgets.QLabel()
        self.msgText.setStyleSheet("font-size: 10pt")
        self.img = QtWidgets.QLabel()
        self.img.setScaledContents(True)
        self.img.setMaximumSize(35, 35)
        self.dialog_button = QtWidgets.QDialogButtonBox()
        self.dialog_button.setStyleSheet("width: 50px; height: 25px;")
        self.dialog_button.setCenterButtons(True)

        hbox = QtWidgets.QHBoxLayout()
        hbox.setSpacing(20)
        hbox.setContentsMargins(10, 10, 10, 10)
        hbox.addWidget(self.img)
        hbox.addWidget(self.msgText)

        mainlayout = QtWidgets.QVBoxLayout(Background)
        mainlayout.setSpacing(10)
        mainlayout.setContentsMargins(20, 40, 20, 20)
        #mainlayout.addStretch(1)
        mainlayout.addLayout(hbox)
        mainlayout.addWidget(self.dialog_button)
        

    def msgbox(self, title, msgtext, type):
        self.Dialog.setWindowTitle(title)
        self.msgText.setText(msgtext)
        self.img.setPixmap(QtGui.QPixmap(init_icon(type)))
        self.dialog_button.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.dialog_button.accepted.connect(self.Dialog.accept)
        self.Dialog.show()

    def msgboxSuccess(self):
        self.Dialog.setWindowTitle("Thông báo")
        self.msgText.setText("Thành công")
        self.img.setPixmap(QtGui.QPixmap(init_icon("information")))
        self.dialog_button.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.dialog_button.accepted.connect(self.Dialog.accept)
        self.Dialog.show()

    def msgboxError(self, e):
        msgtring = "%s" % e
        self.Dialog.setWindowTitle("Lỗi")
        self.msgText.setText(msgtring)
        self.img.setPixmap(QtGui.QPixmap(init_icon("error")))
        self.dialog_button.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.dialog_button.accepted.connect(self.Dialog.reject)
        self.Dialog.show()