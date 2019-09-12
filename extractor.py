'''
contains all class responsible
for data extraction
'''
class DataExtractor(object):
    '''
    Extracts data open for extension closed for modification
    '''
    file_path = ''
    seekpoint = 0
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path) as opened_file:
            opened_file.readline()
            self.seekpoint = opened_file.tell()

    def get_next_fields(self):
        '''
        gives the fields of a data row
        '''
        with open(self.file_path) as opened_file:
            opened_file.seek(self.seekpoint)
            line = opened_file.readline()
            if line == "":
                return 'EOF'
            self.seekpoint = opened_file.tell()
        return line.split()
