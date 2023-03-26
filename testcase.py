from PyQt5 import QtCore, QtGui, QtWidgets
from database import dataConnection


dt_conn = dataConnection()

class TestCase():
    def __init__(self):
        
        ...

    def setupUI(self, Form):
        
        Form.setObjectName("logform")
        Form.setWindowTitle("Log")
        Form.setMinimumSize(1200, 670)
        # self.edtCase = QtWidgets.QLineEdit()
        # self.btnAddCase = QtWidgets.QPushButton("Add")
        lbTitle = QtWidgets.QLabel("Các case XML test")
        self.tb = QtWidgets.QTableWidget()
        self.tb.setColumnCount(3)
        self.header = self.tb.horizontalHeader()  
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tb.setHorizontalHeaderLabels(("XML","Case","Expect"))
        self.tb.setColumnWidth(0, 70)
        self.tb.setColumnWidth(1, 400)
        main_l = QtWidgets.QVBoxLayout(Form)
        
        main_l.addWidget(lbTitle)
        main_l.addWidget(self.tb)
        self.init_tb()

    def init_tb(self):
        self.tb.clearContents()
        rows = dt_conn.get_testcase()
        for i, row in enumerate(rows):
            case = row[1]
            expect = row[2]
            xml = row[3]
            xml_item = QtWidgets.QTableWidgetItem(str(xml))
            xml_item.setTextAlignment(QtCore.Qt.AlignCenter)
            case_item = QtWidgets.QTableWidgetItem(str(case))
            expect_item = QtWidgets.QTableWidgetItem(str(expect))
            
            self.tb.setRowCount(i+1)
            self.tb.setRowHeight(i, 9)
            self.tb.setItem(i, 0, xml_item)
            self.tb.setItem(i, 1, case_item)
            self.tb.setItem(i, 2, expect_item)
            
   




    

