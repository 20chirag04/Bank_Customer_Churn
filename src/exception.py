import sys
from src.logger import logging

class CustomException(Exception):
    def __init__(self,error_message,error_details):
        super().__init__(error_message)
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.line_number = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

        self.error_message = (
            f"Error occurred in python script : [{self.file_name}]\n"
            f"line number [{self.line_number}]  "
            f"error message [{error_message}]"
)

    def __str__(self):
        return self.error_message

