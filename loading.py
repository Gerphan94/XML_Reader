from PyQt5 import QtCore, QtGui, QtWidgets
from database import dataConnection
import base64, os.path
from bs4 import BeautifulSoup



dt_conn = dataConnection()


class Loading():
    def __init__(self):
        self.xml_path = dt_conn.get_path()
        pass

    def setup_ui(self, Form):
        Form.setObjectName("Form")
        Form.setWindowTitle("Loading...")
        Form.setMinimumSize(400, 100)

        main_layout = QtWidgets.QVBoxLayout(Form)
        self.processBar = QtWidgets.QProgressBar()
        self.processBar.setMaximum(100)
        self.processBar.setFixedHeight(20)

        self.lb1 = QtWidgets.QLabel("Đường dẫn file xml: ")
        self.edtPath = QtWidgets.QLineEdit()
        self.edtPath.setReadOnly(True)
        self.edtPath.setMaximumWidth(250)
        self.edtPath.setText(self.xml_path)
        self.btnChooseFile = QtWidgets.QPushButton("Chọn File")
        self.btnChooseFile.clicked.connect(self.choose_file)
        self.processBar = QtWidgets.QProgressBar()
        self.processBar.setMaximum(100)
        self.processBar.setFixedHeight(15)

        gb1 = QtWidgets.QGroupBox()
        gb1_l = QtWidgets.QHBoxLayout(gb1)
        
        gb1_l.addWidget(self.edtPath)
        gb1_l.addWidget(self.btnChooseFile)
        main_layout.addWidget(self.lb1)
        hbox1 = QtWidgets.QHBoxLayout()
        hbox1.addWidget(self.edtPath)
        hbox1.addWidget(self.btnChooseFile)


        main_layout.addLayout(hbox1)
        main_layout.addWidget(self.processBar)


    def choose_file(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setWindowTitle('Chọn file XML')
        dialog.setNameFilter('XML files (*.xml)')
        dialog.setDirectory(QtCore.QDir.currentPath())
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.xml_path = str(dialog.selectedFiles()[0])
            self.edtPath.setText(self.xml_path)
            dt_conn.save_path(self.xml_path)
            self.load_xmlfile()
        else:
            return None
        

    def load_xmlfile(self):
        if not(os.path.exists(self.xml_path)):
            return
        if (self.xml_path == ''):
            return
        try:
            with open(self.xml_path, 'r') as f:
                data = f.read()
        except Exception as e:
            print(e)
            return
        self.xml_content = BeautifulSoup(data, "xml")
        # Xóa hết các dữ liệu cũ
        dt_conn.delete_xml1_table()
        dt_conn.delete_xml2_table()
        dt_conn.delete_xml3_table()
        dt_conn.delete_xml4_table()
        dt_conn.delete_xml5_table()
        # Tìm tất cả tag
        file_hoso_list = self.xml_content.find_all('FILEHOSO')
        max_hs = len(file_hoso_list)
        step = 95/max_hs
        for i_step, file in enumerate(file_hoso_list):
            loai_hs = file.find('LOAIHOSO')
            nd_hs = file.find('NOIDUNGFILE')
            match loai_hs.text:
                case 'XML1':
                    dt_conn.insert_xml1_table(nd_hs.text)
                case 'XML2':
                    dt_conn.insert_xml2_table(nd_hs.text)
                case 'XML3':
                    dt_conn.insert_xml3_table(nd_hs.text)
                case 'XML4':
                    dt_conn.insert_xml4_table(nd_hs.text)
                case 'XML5':
                    dt_conn.insert_xml5_table(nd_hs.text)
            process_value = round(i_step*step)

            self.processBar.setValue(process_value)
        # self.init_table()
        self.processBar.setValue(100)
