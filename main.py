from win32com.makegw.makegwparse import error_not_supported

from Record import Record
from SingleRecordTest import *

class INI():
    def __init__(self,file_path):
        self.file_path=file_path
    def run_file_ini(self):
        single_record_tests = [INI001(), INI004(), INI005(), INI006(), INI007(), INI008(), INI009(),
                               INI010(), INI011(), INI012(), INI013(), INI014(), INI015(), INI016(), INI017(),
                               INI018(), INI019(), INI020(), INI021(), INI022(),INI023(), INI024(), INI025(),
                               INI028()]
        file_path = self.file_path
        record_list = []
        errors = []
        with open(file_path, 'r') as f:
            pos = f.tell()
            line = f.readline()
            while line:
                rec = Record(line, pos, True, len(record_list) + 1)
                record_list.append(rec)
                print(f'line: {line} pos: {pos}')
                for test in single_record_tests:
                    if test.is_supported(rec):
                        err = test.check(rec, line, f)
                        if err:
                            errors.append(err)
                pos = f.tell()
                line = f.readline()
        for err in errors:
            print(err)

ini=INI("C:/Users/Esther Bienstock/Downloads/INI.txt")
ini.run_file_ini()