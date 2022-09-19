def _extract_id(line):
    return line[0:4]


class Record:
    def __init__(self, line, pos_in_file, is_ini, idx):
        self.id = _extract_id(line)
        self.pos = pos_in_file
        self.is_ini = is_ini
        self.idx = idx

    def get_line(self, file):
        file.seek(self.pos)
        return file.readline()
