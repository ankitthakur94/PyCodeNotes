# Objective : 
# Explore logging per module

import logging
####### Root Looger ##############

## We have seen that how logging can be used. Following is the basic syntax to create a logger
#  logging.basicConfig ( level = logging.DEBUG , filename = 'logging_file.log' , format = '%(asctime)s :%(levelname)s : %(message)s ' )
# The above statement configures the root logger in the file the statement has been written.

# and now instead of print we can do 
# logging.debug ( ' <string> ' )
# Now this string will be printed in the file mentioned in root logger.



####### Issues with root logger ###########
# Say we are working with multiple python files (module1.py module2.py )
# we do > import module 1  in module2.py
# each of the above files has a root logger configured which dumps logging messages in module1.log and module2.log
# Now when we run python module2.py
# There is an issue
# All the logging info is dumped in module1.log (and no new module2.log is created)
# This is because module1 was imported and its root logger was first created which dumps files in module1.log
# Now after module1 is finished and we come to create root logger of module2, that statement does nothing
# It does not over write the root logger created in module1, thus info is still dumped in the file of original root logger.

# So once the root logger is set the first time. It does not get overridden and all the logging of all the modules in done via the same root logger.
######### Solution ###########


#Instead of creating root logger we create a separate non-root  logger in each file.


# Create a new logger (This will be our custom logger not the root logger)
# We can actually hardcode any name we want but it is a general practice to use __name__ so that if this module is imported in some other module, name of the logger is set to name of the module.
# now instead of using logging.info (<string>) we will use logger_1.info (<string>)

logger_1 = logging.getLogger (__name__)
# If a module is executed directly, __name__ is set to '__main__'
# If a module is imported in some other module, __name__ is set to the module name.


# -> 1.) Set the default level of our custom logger.
logger_1.setLevel (logging.INFO)


# -> 2.) Create an output filename
# To specify the output file for our custom logger we will have to create a file handler and add that handler to our logger.
file_handler = logging.FileHandler ('11_B_output.log')
logger_1.addHandler (file_handler)


# -> 3.) Set format of the output file.
# To specify the format for our custom logger we will have to create a formatter and add that formatter to file handler
formatter = logging.Formatter('%(asctime)s :%(levelname)s : %(message)s')
file_handler.setFormatter(formatter)


logger_1.debug ( ' How is the day today ' )
logger_1.info (' Today can be a good day ' )
logger_1.warning ( ' Only if you do not screw over ' )
logger_1.error ( ' Stop believing others ' )
logger_1.critical ( ' Damn you bro ! I told you to believe yourself . You are now doomed ' )








































