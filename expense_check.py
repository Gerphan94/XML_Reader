from PyQt5 import QtCore, QtGui, QtWidgets

class Expense():
    def __init__(self):
        pass

    def setup_ui(self, Form):
        Form.setObjectName("form")
        Form.setWindowTitle("Chi phí Check")
        Form.setMinimumSize(1200, 670)

        lbTitle = QtWidgets.QLabel("Số dữ liệu bị lỗi: 0")
        font = QtGui.QFont()
        font.setPointSize(12)
        lbTitle.setFont(font)
        self.tb = QtWidgets.QTableWidget()
        TB_COL = ["#", "MA_LK", "MABN","HO_TEN","T_TONGCHI","T_BNTT","T_BNCTT","T_BHTT","T_TONGTHUOC","T_TONGVTYT","TONG_THUOC(XML2)","TONG_VTYT(XML3)"]
        self.tb.setColumnCount(len(TB_COL))
        for i, tag in enumerate(TB_COL):
            self.tb.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(tag))



        main_l = QtWidgets.QVBoxLayout(Form)
        
        main_l.addWidget(lbTitle)
        main_l.addWidget(self.tb)