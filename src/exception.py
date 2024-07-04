import sys
#function to print error message
def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc.info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.lineno,str(error)
    )
    return error_message
#create custom class for exception
class CustomException(Exception):
    #define constructor function
    def __init__(self,error_message,error_details:sys):
        #initialize __init__
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail= error_details)
    def __str__(self):
        return self.error_message
        
        

