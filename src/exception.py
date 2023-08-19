# for exception handling purpose, this is common for entire project
import sys
import logging  

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb= error_detail.exc_info()   # gives three output, we will need only third
    file_name = exc_tb.tb_frame.f_code.co_filename  # it will give file name in which error occured
    error_message = "Error Occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)  
    ) 
    return error_message

class CustomException(Exception):
    # class constructor
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) # inherit the init function for exception class  
        self.error_message=error_message_detail(error_message,error_detail) 

    # inherit other functionality
    def __str__(self):
        return self.error_message  


# testing  this file
# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("divide by zero...")
#         raise CustomException(e,sys)