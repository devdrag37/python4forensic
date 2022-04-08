import sys
import winreg

#######################################
'''
  STEP 1: Getting Subkeys of OpenSavePidlMRU in the local system
    - winreg: https://docs.python.org/3/library/winreg.html
    - OpenSavePidlMRU key path
      > HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU
'''



with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkcu:
    with winreg.OpenKey(hkcu, r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU") as targetkey:
        try:
            i = 0
            while True:
                asubkey = winreg.EnumKey(targetkey, i)
                print(asubkey)
                i += 1
        except WindowsError:
            pass
        
        
        
    
