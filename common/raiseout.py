import traceback
from util.log.mylog import Log

def raiseout():
    Log().debug( "This is a debug log.")
    with open(Log().logname, 'a+') as f:
        f.writelines(traceback.format_exc())