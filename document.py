from PyQt5 import QtCore, QtGui, QtWidgets
from database import dataConnection

dt_conn = dataConnection()

class DocumentForm():
    def __init__(self) -> None:
        
        ...

    def setupUI(self, Form):
        
        Form.setObjectName("logform")
        Form.setWindowTitle("Log")
        Form.setMinimumSize(1200, 670)


        lb = QtWidgets.QLabel("Mô tả các bảng XML")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(20)
        lb.setFont(font)
        self.cbbXML = QtWidgets.QComboBox()
        self.cbbXML.addItems(["XML1","XML2","XML3","XML4","XML5"])
        self.cbbXML.setMinimumWidth(300)
        self.cbbXML.currentIndexChanged.connect(self.init_table)
        self.tb = QtWidgets.QTableWidget()
        
        self.tb.setColumnCount(4)
        self.tb.setColumnWidth(2,400)

        self.tb.setHorizontalHeaderLabels(("Tag","Mô tả","Mô tả thêm","Bắt buộc"))
        self.header = self.tb.horizontalHeader()  
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        main_l = QtWidgets.QVBoxLayout(Form)
        main_l.addWidget(lb)
        main_l.addWidget(self.cbbXML)
        main_l.addWidget(self.tb)
        self.init_table()

    def init_table(self):
        self.tb.clearContents()
        xml_id = self.cbbXML.currentIndex() + 1
        rows = dt_conn.get_tag(xml_id)
        for i, row in enumerate(rows):
            tag_name = row[2]
            tag_des = row[3]
            tag_des_plus = row[4]
            tag_name_item = QtWidgets.QTableWidgetItem(str(tag_name))
            tag_des_item = QtWidgets.QTableWidgetItem(str(tag_des))
            tag_des_plus_item = QtWidgets.QTableWidgetItem(str(tag_des_plus))
            self.tb.setRowCount(i+1)
            self.tb.setRowHeight(i+1, 9)
            #self.tb.setItem(i, 0, stt_item)
            self.tb.setItem(i, 0, tag_name_item)
            self.tb.setItem(i, 1, tag_des_item)
            self.tb.setItem(i, 2, tag_des_plus_item)
            

        ...
