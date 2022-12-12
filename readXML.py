from bs4 import BeautifulSoup
import base64
from database import dataConnection


dt_conn = dataConnection()

class ReadXML(object):
    def __init__(self, path):
        self.path = path
        self.xml_content = ''
        self.hoso_count = 0
        self.read_file()
        pass

    def read_file(self):
        try:
            with open(self.path, 'r') as f:
                data = f.read()
        except Exception as e:
            print(e)
            return
        self.xml_content = BeautifulSoup(data, "xml")

    def init_xml_table(self):
        dt_conn.delete_xml1_table()
        dt_conn.delete_xml2_table()
        dt_conn.delete_xml3_table()

        file_hoso_list = self.xml_content.find_all('FILEHOSO')
        for file in file_hoso_list:
            loai_hs = file.find('LOAIHOSO')
            nd_hs = file.find('NOIDUNGFILE')
            match loai_hs.text:
                case 'XML1':
                    dt_conn.insert_xml1_table(nd_hs.text)
                case 'XML2':
                    dt_conn.insert_xml2_table(nd_hs.text)
                case 'XML3':
                    dt_conn.insert_xml3_table(nd_hs.text)
                    pass
                case 'XML4':
                    pass
                case 'XML5':
                    pass
    
    def get_tag_xml2(self):
        baseString = "PERTQUNIX0NISV9USUVUX1RIVU9DPg0KICA8Q0hJX1RJRVRfVEhVT0M+DQogICAgPE1BX0xLPlROLjIyMTIuMDAwNDY3PC9NQV9MSz4NCiAgICA8U1RUPjE8L1NUVD4NCiAgICA8TUFfVEhVT0M+PC9NQV9USFVPQz4NCiAgICA8TUFfTkhPTT40PC9NQV9OSE9NPg0KICAgIDxURU5fVEhVT0M+Q2VydGljYW48L1RFTl9USFVPQz4NCiAgICA8RE9OX1ZJX1RJTkg+VmnDqm48L0RPTl9WSV9USU5IPg0KICAgIDxIQU1fTFVPTkc+MCwyNW1nPC9IQU1fTFVPTkc+DQogICAgPERVT05HX0RVTkc+PC9EVU9OR19EVU5HPg0KICAgIDxMSUVVX0RVTkc+MiBWacOqbi9s4bqnbiAqIDEgbOG6p24vbmfDoHk8L0xJRVVfRFVORz4NCiAgICA8U09fREFOR19LWT5WTjEtNTkxLTExPC9TT19EQU5HX0tZPg0KICAgIDxUVF9USEFVPjIwMjIuMTIuMDg7RzE7TjE8L1RUX1RIQVU+DQogICAgPFBIQU1fVkk+MTwvUEhBTV9WST4NCiAgICA8VFlMRV9UVD4xMDA8L1RZTEVfVFQ+DQogICAgPFNPX0xVT05HPjEyLjAwMDwvU09fTFVPTkc+DQogICAgPERPTl9HSUE+OTAwLjAwMDwvRE9OX0dJQT4NCiAgICA8VEhBTkhfVElFTj4xMDgwMC4wMDwvVEhBTkhfVElFTj4NCiAgICA8TVVDX0hVT05HPjEwMDwvTVVDX0hVT05HPg0KICAgIDxUX05HVU9OS0hBQz48L1RfTkdVT05LSEFDPg0KICAgIDxUX0JOVFQ+MC4wMDwvVF9CTlRUPg0KICAgIDxUX0JIVFQ+MTA4MDAuMDA8L1RfQkhUVD4NCiAgICA8VF9CTkNDVD4wLjAwPC9UX0JOQ0NUPg0KICAgIDxUX05HT0FJRFM+PC9UX05HT0FJRFM+DQogICAgPE1BX0tIT0E+SzAxPC9NQV9LSE9BPg0KICAgIDxNQV9CQUNfU0k+ZHdkdzwvTUFfQkFDX1NJPg0KICAgIDxNQV9CRU5IPkEwMDwvTUFfQkVOSD4NCiAgICA8TkdBWV9ZTD4yMDIyMTIwODA5NTU8L05HQVlfWUw+DQogICAgPE1BX1BUVFQ+MTwvTUFfUFRUVD4NCiAgPC9DSElfVElFVF9USFVPQz4NCiAgPENISV9USUVUX1RIVU9DPg0KICAgIDxNQV9MSz5UTi4yMjEyLjAwMDQ2NzwvTUFfTEs+DQogICAgPFNUVD4yPC9TVFQ+DQogICAgPE1BX1RIVU9DPlZOLVZJVDAwMTwvTUFfVEhVT0M+DQogICAgPE1BX05IT00+NDwvTUFfTkhPTT4NCiAgICA8VEVOX1RIVU9DPlZpdGFtaW4gQyAoY29kZSBCSFlUKTwvVEVOX1RIVU9DPg0KICAgIDxET05fVklfVElOSD5WacOqbjwvRE9OX1ZJX1RJTkg+DQogICAgPEhBTV9MVU9ORz4zNSBtZzwvSEFNX0xVT05HPg0KICAgIDxEVU9OR19EVU5HPjwvRFVPTkdfRFVORz4NCiAgICA8TElFVV9EVU5HPjEgVmnDqm4vbOG6p24gKiAxIGzhuqduL25nw6B5PC9MSUVVX0RVTkc+DQogICAgPFNPX0RBTkdfS1k+Qy4wMTA5PC9TT19EQU5HX0tZPg0KICAgIDxUVF9USEFVPjIwMjIuMTIuMDg7RzE7TjE8L1RUX1RIQVU+DQogICAgPFBIQU1fVkk+MTwvUEhBTV9WST4NCiAgICA8VFlMRV9UVD44MDwvVFlMRV9UVD4NCiAgICA8U09fTFVPTkc+Ni4wMDA8L1NPX0xVT05HPg0KICAgIDxET05fR0lBPjEyMDAuMDAwPC9ET05fR0lBPg0KICAgIDxUSEFOSF9USUVOPjcyMDAuMDA8L1RIQU5IX1RJRU4+DQogICAgPE1VQ19IVU9ORz4xMDA8L01VQ19IVU9ORz4NCiAgICA8VF9OR1VPTktIQUM+PC9UX05HVU9OS0hBQz4NCiAgICA8VF9CTlRUPjE0NDAuMDA8L1RfQk5UVD4NCiAgICA8VF9CSFRUPjU3NjAuMDA8L1RfQkhUVD4NCiAgICA8VF9CTkNDVD4wLjAwPC9UX0JOQ0NUPg0KICAgIDxUX05HT0FJRFM+PC9UX05HT0FJRFM+DQogICAgPE1BX0tIT0E+SzAxPC9NQV9LSE9BPg0KICAgIDxNQV9CQUNfU0k+ZHdkdzwvTUFfQkFDX1NJPg0KICAgIDxNQV9CRU5IPkEwMDwvTUFfQkVOSD4NCiAgICA8TkdBWV9ZTD4yMDIyMTIwODA5NTU8L05HQVlfWUw+DQogICAgPE1BX1BUVFQ+MTwvTUFfUFRUVD4NCiAgPC9DSElfVElFVF9USFVPQz4NCjwvRFNBQ0hfQ0hJX1RJRVRfVEhVT0M+"
        data = base64.b64decode(baseString)
        data = BeautifulSoup(data, "xml").find("DSACH_CHI_TIET_THUOC").find("CHI_TIET_THUOC")
        string = ""
        for tag in data:
            if (tag.name != None):
                string = string + "'" + tag.name + "',"
        print(string)        

# if __name__ == "__main__":
#     a = ReadXML('')
#     a.init_xml2()