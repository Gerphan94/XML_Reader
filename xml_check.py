from database import dataConnection

dt_conn = dataConnection()

class xml_check():
    def __init__(self) -> None:
        pass

    def xml1_check(sefl,malk):
        ...
    
    def xml2_check(self, malk):
        _log = []
        rows = dt_conn.get_xml2(malk)
        for row in rows:
            _ma_lk = row[1]

            _ma_thuoc = row[3]
            _ma_nhom = row[4]
            _ten_thuoc = row[5]
            _dvt = row[6]
            _ham_luong = row[7]
            _duong_dung = row[8]
            _lieu_dung = row[9]
            _so_dk = row[10]
            _tt_thau = row[11]
            _pham_vi = row[12]
            _tyle_tt = row[13]
            _sl = row[14]
            _don_gia = row[15]
            _thanh_tien = row[16]
            _mh = row[17]
            # _nguon_khac = row[18]
            _bntt = row[19]
            _bhtt = row[20]
            _bnctt = row[21]
            _ma_khoa = row[23]
            _ma_bs = row[24]
            _ma_benh = row[25]
            _ngay_yl = row[26]

            

            # Kiểm tra các dữ liệu NOT NULL
            if ( _ma_thuoc == '' ):
                _log.append("MA_THUOC trống")
            if (_ma_nhom != '4'):
                _log.append("MA_NHOM không đúng")
            if (_ten_thuoc == ''):
                _log.append("TEN_THUOC trống")
            if (_duong_dung == ''):
                _log.append("DUONG_DUNG trống")
            if (_lieu_dung ==''):
                _log.append("LIEU_DUNG trống")
            if (_ma_khoa ==''):
                _log.append("MA_KHOA trống")
            if (_ma_bs ==''):
                _log.append("MA_BAC_SI trống")
            

            # Gán các biến Số lượng, tiền tệ sang float
            sl = self.convert_Str2Float(_sl)
            don_gia = self.convert_Str2Float(_don_gia)
            thanh_tien = self.convert_Str2Float(_thanh_tien)


            if (don_gia == None):
                _log.append("DON_GIA không đúng định dạng")
            if ( don_gia == 0.0):
                _log.append("DON_GIA = 0")
            
            # Kiểm tra THANH_TIEN so với SL*DON_GIA
            if (sl != None and don_gia != None):
                tmp_thanhtien = sl*don_gia
                if (tmp_thanhtien == thanh_tien):
                    print("ĐÚNG")
                else:
                    print("SAI")


        return _log



    def xml3_check(self, malk):
        _log = []
        rows = dt_conn.get_xml3(malk)
        for row in rows:
            _ma_lk = row[1]
            _ma_dv = row[3]
            _ma_vt = row[4]
            _ma_nhom = row[5]
            
            _pham_vi = row[10]
            _ma_khoa = row[23]
            _ma_giuong = row[24]
            _ma_benh = row[26]

            if (_pham_vi == '2'):
                _log.append("Lỗi PHAM_VI = 2")
            if (_ma_nhom == '10'):
                if (_ma_vt ==''):
                    _log.append("MA_VAT trống")
            else:
                if (_ma_nhom == '14' or _ma_nhom == '15'):
                    if (_ma_giuong == ''):
                        _log.append("MA_GIUONG trống")
            # Kiểm tra mã khoa (Dữ liệu bắt buộc)
            if (_ma_khoa == ''):
                _log.append("MA_GIUONG trống")
            # Kiểm tra MA_BENH Mã bệnh bao gồm mã bệnh chính và các mã bệnh kèm theo
            icd_list = dt_conn.get_icdCode(_ma_lk)
            if (_ma_benh != icd_list):
                _log.append("MA_BENH Không đúng dữ liệu")
        return _log
    
    def convert_Str2Float(self, string):
        try:
            num = float(string)
            return num
        except:
            return None
