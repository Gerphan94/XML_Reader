from PyQt5 import QtCore, QtGui, QtWidgets

#20E3B2
class xml_table():
    def __init__(self):
        self.XML1_COL = ["MA_LK","STT","MA_BN","HO_TEN","NGAY_SINH","GIOI_TINH","DIA_CHI","MA_THE","MA_DKBD","GT_THE_TU","GT_THE_DEN","MIEN_CUNG_CT","TEN_BENH","MA_BENH","MA_BENHKHAC","MA_LYDO_VVIEN","MA_NOI_CHUYEN","MA_TAI_NAN","NGAY_VAO","NGAY_RA","SO_NGAY_DTRI","KET_QUA_DTRI","TINH_TRANG_RV","NGAY_TTOAN","T_THUOC","T_VTYT","T_TONGCHI","T_BNTT","T_BNCCT","T_BHTT","T_NGUONKHAC","T_NGOAIDS","NAM_QT","THANG_QT","MA_LOAI_KCB","MA_KHOA","MA_CSKCB","MA_KHUVUC","MA_PTTT_QT","CAN_NANG"]
        self.XML2_COL = ['MA_LK','STT','MA_THUOC','MA_NHOM','TEN_THUOC','DON_VI_TINH','HAM_LUONG','DUONG_DUNG','LIEU_DUNG','SO_DANG_KY','TT_THAU','PHAM_VI','TYLE_TT','SO_LUONG','DON_GIA','THANH_TIEN','MUC_HUONG','T_NGUONKHAC','T_BNTT','T_BHTT','T_BNCCT','T_NGOAIDS','MA_KHOA','MA_BAC_SI','MA_BENH','NGAY_YL','MA_PTTT']
        self.XML3_COL = ['MA_LK','STT','MA_DICH_VU','MA_VAT_TU','MA_NHOM','GOI_VTYT','TEN_VAT_TU','TEN_DICH_VU','DON_VI_TINH','PHAM_VI','SO_LUONG','DON_GIA','TT_THAU','TYLE_TT','THANH_TIEN','T_TRANTT','MUC_HUONG','T_NGUONKHAC','T_BNTT','T_BHTT','T_BNCCT','T_NGOAIDS','MA_KHOA','MA_GIUONG','MA_BAC_SI','MA_BENH','NGAY_YL','NGAY_KQ','MA_PTTT']
        self.XML4_COL = ['MA_LK','STT','MA_DICH_VU','MA_CHI_SO','TEN_CHI_SO','GIA_TRI','MA_MAY','MO_TA','KET_LUAN','NGAY_KQ']
        self.XML5_COL = ['MA_LK','STT','DIEN_BIEN','HOI_CHAN','PHAU_THUAT','NGAY_YL']

    def setupUi_XML1(self, table):
        #self.tbXML1 = QtWidgets.QTableWidget()
        #table = QtWidgets.QTableWidget()
        table.setColumnCount(len(self.XML1_COL))
        table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        table.setSelectionMode(QtWidgets.QTableView.SingleSelection)
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i,tag in enumerate(self.XML1_COL):
            table.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(tag + f'({i+1})'))
            match tag:
                case "STT":
                    table.setColumnWidth(i, 50)
                case "GIOI_TINH":
                    table.setColumnWidth(i, 90)
                case "HO_TEN":
                    table.setColumnWidth(i, 150)
                case "TEN_BENH" |"DIA_CHI":
                    table.setColumnWidth(i, 500)

    def setupUi_XML2(self, table):
        #table = QtWidgets.QTableWidget()
        table.setColumnCount(len(self.XML2_COL))
        table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        table.setSelectionMode(QtWidgets.QTableView.SingleSelection)
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        table.setSortingEnabled(True)
        for i,tag in enumerate(self.XML2_COL):
            table.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(tag + f' ({i+1})'))
            match tag:
                case "STT":
                    table.setColumnWidth(i, 50)
                case "MA_KHOA" | "TYLE_TT" | "PHAM_VI":
                    table.setColumnWidth(i, 70)
                case "LIEU_DUNG" | "TEN_THUOC":
                    table.setColumnWidth(i, 300)
               
    # XML3 TABLE -----------------------------------
    def setupUi_XML3(self, table):

        #table = QtWidgets.QTableWidget()
        table.setColumnCount(len(self.XML3_COL))
        table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        table.setSelectionMode(QtWidgets.QTableView.SingleSelection)
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i,tag in enumerate(self.XML3_COL):
            table.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(tag + f' ({i+1})'))
            match tag:
                case "STT" | "TY_LE":
                    table.setColumnWidth(i, 50)
                case "TYLE_TT":
                    table.setColumnWidth(i, 70)
                case "TEN_VAT_TU" | "TEN_DICH_VU":
                    table.setColumnWidth(i, 400)
              
    def setupUi_XML4(self, table):
        
        #table = QtWidgets.QTableWidget()
        table.setColumnCount(len(self.XML4_COL))
        table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        table.setSelectionMode(QtWidgets.QTableView.SingleSelection)
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i,tag in enumerate(self.XML4_COL):
            table.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(tag + f' ({i+1})'))
            match tag:
                case "STT":
                    table.setColumnWidth(i, 50)
                case "GIOI_TINH":
                    table.setColumnWidth(i, 80)
                case "HO_TEN":
                    table.setColumnWidth(i, 150)
                case "TEN_BENH" |"DIA_CHI":
                    table.setColumnWidth(i, 500)
    
    def setupUi_XML5(self, table):
        #table = QtWidgets.QTableWidget()
        table.setColumnCount(len(self.XML5_COL))
        table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        table.setSelectionMode(QtWidgets.QTableView.SingleSelection)
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i,tag in enumerate(self.XML5_COL):
            table.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(tag + f' ({i+1})'))
            match tag:
                case "STT":
                    table.setColumnWidth(i, 50)
                case "GIOI_TINH":
                    table.setColumnWidth(i, 80)
                case "TEN_VAT_TU" | "TEN_DICH_VU":
                    table.setColumnWidth(i, 200)
                case "TEN_BENH" |"DIA_CHI":
                    table.setColumnWidth(i, 500)
    
    def init_align_colum(self, xml_table):
        center_col = []
        right_col = []
        match xml_table:
            case "XML1":
                ...
            case "XML2":
                c_column = ['MA_LK','STT','MA_THUOC','MA_NHOM','DON_VI_TINH','HAM_LUONG','DUONG_DUNG','PHAM_VI','TYLE_TT','MUC_HUONG','MA_KHOA','MA_BAC_SI','MA_BENH','NGAY_YL','MA_PTTT']
                r_column = ['SO_LUONG','DON_GIA','THANH_TIEN','T_NGUONKHAC','T_BNTT','T_BHTT','T_BNCCT','T_NGOAIDS']
                for i, ele in enumerate(self.XML2_COL):
                    if ele in c_column:
                        center_col.append(i+1)
                    elif ele in r_column:
                        right_col.append(i+1)
                
            case "XML3":
                c_column = ['MA_LK','STT','MA_DICH_VU','MA_VAT_TU','MA_NHOM','GOI_VTYT','DON_VI_TINH','PHAM_VI','TYLE_TT','MUC_HUONG','MA_KHOA','MA_GIUONG','MA_BAC_SI','MA_BENH','NGAY_YL','NGAY_KQ','MA_PTTT']
                r_column = ['SO_LUONG','DON_GIA','THANH_TIEN','T_TRANTT','T_NGUONKHAC','T_BNTT','T_BHTT','T_BNCCT','T_NGOAIDS']
                for i, ele in enumerate(self.XML3_COL):
                    if ele in c_column:
                        center_col.append(i+1)
                    elif ele in r_column:
                        right_col.append(i+1)
        
                
                ...
            case "XML4":
                ...
            case "XML5":
                ...
        return center_col, right_col