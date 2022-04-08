import sys
import winreg
import pyfwsi

#######################################
'''
  STEP 3: Translate value data to Shell Item List format data
    - winreg: https://docs.python.org/3/library/winreg.html
    - OpenSavePidlMRU key path
      > HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU
    - Query Values (winreg.QueryValueEx)
      > https://docs.python.org/3/library/winreg.html
      > https://github.com/gitgiant/forensics/blob/master/openSaveMRU.py
    - Shell Item List format
      > https://github.com/libyal/libfwsi/blob/main/documentation/Windows%20Shell%20Item%20format.asciidoc
    - pyfwsi document
      > https://github.com/libyal/libfwsi/wiki/Python-development
'''



with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkcu:
    with winreg.OpenKey(hkcu, r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU") as targetkey:
        try:
            for i in range(0, winreg.QueryInfoKey(targetkey)[0]): # [0]: get key count
                asubkeyname = winreg.EnumKey(targetkey, i)
                print(asubkeyname)

                with winreg.OpenKey(targetkey, asubkeyname) as asubkey:
                    for j in range(0, winreg.QueryInfoKey(asubkey)[1]): # [1]: get value count
                        print("  - {}".format(winreg.EnumValue(asubkey,j)[0]))

                        vdata = winreg.EnumValue(asubkey,j)[1]
                        
                        sil = pyfwsi.item_list()
                        # translate value data to Shell Item List formatted data
                        sil.copy_from_byte_stream(vdata, ascii_codepage='cp949')
                        print ("       #Value: " + str(sil.get_number_of_items()))
                        
        except WindowsError:
            pass
        
        
        
    
