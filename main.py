from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import base64
from table_UI import *
from readXML import ReadXML
from database import dataConnection

data_conn = dataConnection()

class MainUI():
    def __init__(self):
        self.xml = ''
        self.xml1 = ''
        self.xml2 = ''
        self.xml3 = ''
        self.xml4 = ''
        self.xml5 = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(1220, 670)
        CWget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPixelSize(12)
        CWget.setFont(font)
        main_l = QtWidgets.QVBoxLayout(CWget)

        self.lb1 = QtWidgets.QLabel("Đường dẫn file xml: ")
        self.edtPath = QtWidgets.QLineEdit()
        self.edtPath.setReadOnly(True)
        self.edtPath.setPlaceholderText("Chọn file xml")
        self.btnChooseFile = QtWidgets.QPushButton("Chọn File")
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
        self.tbXML1.clicked.connect(self.click_xml_table)
        
        
        xml1_l = QtWidgets.QVBoxLayout(self.tab_xml1)
        xml1_l.addWidget(self.tbXML1)

        # TAG 2
        self.tbXML2 = QtWidgets.QTableWidget()
        # xmltb_2= xml_table()
        # xmltb_2.setupUi_XML1(self.tbXML2)
        
        # xml2_l = QtWidgets.QVBoxLayout(self.tab_xml2)
        # xml2_l.addWidget(self.tbXML2)

        # TAB 3
        self.tbXML3 = QtWidgets.QTableWidget()
        xmltb_3= xml_table()
        xmltb_3.setupUi_XML1(self.tbXML3)
        
        xml2_l = QtWidgets.QVBoxLayout(self.tab_xml2)
        xml2_l.addWidget(self.tbXML2)


        xml3_l = QtWidgets.QVBoxLayout(self.tab_xml3)
        xml3_l.addWidget(self.tbXML3)

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
        self.read_xml()

    def click_btnRun(self):
        path = 'template.xml'
        self.read_xml = ReadXML(path)
        xml1_list = self.read_xml.init_xml1()
        self.init_xml1_table(xml1_list)

    def click_xml_table(self):
        index = self.tbXML1.selectionModel().currentIndex()
        row = index.row()
        if (row == -1):
            return
        ma_lk = index.sibling(row, 0).data()
        self.read_xml.init_xml2345(ma_lk)
        

    def read_xml(self):
        read_xml = ReadXML('template.xml')
        read_xml.init_xml1()
      

    def init_xml1_table(self, data_list):
        self.tbXML1.setRowCount(0)
        for i, data in enumerate(data_list):
            nd_decode = base64.b64decode(data)
            nd_xml = BeautifulSoup(nd_decode, "xml")
            nd_xml = nd_xml.find('TONG_HOP')
            for j, tag in enumerate(nd_xml.find_all()):
                # item_tag_name = QtWidgets.QTableWidgetItem(str(tag.name))
                item_tag_value = QtWidgets.QTableWidgetItem(str(tag.text))
                if ( j < 2):
                    pass
                elif (j <= 6):
                    item_tag_value.setBackground(QtGui.QColor("#F9E0AE"))
                elif (j <= 11):
                    item_tag_value.setBackground(QtGui.QColor("#CAE4DB"))
                self.tbXML1.setRowCount(i + 1)
                self.tbXML1.setRowHeight(i, 9)
                self.tbXML1.setItem(i, j, item_tag_value)
            
            
    def init_xml2_table(self, data):
        self.tbXML2.setRowCount(0)
        for i, tag in enumerate(data.find_all()):
            item_tag_name = QtWidgets.QTableWidgetItem(str(tag.name))
            item_tag_value = QtWidgets.QTableWidgetItem(str(tag.text))
            self.tbXML2.setRowCount(i+1)
            self.tbXML2.setRowHeight(i, 9)
            self.tbXML2.setItem(i, 0, item_tag_name)
            self.tbXML2.setItem(i, 1, item_tag_value)
    
    # def init_xml3_tree(self, data):
    #     self.tree_xml3.clear()
    #     dvkt_list = data.find_all('CHI_TIET_DVKT')
    #     for i, dvkt in enumerate(dvkt_list, start=1):
    #         item = QtWidgets.QTreeWidgetItem()
    #         font = QtGui.QFont()
    #         font.setBold(True)
    #         item.setBackground(0, QtGui.QColor('azure'))
    #         item.setBackground(1, QtGui.QColor('azure'))
    #         item.setBackground(2, QtGui.QColor('azure'))
    #         item.setText(0, f"STT: {str(i)}")
    #         item.setText(1, '')
    #         item.setText(2, '')
    #         item.setFont(0, font)
    #         for tag in dvkt:
    #             if (tag.name != None):
    #                 child = QtWidgets.QTreeWidgetItem(item)
    #                 child.setText(0,'')
    #                 child.setText(1, tag.name)
    #                 child.setText(2, tag.text)
    #                 item.addChild(child)
    #         self.tree_xml3.addTopLevelItem(item)
        # self.tree_xml3.expandToDepth(1)
    
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