from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import base64, os.path
from table_UI import xml_table
from logForm import logForm
from readXML import ReadXML
from database import dataConnection
from xml_check import xml_check
from document import DocumentForm
from testcase import TestCase
from loading import Loading

dt_conn = dataConnection()
table = xml_table()
xml_ck = xml_check()

# Setup color
color_orange = QtGui.QColor("#FFD36E")
color_red = QtGui.QColor("#FF0303")



class MainUI():
    def __init__(self):
        self.xml_path = dt_conn.get_path()
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

       
       
        




        self.TAB1 = QtWidgets.QTabWidget()
        # self.TAB1.setFixedHeight(70)
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
        # self.tbXML1.setHidden(True)
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

        # FOOTER 
        # GB1
        GB1 = QtWidgets.QGroupBox()
        self.btnDocumnet = QtWidgets.QPushButton("Mô tả:")
        self.btnDocumnet.clicked.connect(self.click_Document)
        self.btnTestCase = QtWidgets.QPushButton("Testcase:")
        self.btnTestCase.clicked.connect(self.click_Testcase)
        GB1_l = QtWidgets.QHBoxLayout(GB1)
        GB1_l.addWidget(self.btnDocumnet)
        GB1_l.addWidget(self.btnTestCase)

        GB2 = QtWidgets.QGroupBox()
        self.rbAll = QtWidgets.QRadioButton("All")
        self.rbAll.setChecked(True)
        self.rbAll.clicked.connect(self.click_radio)
        self.rbxml1 = QtWidgets.QRadioButton("Full XML1")
        self.rbxml1.clicked.connect(self.click_radio)
        self.rbnotxml1 = QtWidgets.QRadioButton("Hide XML1")
        self.rbnotxml1.clicked.connect(self.click_radio)
        GB2_l = QtWidgets.QHBoxLayout(GB2)
        GB2_l.addWidget(self.rbAll)
        GB2_l.addWidget(self.rbxml1)
        GB2_l.addWidget(self.rbnotxml1)

        GB3 = QtWidgets.QGroupBox()

        self.btnChooseFile = QtWidgets.QPushButton("Chọn File")
        self.btnChooseFile.clicked.connect(self.choose_file)
        self.btnLoad = QtWidgets.QPushButton("Xem")
        self.btnLoad.setShortcut("Ctrl+R")
        self.btnLoad.clicked.connect(self.init_table)
        GB3_l = QtWidgets.QHBoxLayout(GB3)
        GB3_l.addWidget(self.btnChooseFile)
        GB3_l.addWidget(self.btnLoad)

        self.btnxml_check = QtWidgets.QPushButton('Kiểm tra')
        self.btnxml_check.clicked.connect(self.click_btnCheck)
        self.btnShowLog = QtWidgets.QPushButton("Show Log")
        self.btnShowLog.clicked.connect(self.showLog)

        self.list_log = QtWidgets.QListWidget()

        vbox1 = QtWidgets.QVBoxLayout()
        vbox1.addWidget(self.TAB1)
        vbox1.addWidget(self.TAB2)
   

        footer_l = QtWidgets.QHBoxLayout()
        footer_l.addWidget(GB1)
        footer_l.addStretch(1)
        footer_l.addWidget(GB2)
       
        footer_l.addWidget(GB3)


        hbox2 = QtWidgets.QHBoxLayout()
        hbox2.addLayout(vbox1)
        
        main_l.addLayout(hbox2)
        main_l.addLayout(footer_l)
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
        self.loadingDialog = QtWidgets.QDialog()
        self.loading = Loading()
        self.loading.setup_ui(self.loadingDialog)
        self.loadingDialog.show()



        # dialog = QtWidgets.QFileDialog()
        # dialog.setWindowTitle('Chọn file XML')
        # dialog.setNameFilter('XML files (*.xml)')
        # dialog.setDirectory(QtCore.QDir.currentPath())
        # dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        # if dialog.exec_() == QtWidgets.QDialog.Accepted:
        #     self.xml_path = str(dialog.selectedFiles()[0])
        #     self.edtPath.setText(self.xml_path)
        #     dt_conn.save_path(self.xml_path)
        #     self.load_xmlfile()
        # else:
        #     return None
        
    def click_radio(self):
        isra1 = self.rbAll.isChecked()
        isra2 = self.rbxml1.isChecked()
        isra3 = self.rbnotxml1.isChecked()
        if (isra1):
            self.TAB1.setHidden(False)
            self.TAB2.setHidden(False)
        elif (isra2):
            self.TAB1.setHidden(False)
            self.TAB2.setHidden(True)
        else:
            self.TAB1.setHidden(True)
            self.TAB2.setHidden(False)
        pass
    
    

    
    
    def init_table(self):
        ma_lk = None
        self.init_xml1_table()
        
        self.init_xml2_table(ma_lk)
        self.init_xml3_table(ma_lk)
        self.init_xml4_table(ma_lk)
        self.init_xml5_table(ma_lk)
    
    def click_Document(self):
        self.dcmDialog = QtWidgets.QDialog()
        self.dcm = DocumentForm()
        self.dcm.setupUI(self.dcmDialog)
        self.dcmDialog.show()

    def click_Testcase(self):
        self.tcDialog = QtWidgets.QDialog()
        self.tc = TestCase()
        self.tc.setupUI(self.tcDialog)
        self.tcDialog.show()

    
    
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
        center_col = [2,3,5,6,9,10,11,12,16,19,20,21,22,23,24,33,34,35,37]
        right_col = [25,26,27,28,29,30,31]
        notnull_col = [8,9,10,11]
        maybenull_col = []
        self.tbXML1.setRowCount(0)
        rows = dt_conn.get_xml1()
        for i, row in enumerate(rows):
            self.tbXML1.setRowCount(i + 1)
            self.tbXML1.setRowHeight(i, 9)

            ma_lk = row[1]
            ten_benh = str(row[13])
            n_ten_benh = len(ten_benh.split(";"))
            ma_benh_chinh = str(row[14])
            n_ma_benh_chinh = len(ma_benh_chinh.split(";"))
            ma_benh_khac = str(row[15])
            if (ma_benh_khac == ""):
                n_ma_benh_khac = 0
            else:
                n_ma_benh_khac = len(ma_benh_khac.split(";"))
            n_ma_benh = n_ma_benh_chinh + n_ma_benh_khac
            
            for j in range(1, len(row)):
                item = QtWidgets.QTableWidgetItem(row[j])
                if j in center_col:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                if j in right_col:
                    item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                if j in notnull_col and row[j]== "":
                    item.setBackground(color_red)
                else:
                    match j:
                        case 15:
                            if (n_ten_benh != n_ma_benh):
                                item.setBackground(color_red)
                        case 20:
                            ngayvao = int(row[19])
                            ngayra = int(row[20])
                            if (ngayvao > ngayra):
                                item.setBackground(color_red)
                        case 24:
                            ngayra = int(row[20])
                            ngayqt = int(row[24])
                            if ngayra > ngayqt:
                                item.setBackground(color_red)
                        case 25:
                            xml2_tongthuoc = dt_conn.get_tongthuoc(ma_lk)
                            tong_thuoc = float(row[25])
                            if (xml2_tongthuoc != tong_thuoc):
                                item.setBackground(color_red)
                        case 26:
                            xml3_tongvtyt = dt_conn.get_tongvtyt(ma_lk)
                            tong_vtyt = float(row[26])
                            if (xml3_tongvtyt != tong_vtyt):
                                item.setBackground(color_red)
                        case _:
                            pass
                self.tbXML1.setItem(i, j-1, item)
  
    def init_xml2_table(self, ma_lk):
        center_col = [1,2,4,6,8,12,13,17,23,26,27]
        right_col = [14,15,16,19,20,21]
        notnull_col = [9,11,25]
        maybenull_col = [3,5,6,7,8,10,23,24]
        # center_col những column sẽ căn giữa (mặc định căn trái)
        # center_col, right_col = table.init_align_colum("XML2")

        self.tbXML2.setRowCount(0)
        rows = dt_conn.get_xml2(ma_lk)
        for i, row in enumerate(rows):
            
            # gán 1 số biến hay dùng
            ma_thuoc = row[3]
            ma_nhom = row[4]
            self.tbXML2.setRowCount(i + 1)
            self.tbXML2.setRowHeight(i, 9)
            for j in range(1, len(row)):
                item = QtWidgets.QTableWidgetItem(row[j])
                if j in center_col:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                if j in right_col:
                    item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                if j in notnull_col and row[j]== "":
                    item.setBackground(color_red)
                elif j in maybenull_col and row[j]== "":
                    item.setBackground(color_orange)
                else:
                    match j:
                        case 4:
                            if (row[j] != "4"):
                                item.setBackground(color_red)
                        case 12:
                            if (row[j] != "1"):
                                item.setBackground(color_red)
                        case 13:
                            if (row[j] == "0"):
                                item.setBackground(color_red)
                            elif (row[j] != "100" and row[19] == "0.00"):
                                item.setBackground(color_red)
                        
                        case 17:
                            if ( (row[j] != "80") and (row[j] != "95") and (row[j] != "100") ):
                                item.setBackground(color_red)
                        case _:
                            pass
                
                
               
                # Check tiền
                n_tyle = int(row[13])
                n_sl = float(row[14])
                n_dongia = float(row[15])
                n_thanhtien = float(row[16])
                # Check thành tiền
                check_thanhtien = n_dongia*n_sl #Không nhân với ty_le
                if (check_thanhtien != n_thanhtien) and (j==16):
                    
                    item.setBackground(color_red)

                # Check BNTT và BHCT
                n_MH = int(row[17])
                check_BNTT = float(n_thanhtien*((100-n_tyle)/100))
                check_BNTT = float("{:.2f}".format(check_BNTT))
                check_BHTT = float(n_thanhtien*((n_tyle)/100)*(n_MH/100))
                check_BHTT = float("{:.2f}".format(check_BHTT))
                check_BNCCT = float(n_thanhtien*((n_tyle)/100)*((100-n_MH)/100))
                check_BNCCT = float("{:.2f}".format(check_BNCCT))
                n_BNTT = float(row[19])
                n_BHTT = float(row[20])
                n_BNCTT = float(row[21])
                if (check_BNTT != n_BNTT) and (j==19):
                    item.setBackground(color_red)
                if (check_BHTT != n_BHTT) and (j==20):
                    print(check_BHTT, n_BHTT)
                    item.setBackground(color_red)
                if (check_BNCCT != n_BNCTT) and (j==21):
                    print(check_BNCCT, n_BNCTT)
                    item.setBackground(color_red)

                self.tbXML2.setItem(i, j-1, item)
    
    
    
    def init_xml3_table(self, ma_lk):
        
        # center_col những column sẽ căn giữa (mặc định căn trái)
        center_col = [1,2,5,9,10,14,17,29]
        right_col = [11,12,15,16,19,20,21]
        notnull_col = [9,11,26]
        maybenull_col = [10,23,25]
        self.tbXML3.setRowCount(0)
        self.tbXML3.verticalHeader()
        rows = dt_conn.get_xml3(ma_lk)
        for i, row in enumerate(rows):
            self.tbXML3.setRowCount(i + 1)
            self.tbXML3.setRowHeight(i, 9)
            ma_nhom = row[5]
            for j in range(1, len(row)):
                item = QtWidgets.QTableWidgetItem(row[j])
                if j in center_col:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                if j in right_col:
                    item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                if j in notnull_col and row[j]== "":
                    item.setBackground(color_red)
                elif j in maybenull_col and row[j]== "":
                    item.setBackground(color_orange)
                else:
                    match j:
                        case 3|8:
                            if (ma_nhom != "10" and ma_nhom == ""):
                                item.setBackground(color_orange)
                        case 4|7|13:
                            if (ma_nhom == "10" and row[j] == ""):
                                item.setBackground(color_orange)
                        case 10:
                            if (row[j] != "1"):
                                item.setBackground(color_red)
                        case 24:
                            if(ma_nhom == "14" or ma_nhom == "15" or ma_nhom == "16"):
                                if (row[j] == ""):
                                    item.setBackground(color_orange)

                       
                                
                        case _:
                            pass
                    

               
                self.tbXML3.setItem(i, j-1, item)

    def init_xml4_table(self, ma_lk):
        # center_col những column sẽ căn giữa (mặc định căn trái)
        center_col = [2,4,6,8,12]
        self.tbXML4.setRowCount(0)
        rows = dt_conn.get_xml4(ma_lk)
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
        rows = dt_conn.get_xml5(ma_lk)
        for i, row in enumerate(rows):
            self.tbXML5.setRowCount(i + 1)
            self.tbXML5.setRowHeight(i, 9)
            for j in range(1, len(row)):
                item = QtWidgets.QTableWidgetItem(row[j])
                if j in center_col:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tbXML5.setItem(i, j-1, item)
    
    def costed_check(self):
        pass



    # CÁC FUNCTION KIỂM TRA XML

    def xml_check(self):
        self.log.clear()
        malks = dt_conn.get_malk()
        for malk in malks:
            malk_log = []
            xml_log = []
            malk_log.append(malk)
            xml1_log = xml_ck.xml1_check(malk)
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