import sys ## sys has all the info related to exception.
import logging
def error_message_details(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info() ## on which line the error has occured.
    file_name = exc_tb.tb_frame.f_code.co_filename ### to get file name
    error_message = "Error occured in python script name [{0}] line no [{1} error message [{2}]].".format(
        file_name, exc_tb.tb_lineno,str(error))
    return error_message

class CustomException (Exception):
    def __int__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message
    
