import sys 
sys.dont_write_bytecode = True

import os
import shutil

from Logs.GetTracebackLogs import *


def clearDir(dir_path):

    logger.info("Validating path")
    try:
        if os.path.isdir(dir_path):
            for root, dirs, files in os.walk(dir_path):
                #clear files
                try:
                    for f in files:
                        os.unlink(os.path.join(root, f))
                        logger.info("% s has been removed successfully" % f)
                except OSError as e:
                    logger.error(str(e))
                    logger.error(traceback.format_exc())
                #clear subfolders
                for d in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, d))
                        logger.info("% s has been removed successfully" % d)
                    except OSError as e:
                        logger.error(str(e))
                        logger.error(traceback.format_exc())
            return True
        elif os.path.isfile(dir_path):
            os.unlink(os.path.join(dir_path))
            logger.info("% s has been removed successfully" % dir_path)
            return True
        else:  
            logger.error("Method Error - Entered path does not exist: % s" % dir_path)
            return False

    except Exception as e:
        logger.error(str(e))
        logger.error(traceback.format_exc())








import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False








def LastNlines(fname, N):
     
    # assert statement check
    # a condition
    assert N >= 0
     
    # declaring variable
    # to implement
    # exponential search
    pos = N + 1
     
    # list to store
    # last N lines
    lines = []
     
    # opening file using with() method
    # so that file get closed
    # after completing work
    with open(fname) as f:
         
        # loop which runs
        # until size of list
        # becomes equal to N
        while len(lines) <= N:
             
            # try block
            try:
                # moving cursor from
                # left side to
                # pos line from end
                f.seek(-pos, 2)
         
            # exception block
            # to handle any run
            # time error
            except IOError:
                f.seek(0)
                break
             
            # finally block
            # to add lines
            # to list after
            # each iteration
            finally:
                lines = list(f)
             
            # increasing value
            # of variable
            # exponentially
            pos *= 2
             
    # returning the
    # whole list
    # which stores last
    # N lines
    return lines[-N:]
 
    # # Driver Code:
    # if __name__ == '__main__':
    #     fname = 'File1.txt'
    #     N = 3
    #     try:
    #         lines = LastNlines(fname, N)
    #         for line in lines:
    #             print (line, end ='')
    #     except:
    #         print('File not found')














# if is_admin():
#     # Code of your program here
#     dir_path = 'E:\\IT\\Drivers\\TestDir\\1.jpg'
#     clearDir(dir_path)
# else:
#     # Re-run the program with admin rights
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)



# k=input("press close to exit") 