import win32gui
import config

#get progman atom
progman = win32gui.FindWindow("Progman",None)

#create window "WorkerW" between icons and wallpaper do nothing if exits
win32gui.SendMessageTimeout(progman,
                                0x052C,
                                0,
                                0,
                                0,
                                1000)

#function to find workerw
def get_workerw(tophandle, topparamhandle):
    shell = win32gui.FindWindowEx(tophandle, 
                              0, 
                              "SHELLDLL_DefView", 
                              None);
    #shell != 0 if found
    if(shell != 0):
        config.workerw = win32gui.FindWindowEx(0, 
                                   tophandle, 
                                   "WorkerW", 
                                   None);
    return True

#loop over windows using "get_workerw" function
win32gui.EnumWindows(get_workerw, 0)
print(config.workerw)