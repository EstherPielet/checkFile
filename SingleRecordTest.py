from abc import ABC, abstractmethod
from Record import Record
import re


class SingleRecodeTest(ABC):
    @abstractmethod
    def is_supported(self, rec):
        pass

    @abstractmethod
    def check(self, record, line, file):
        pass


class INI001(SingleRecodeTest):
    def is_supported(self, rec):
        return rec.id == 'A000'

    def check(self, record, line, file):
        if record.id != 'A000':
            return "בקובץ INI.TXT שדה 100 שגוי"


class INI004(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        numeric = line[34:48]
        pattern = re.compile(r"[1-9]")
        match = pattern.findall(numeric)
        if not match:
            return "שדה 1004 שדה חובה חייב להכיל ערך"


class INI005(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        my_str = line[49:56]
        pattern = re.compile(r"OF1.3&")
        match = pattern.findall(my_str)
        if not match:
            return "שדה 1005 אינונ תקין"


class INI006(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        numeric = line[64:57]
        pattern = re.compile(r"[1-9]")
        match = pattern.findall(numeric)
        if not match:
            return "שדה 1006 שדה חובה חייב להכיל ערך"


class INI007(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        numeric = line[65:84]
        pattern = re.compile(r"[a-zA-Z1-9]+")
        match = pattern.findall(numeric)
        if not match:
            return "שדה1007  שדה חובה חייב להכיל ערך"


class INI008(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        alpha = line[85:104]
        pattern = re.compile(r"[a-zA-Z1-9]+")
        match = pattern.findall(alpha)
        if not match:
            return "שדה 1008 שדה חובה חייב להכיל ערך"


class INI009(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        numeric = line[65:84]
        pattern = re.compile(r"[1-9]+")
        match = pattern.findall(numeric)
        if not match:
            return "שדה 1009 שדה חובה חייב להכיל ערך"


class INI010(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        alpha = line[114:133]
        pattern = re.compile(r"[a-zA-Z1-9]+")
        match = pattern.findall(alpha)
        if not match:
            return "שדה 1010 שדה חובה חייב להכיל ערך"


class INI011(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        char = line[134:134]
        if char != "2":
            return "שדה 1011 אינו תקין"


class INI012(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        alpha = line[135:184]
        pattern = re.compile(r"[a-zA-Z1-9]+")
        match = pattern.findall(alpha)
        if not match:
            return "שדה 1012 שדה חובה חייב להכיל ערך"


class INI013(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        char = line[185:185]
        if char != "2":
            return "שדה 1013 אינו תקין"


class INI014(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        char = line[186:186]
        if char != "2" or char != "1":
            return "שדה 1014 אינו תקין"


class INI015(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        alpha = line[215:264]
        pattern = re.compile(r"[a-zA-Z1-9]+")
        match = pattern.findall(alpha)
        if not match:
            return "שדה 1018 שדה חובה חייב להכיל ערך"


class INI016(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        numeric = line[367:374]
        pattern = re.compile(r"[1-9]")
        match = pattern.findall(numeric)
        if not match:
            return "שדה 1024 שדה חובה חייב להכיל ערך"


class INI017(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        numeric = line[375:382]
        pattern = re.compile(r"[1-9]")
        match = pattern.findall(numeric)
        if not match:
            return "שדה 1025 שדה חובה חייב להכיל ערך"


class INI018(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        numeric = line[383:390]
        pattern = re.compile(r"[1-9]")
        match = pattern.findall(numeric)
        if not match:
            return "שדה 1026 שדה חובה חייב להכיל ערך"


class INI019(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        numeric = line[391:394]
        pattern = re.compile(r"[1-9]")
        match = pattern.findall(numeric)
        if not match:
            return "שדה 1027 שדה חובה חייב להכיל ערך"


class INI020(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        numeric = line[395:395]
        pattern = re.compile(r"[1-9]")
        match = pattern.findall(numeric)
        if not match:
            return "שדה 1028 שדה חובה חייב להכיל ערך"


class INI021(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        char = line[396:396]
        if char != "2" or char != "1":
            return "שדה 1029 אינו תקין"


class INI022(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        alpha = line[397:416]
        pattern = re.compile(r"[a-zA-Z1-9]+")
        match = pattern.findall(alpha)
        if not match:
            return "שדה 1030 שדה חובה חייב להכיל ערך"


class INI023(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        alpha = line[417:419]
        pattern = re.compile(r"[a-zA-Z1-9]+")
        match = pattern.findall(alpha)
        if not match:
            return "שדה 1032 שדה חובה חייב להכיל ערך"


class INI024(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A000'

    def check(self, record, line, file):
        char = line[420:420]
        if char == "1" or char == '0':
            return "שדה 1034 אינו תקין"


# ? what should i return in get_type function
class INI025(SingleRecodeTest):
    def is_supported(self, rec):
        return rec.is_ini and 2 <= rec.idx < 7

    def check(self, record, line, file):
        alpha = line[0:4]
        pattern = re.compile(r"(B100|B110|C100|D100|D1200|M100)")
        match = pattern.findall(alpha)
        if not match:
            return "שדה  1050 אינו תקין"


class INI028(SingleRecodeTest):
    def is_supported(self, rec):
        return 'A100'

    def check(self, record, line, file):
        if len(line) != 466:
            return "אורך רשומה A100 לא תקין"
