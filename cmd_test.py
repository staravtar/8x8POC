import sys
import os
import win32com.shell.shell as shell
from time import sleep



if __name__=="__main__":
    #os.system("powershell -Command Start-Process cmd -Verb RunAs")


    commands = 'C:/Users/akumar60/Desktop/clumsy-0.2-win64/clumsy.exe --filter outbound --drop on --drop-inbound on --drop-outbound on --drop-chance 10.0'
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + commands)
    sleep(10)
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c taskkill /f /im clumsy.exe*' )


