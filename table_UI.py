from PyQt5 import QtCore, QtGui, QtWidgets


class xml_table():
    def __init__(self):
        pass


    def setupUi_XML1(self, table):
        #self.tbXML1 = QtWidgets.QTableWidget()
        tags= ["MA_LK","STT","MA_BN","HO_TEN","NGAY_SINH","GIOI_TINH","DIA_CHI","MA_THE","MA_DKBD","GT_THE_TU","GT_THE_DEN","MIEN_CUNG_CT","TEN_BENH","MA_BENH","MA_BENHKHAC","MA_LYDO_VVIEN","MA_NOI_CHUYEN","MA_TAI_NAN","NGAY_VAO","NGAY_RA","SO_NGAY_DTRI","KET_QUA_DTRI","TINH_TRANG_RV","NGAY_TTOAN","T_THUOC","T_VTYT","T_TONGCHI","T_BNTT","T_BNCCT","T_BHTT","T_NGUONKHAC","T_NGOAIDS","NAM_QT","THANG_QT","MA_LOAI_KCB","MA_KHOA","MA_CSKCB","MA_KHUVUC","MA_PTTT_QT","CAN_NANG"]
        #table = QtWidgets.QTableWidget()
        table.setColumnCount(len(tags))
        table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        table.setSelectionMode(QtWidgets.QTableView.SingleSelection)
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i,tag in enumerate(tags):
            table.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(tag))
            match tag:
                case "STT":
                    table.setColumnWidth(i, 50)
                case "GIOI_TINH":
                    table.setColumnWidth(i, 90)
                case "HO_TEN":
                    table.setColumnWidth(i, 150)
                case "TEN_BENH" |"DIA_CHI":
                    table.setColumnWidth(i, 500)

    def setupUI_XML2(self, table):
        tags= ['MA_LK','STT','MA_THUOC','MA_NHOM','TEN_THUOC','DON_VI_TINH','HAM_LUONG','DUONG_DUNG','LIEU_DUNG','SO_DANG_KY','TT_THAU','PHAM_VI','TYLE_TT','SO_LUONG','DON_GIA','THANH_TIEN','MUC_HUONG','T_NGUONKHAC','T_BNTT','T_BHTT','T_BNCCT','T_NGOAIDS','MA_KHOA','MA_BAC_SI','MA_BENH','NGAY_YL','MA_PTTT']
        #table = QtWidgets.QTableWidget()
        table.setColumnCount(len(tags))
        table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        table.setSelectionMode(QtWidgets.QTableView.SingleSelection)
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i,tag in enumerate(tags):
            table.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(tag))
            match tag:
                case "STT":
                    table.setColumnWidth(i, 50)
                case "GIOI_TINH":
                    table.setColumnWidth(i, 80)
                case "HO_TEN":
                    table.setColumnWidth(i, 150)
                case "TEN_BENH" |"DIA_CHI":
                    table.setColumnWidth(i, 500)
    
    def setupUI_XML3(self, table):
        tags = ['MA_LK','STT','MA_DICH_VU','MA_VAT_TU','MA_NHOM','GOI_VTYT','TEN_VAT_TU','TEN_DICH_VU','DON_VI_TINH','PHAM_VI','SO_LUONG','DON_GIA','TT_THAU','TYLE_TT','THANH_TIEN','T_TRANTT','MUC_HUONG','T_NGUONKHAC','T_BNTT','T_BHTT','T_BNCCT','T_NGOAIDS','MA_KHOA','MA_GIUONG','MA_BAC_SI','MA_BENH','NGAY_YL','NGAY_KQ','MA_PTTT']

        #table = QtWidgets.QTableWidget()
        table.setColumnCount(len(tags))
        table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        table.setSelectionMode(QtWidgets.QTableView.SingleSelection)
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i,tag in enumerate(tags):
            table.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(tag))
            match tag:
                case "STT":
                    table.setColumnWidth(i, 50)
                case "GIOI_TINH":
                    table.setColumnWidth(i, 80)
                case "HO_TEN":
                    table.setColumnWidth(i, 150)
                case "TEN_BENH" |"DIA_CHI":
                    table.setColumnWidth(i, 500)
    
    