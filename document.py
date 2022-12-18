from PyQt5 import QtCore, QtGui, QtWidgets

class DocumentForm():
    def __init__(self) -> None:
        
        ...

    def setupUI(self, Form):
        
        Form.setObjectName("logform")
        Form.setWindowTitle("Log")
        Form.setMinimumSize(800, 670)


        lb = QtWidgets.QLabel("Mô tả các bảng XML")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(20)
        lb.setFont(font)
        self.cbbXML = QtWidgets.QComboBox()
        self.cbbXML.addItems(["XML1","XML2","XML3","XML4","XML5"])
        self.cbbXML.setMinimumWidth(300)
        self.tb = QtWidgets.QTableWidget()
        self.tb.setColumnCount(4)



        main_l = QtWidgets.QVBoxLayout(Form)
        main_l.addWidget(lb)
        main_l.addWidget(self.cbbXML)
        main_l.addWidget(self.tb)