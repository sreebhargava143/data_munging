'''
contains a abstract class used to clean noisy data
'''
import re

class Cleaner(object):
    '''
    cleans noisy data
    '''
    def __init__(self):
        pass

    def get_cleaned_number(self, data_field):
        '''
        cleans and returns number string
        '''
        cleaned_number = re.findall(r"[\d]", data_field)
        number_string = ''
        for number in cleaned_number:
            number_string += number
        return number_string
