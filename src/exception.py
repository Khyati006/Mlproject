import sys
import src.logger import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()#this will genrate 3 info we are intrested in third one.
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error ocuured in python sript name[{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):                                           #inheriting the exception
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)                                         #this wil inherit the init funciton
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):                                                          #this will print the error msg itself
        return self.error_message

 
