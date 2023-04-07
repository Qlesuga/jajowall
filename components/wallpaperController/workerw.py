import win32gui

#get progman atom
progman = win32gui.FindWindow("Progman",None)

#creates window "WorkerW" between icons and wallpaper do nothing if exits
win32gui.SendMessageTimeout(progman,
                            0x052C,
                            0,
                            0,
                            0,
                            1000)

workerw = 0

#function to find workerw
def get_workerw(tophandle, topparamhandle):
    global workerw
    shell = win32gui.FindWindowEx(tophandle, 
                                  0, 
                                  "SHELLDLL_DefView", 
                                  None);
    #shell != 0 if found
    if(shell != 0):
        workerw = win32gui.FindWindowEx(0, 
                                        tophandle, 
                                        "WorkerW", 
                                        None);
    return True

#loop over windows using "get_workerw" function
win32gui.EnumWindows(get_workerw, 0)
