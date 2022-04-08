import sys
import winreg

#######################################
'''
  STEP 2: Getting all values in OpenSavePidlMRU subkeys
    - winreg: https://docs.python.org/3/library/winreg.html
    - OpenSavePidlMRU key path
      > HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU
    - Query Values (winreg.QueryValueEx)
      > https://docs.python.org/3/library/winreg.html
      > https://github.com/gitgiant/forensics/blob/master/openSaveMRU.py
'''



with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkcu:
    with winreg.OpenKey(hkcu, r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU") as targetkey:
        try:
            for i in range(0, winreg.QueryInfoKey(targetkey)[0]):
                asubkeyname = winreg.EnumKey(targetkey, i)
                print(asubkeyname)

                with winreg.OpenKey(targetkey, asubkeyname) as asubkey:
                    for j in range(0, winreg.QueryInfoKey(asubkey)[1]):
                        print("  - {}".format(winreg.EnumValue(asubkey,j)[0]))
        except WindowsError:
            pass
        
        
        
    
