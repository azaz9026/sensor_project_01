import sys
import traceback

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = self.error_message_detail(error_message, error_details)

    def error_message_detail(self, error_message, error_details: sys):
        _, _, exc_tb = error_details.exc_info()
        line_number = exc_tb.tb_lineno
        file_name = exc_tb.tb_frame.f_code.co_filename
        return f"Error occurred in script: {file_name}, line: {line_number}, message: {error_message}"

    def __str__(self):
        return self.error_message
