##################################
# Objective : Explore Basic logging
##################################


##################################
## Theory : 
##################################
## logging is an inbuilt module.
## Has 5 default levels of logging :
#DEBUG (10):
#	Detailed information, typically of interest only when diagnosing problems.
#INFO  (20):
#	Confirmation that things are working as expected.
#WARNING (30):
#ERROR (40):
#	Due to a more serious problem, the software has not been able to perform some function.
#CRITICAL (50):
#	A serious error, indicating that the program itself may be unable to continue running.


## By default statements above Warning level (>30) are printed by logging module. We can of course change that.

##################################



import logging

logging.basicConfig ( level = logging.DEBUG , filename = 'logging_file.log' , format = '%(asctime)s :%(levelname)s : %(message)s ' )
# level : Determines the minimum level of logging 
# filename : File to dump the log info into. If not specified, console is default.
# format : format of each line. Here it is <time> <levelname> <message_string>

logging.debug ( ' How is the day today ' )
logging.info (' Today can be a good day ' )
logging.warning ( ' Only if you do not screw over ' )
logging.error ( ' Stop believing others ' )
logging.critical ( ' Damn you bro ! I told you to believe yourself . You are now doomed ' )







