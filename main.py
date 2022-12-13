from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import base64
from table_UI import *
from readXML import ReadXML
from database import dataConnection

data_conn = dataConnection()

class MainUI():
    def __init__(self):
        self.xml_path = data_conn.get_path()

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
        self.btnRun.clicked.connect(self.click_btnRun)

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
        xmltb_1= xml_table()
        xmltb_1.setupUi_XML1(self.tbXML1)
        self.tbXML1.clicked.connect(self.click_xml1_table)
        xml1_l = QtWidgets.QVBoxLayout(self.tab_xml1)
        xml1_l.addWidget(self.tbXML1)

        # TAG 2
        self.tbXML2 = QtWidgets.QTableWidget()
        xmltb_2= xml_table()
        xmltb_2.setupUi_XML2(self.tbXML2)
        xml2_l = QtWidgets.QVBoxLayout(self.tab_xml2)
        xml2_l.addWidget(self.tbXML2)

        # TAB 3
        self.tbXML3 = QtWidgets.QTableWidget()
        xmltb_3= xml_table()
        xmltb_3.setupUi_XML3(self.tbXML3)
        xml3_l = QtWidgets.QVBoxLayout(self.tab_xml3)
        xml3_l.addWidget(self.tbXML3)
        # XML 4
        self.tbXML4 = QtWidgets.QTableWidget()
        xmltb_4= xml_table()
        xmltb_4.setupUi_XML4(self.tbXML4)
        xml4_l = QtWidgets.QVBoxLayout(self.tab_xml4)
        xml4_l.addWidget(self.tbXML4)

        # XML 5
        self.tbXML5 = QtWidgets.QTableWidget()
        xmltb_5= xml_table()
        xmltb_5.setupUi_XML5(self.tbXML5)
        xml5_l = QtWidgets.QVBoxLayout(self.tab_xml5)
        xml5_l.addWidget(self.tbXML5)

        GB1 = QtWidgets.QGroupBox()

        self.btnxml1_check = QtWidgets.QPushButton('XML1')
        self.btnxml1_check.clicked.connect(self.xml1_check)
        self.btnxml2_check = QtWidgets.QPushButton('XML2')
        self.btnxml3_check = QtWidgets.QPushButton('XML3')
        self.btnxml4_check = QtWidgets.QPushButton('XML4')
        self.btnxml5_check = QtWidgets.QPushButton('XML5')
        gb1_l = QtWidgets.QHBoxLayout(GB1)
        gb1_l.addStretch(1)
        gb1_l.addWidget(self.btnxml1_check)
        gb1_l.addWidget(self.btnxml2_check)
        gb1_l.addWidget(self.btnxml3_check)
        gb1_l.addWidget(self.btnxml4_check)
        gb1_l.addWidget(self.btnxml5_check)

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
        main_l.addLayout(hbox2)
        MainWindow.setCentralWidget(CWget)
        
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
        if (self.xml_path == ''):
            return
        read_xml = ReadXML(self.xml_path)
        read_xml.read_file()
        read_xml.init_xml_table()
        data_conn.get_xml1()
        self.init_xml1_table()

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
        self.tbXML1.setRowCount(0)
        rows = data_conn.get_xml1()
        for i, row in enumerate(rows):
            self.tbXML1.setRowCount(i + 1)
            self.tbXML1.setRowHeight(i, 9)
            for j in range(1, len(row)):
                item = QtWidgets.QTableWidgetItem(row[j])
                if j in center_col:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                if ( j < 3):
                    pass
                elif (j <= 7):
                    item.setBackground(QtGui.QColor("#F9E0AE"))
                elif (j <= 12):
                    item.setBackground(QtGui.QColor("#CAE4DB"))
                self.tbXML1.setItem(i, j-1, item)
  
    def init_xml2_table(self, ma_lk):
        # center_col những column sẽ căn giữa (mặc định căn trái)
        center_col = [2,4,6,8,12]
        self.tbXML2.setRowCount(0)
        rows = data_conn.get_xml2(ma_lk)
        for i, row in enumerate(rows):
            self.tbXML2.setRowCount(i + 1)
            self.tbXML2.setRowHeight(i, 9)
            for j in range(1, len(row)):
                item = QtWidgets.QTableWidgetItem(row[j])
                if j in center_col:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tbXML2.setItem(i, j-1, item)
    
    def init_xml3_table(self, ma_lk):
        # center_col những column sẽ căn giữa (mặc định căn trái)
        center_col = [1,2,3,4,5,6]
        self.tbXML3.setRowCount(0)
        rows = data_conn.get_xml3(ma_lk)
        for i, row in enumerate(rows):
            self.tbXML3.setRowCount(i + 1)
            self.tbXML3.setRowHeight(i, 9)
            for j in range(1, len(row)):
                item = QtWidgets.QTableWidgetItem(row[j])
                if j in center_col:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
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
  
    
    def xml1_check(self):
        # Kiểm tra ngày vào - ngày ra
        ngay_vao = self.xml1.find('NGAY_VAO')
        ngay_ra = self.xml1.find('NGAY_VAO')
        if (len(ngay_vao.text) != 12 ):
            print('thẻ <NGAY_VAO> không hợp lệ ')
        if (len(ngay_ra.text) != 12 ):
            print('thẻ <NGAY_RA> không hợp lệ ')
        
        pass


    def tag_name_check(self, xml_number):
        match xml_number:
            case 'XML1':
                standard_tag_name = [""]
            case 'XML2':
                standard_tag_name = [""]
            case 'XML3':
                standard_tag_name = ['MA_LK','STT','MA_DICH_VU','MA_VAT_TU','MA_NHOM','GOI_VTYT','TEN_VAT_TU','TEN_DICH_VU','DON_VI_TINH','PHAM_VI','SO_LUONG','DON_GIA','TT_THAU','TYLE_TT','THANH_TIEN','T_TRANTT','MUC_HUONG','T_NGUONKHAC','T_BNTT','T_BHTT','T_BNCCT','T_NGOAIDS','MA_KHOA','MA_GIUONG','MA_BAC_SI','MA_BENH','NGAY_YL','NGAY_KQ','MA_PTTT']

            case 'XML4':
                standard_tag_name = [""]
            case 'XML5':
                standard_tag_name = [""]

    


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