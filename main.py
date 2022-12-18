from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import base64
from table_UI import xml_table
from logForm import logForm
from readXML import ReadXML
from database import dataConnection
from xml_check import xml_check
from document import DocumentForm

data_conn = dataConnection()
table = xml_table()
xml_ck = xml_check()


class MainUI():
    def __init__(self):
        self.xml_path = data_conn.get_path()
        self.log = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("XML Check")
        MainWindow.setMinimumSize(1220, 670)
        CWget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPixelSize(12)
        CWget.setFont(font)
        main_l = QtWidgets.QVBoxLayout(CWget)

        self.lb1 = QtWidgets.QLabel("Đường dẫn file xml: ")
        self.edtPath = QtWidgets.QLineEdit()
        self.edtPath.setReadOnly(True)
        self.edtPath.setText(self.xml_path)
        self.btnChooseFile = QtWidgets.QPushButton("Chọn File")
        self.btnChooseFile.clicked.connect(self.choose_file)
        self.btnRun = QtWidgets.QPushButton("Khởi tạo")
        self.btnRun.setShortcut("Ctrl+R")
        self.btnRun.clicked.connect(self.click_btnRun)
        self.processBar = QtWidgets.QProgressBar()
        self.processBar.setMaximum(100)
        self.processBar.setFixedHeight(15)

        hbox1 = QtWidgets.QHBoxLayout()
        hbox1.addWidget(self.lb1)
        hbox1.addWidget(self.edtPath)
        hbox1.addWidget(self.btnChooseFile)
        hbox1.addWidget(self.btnRun)
        self.TAB1 = QtWidgets.QTabWidget()
        self.TAB2 = QtWidgets.QTabWidget()
        self.tab_xml1 = QtWidgets.QWidget()
        self.tab_xml2 = QtWidgets.QWidget()
        self.tab_xml3 = QtWidgets.QWidget()
        self.tab_xml4 = QtWidgets.QWidget()
        self.tab_xml5 = QtWidgets.QWidget()
        self.TAB1.addTab(self.tab_xml1, "XML1")

        self.TAB2.addTab(self.tab_xml2, "XML2")
        self.TAB2.addTab(self.tab_xml3, "XML3")
        self.TAB2.addTab(self.tab_xml4, "XML4")
        self.TAB2.addTab(self.tab_xml5, "XML5")
        self.tree = QtWidgets.QTreeWidget()

        # TAG XML1
        self.tbXML1 = QtWidgets.QTableWidget()
        table.setupUi_XML1(self.tbXML1)
        self.tbXML1.clicked.connect(self.click_xml1_table)
        xml1_l = QtWidgets.QVBoxLayout(self.tab_xml1)
        xml1_l.addWidget(self.tbXML1)

        # TAG 2
        self.tbXML2 = QtWidgets.QTableWidget()
        table.setupUi_XML2(self.tbXML2)
        xml2_l = QtWidgets.QVBoxLayout(self.tab_xml2)
        xml2_l.addWidget(self.tbXML2)

        # TAB 3
        self.tbXML3 = QtWidgets.QTableWidget()
        table.setupUi_XML3(self.tbXML3)
        xml3_l = QtWidgets.QVBoxLayout(self.tab_xml3)
        xml3_l.addWidget(self.tbXML3)
        # XML 4
        self.tbXML4 = QtWidgets.QTableWidget()
        table.setupUi_XML4(self.tbXML4)
        xml4_l = QtWidgets.QVBoxLayout(self.tab_xml4)
        xml4_l.addWidget(self.tbXML4)

        # XML 5
        self.tbXML5 = QtWidgets.QTableWidget()
        table.setupUi_XML5(self.tbXML5)
        xml5_l = QtWidgets.QVBoxLayout(self.tab_xml5)
        xml5_l.addWidget(self.tbXML5)

        GB1 = QtWidgets.QGroupBox()
        self.btnDocumnet = QtWidgets.QPushButton("Mô tả:")
        self.btnDocumnet.clicked.connect(self.click_Document)
        self.btnxml_check = QtWidgets.QPushButton('Kiểm tra')
        self.btnxml_check.clicked.connect(self.click_btnCheck)
        self.btnShowLog = QtWidgets.QPushButton("Show Log")
        self.btnShowLog.clicked.connect(self.showLog)

        gb1_l = QtWidgets.QHBoxLayout(GB1)
        gb1_l.addWidget(self.btnDocumnet)
        gb1_l.addStretch(1)
        gb1_l.addWidget(self.btnxml_check)
        gb1_l.addWidget(self.btnShowLog)

        self.list_log = QtWidgets.QListWidget()

        vbox1 = QtWidgets.QVBoxLayout()
        vbox1.addWidget(self.TAB1)
        vbox1.addWidget(self.TAB2)
        vbox1.addWidget(GB1)

        hbox2 = QtWidgets.QHBoxLayout()
        hbox2.addLayout(vbox1)
        #hbox2.addWidget(self.list_log)
        # C586C0
        main_l.addLayout(hbox1)
        main_l.addWidget(self.processBar)
        main_l.addLayout(hbox2)
        MainWindow.setCentralWidget(CWget)
    
    def setupLogDialog(self, dialog):
        #dialog = QtWidgets.QDialog()
        dialog.setFixedSize(800,600)
        self.edtLog = QtWidgets.QPlainTextEdit()
        self.edtLog.setPlainText(self.log)
        self.edtLog.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edtLog.setFont(font)
        dialog_l = QtWidgets.QVBoxLayout(dialog)
        dialog_l.addWidget(self.edtLog)

    def choose_file(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setWindowTitle('Chọn file XML')
        dialog.setNameFilter('XML files (*.xml)')
        dialog.setDirectory(QtCore.QDir.currentPath())
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.xml_path = str(dialog.selectedFiles()[0])
            self.edtPath.setText(self.xml_path)
            data_conn.save_path(self.xml_path)
        else:
            return None

    def click_btnRun(self):
        self.processBar.setValue(10)
        if (self.xml_path == ''):
            return
        read_xml = ReadXML(self.xml_path)
        read_xml.read_file()
        read_xml.init_xml_table()
        data_conn.get_xml1()
        self.processBar.setValue(10)
        ma_lk = None
        self.init_xml1_table()
        self.processBar.setValue(20)
        self.init_xml2_table(ma_lk)
        self.processBar.setValue(40)
        self.init_xml3_table(ma_lk)
        self.processBar.setValue(60)
        self.init_xml4_table(ma_lk)
        self.processBar.setValue(80)
        self.init_xml5_table(ma_lk)
        self.processBar.setValue(100)
    
    def click_Document(self):
        self.dcmDialog = QtWidgets.QDialog()
        self.dcm = DocumentForm()
        self.dcm.setupUI(self.dcmDialog)
        self.dcmDialog.show()
    
    def click_btnCheck(self):
        self.xml_check()
        self.showLog()
    
    def showLog(self):
        self.logDialog = QtWidgets.QDialog()
        self.logForm = logForm(self.log)
        self.logForm.setupUi(self.logDialog)
        self.logDialog.show()

    def click_xml1_table(self):
        index = self.tbXML1.selectionModel().currentIndex()
        row = index.row()
        if (row == -1):
            return
        ma_lk = index.sibling(row, 0).data()
        self.init_xml2_table(ma_lk)
        self.init_xml3_table(ma_lk)
        self.init_xml4_table(ma_lk)
        self.init_xml5_table(ma_lk)
        
    def init_xml1_table(self):
        # center_col những column sẽ căn giữa (mặc định căn trái)
        center_col = [2,3,5,6,9,10,11,12]
        right_col = [24,25,26,27,28,29,30,31]
        self.tbXML1.setRowCount(0)
        rows = data_conn.get_xml1()
        for i, row in enumerate(rows):
            self.tbXML1.setRowCount(i + 1)
            self.tbXML1.setRowHeight(i, 9)
            for j in range(1, len(row)):
                item = QtWidgets.QTableWidgetItem(row[j])
                if j in center_col:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                if j in right_col:
                    item.setTextAlignment(QtCore.Qt.AlignRight)
                if ( j < 3):
                    pass
                elif (j <= 7):
                    item.setBackground(QtGui.QColor("#F9E0AE"))
                elif (j <= 12):
                    item.setBackground(QtGui.QColor("#CAE4DB"))
                self.tbXML1.setItem(i, j-1, item)
  
    def init_xml2_table(self, ma_lk):
        # center_col những column sẽ căn giữa (mặc định căn trái)
        center_col, right_col = table.init_align_colum("XML2")
        self.tbXML2.setRowCount(0)
        rows = data_conn.get_xml2(ma_lk)
        for i, row in enumerate(rows):
            self.tbXML2.setRowCount(i + 1)
            self.tbXML2.setRowHeight(i, 9)
            for j in range(1, len(row)):
                item = QtWidgets.QTableWidgetItem(row[j])
                if j in center_col:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                if j in right_col:
                    item.setTextAlignment(QtCore.Qt.AlignRight)
                self.tbXML2.setItem(i, j-1, item)
    
    def init_xml3_table(self, ma_lk):
        
        # center_col những column sẽ căn giữa (mặc định căn trái)
        center_col, right_col = table.init_align_colum("XML3")
        self.tbXML3.setRowCount(0)
        self.tbXML3.verticalHeader()
        rows = data_conn.get_xml3(ma_lk)
        for i, row in enumerate(rows):
            self.tbXML3.setRowCount(i + 1)
            self.tbXML3.setRowHeight(i, 9)
            for j in range(1, len(row)):
                item = QtWidgets.QTableWidgetItem(row[j])
                if j in center_col:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                if j in right_col:
                    item.setTextAlignment(QtCore.Qt.AlignRight)
                self.tbXML3.setItem(i, j-1, item)

    def init_xml4_table(self, ma_lk):
        # center_col những column sẽ căn giữa (mặc định căn trái)
        center_col = [2,4,6,8,12]
        self.tbXML4.setRowCount(0)
        rows = data_conn.get_xml4(ma_lk)
        for i, row in enumerate(rows):
            self.tbXML4.setRowCount(i + 1)
            self.tbXML4.setRowHeight(i, 9)
            for j in range(1, len(row)):
                item = QtWidgets.QTableWidgetItem(row[j])
                if j in center_col:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tbXML4.setItem(i, j-1, item)
    
    def init_xml5_table(self, ma_lk):
        # center_col những column sẽ căn giữa (mặc định căn trái)
        center_col = [1,2]
        self.tbXML5.setRowCount(0)
        rows = data_conn.get_xml5(ma_lk)
        for i, row in enumerate(rows):
            self.tbXML5.setRowCount(i + 1)
            self.tbXML5.setRowHeight(i, 9)
            for j in range(1, len(row)):
                item = QtWidgets.QTableWidgetItem(row[j])
                if j in center_col:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tbXML5.setItem(i, j-1, item)
    

    # CÁC FUNCTION KIỂM TRA XML

    def xml_check(self):
        self.log.clear()
        malks = data_conn.get_malk()
        for malk in malks:
            malk_log = []
            xml_log = []
            malk_log.append(malk)
            xml1_log = self.xml1_check(malk)
            xml2_log = xml_ck.xml2_check(malk)
            xml3_log = xml_ck.xml3_check(malk)
            xml4_log = self.xml4_check(malk)
            xml5_log = self.xml5_check(malk)
            xml_log.append(xml1_log)
            xml_log.append(xml2_log)
            xml_log.append(xml3_log)
            xml_log.append(xml4_log)
            xml_log.append(xml5_log)
            malk_log.append(xml_log)
            self.log.append(malk_log)
        

    def xml1_check(self, malk):
        _log = []
        return _log
    
    def xml2_check(self,malk):
        _log = []
        return _log

    def xml3_check(self, malk):
        ...
    
    def xml4_check(self, malk):
        _log = []
        return _log
    
    def xml5_check(self, malk):
        _log = []
        return _log
                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_ui = MainUI()
    with open('style.css', 'r') as f:
            css = f.read()
    app.setStyleSheet(css)
    main_ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())