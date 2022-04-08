import sys
from datetime import datetime
import winreg
import pyfwsi

#######################################
'''
  STEP 4: Print out all of information in shell items
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
    - Code related to shell item
      > https://plaso.readthedocs.io/en/latest/_modules/plaso/parsers/shared/shell_items.html
'''



with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkcu:
    with winreg.OpenKey(hkcu, r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU") as targetkey:
            for i in range(0, winreg.QueryInfoKey(targetkey)[0]): # [0]: get key count
                asubkeyname = winreg.EnumKey(targetkey, i)
                print(asubkeyname)

                with winreg.OpenKey(targetkey, asubkeyname) as asubkey:
                    for j in range(0, winreg.QueryInfoKey(asubkey)[1]): # [1]: get value count
                        print("  - {}".format(winreg.EnumValue(asubkey,j)[0]))

                        vdata = winreg.EnumValue(asubkey,j)[1]
                        
                        sil = pyfwsi.item_list()
                        # translate value data to Shell Item List formatted data
                        try:
                            sil.copy_from_byte_stream(vdata, ascii_codepage='cp949')
                        except:
                            continue
                            
                        print ("#COUNT: " + str(sil.get_number_of_items()))

                        for shell_item in iter(sil.items):
                            #shell_item : file_entry, root_folder, volume, ...
                            #shell_item may include extension_block
                            if isinstance(shell_item, pyfwsi.file_entry):
                                print ("       File Entry ITEM(Name)   : " + shell_item.get_name())
                                print ("         - size: " + str(shell_item.get_file_size()))

                                for extension_block in shell_item.extension_blocks:
                                    # file_entry_extension: base class - extension_block
                                    if isinstance(extension_block, pyfwsi.file_entry_extension):
                                        print("         - long name: " + extension_block.long_name)
                                        if extension_block.get_access_time_as_integer():# skip if zero
                                            print("         - atime: " + str(extension_block.get_access_time()))
                                        if extension_block.get_creation_time_as_integer(): # skip if zero
                                            print("         - ctime: " + str(extension_block.get_creation_time()))
                                if (shell_item.get_modification_time_as_integer()): # skip if zero
                                    print ("         - mtime: " + str(shell_item.get_modification_time()))
                            elif isinstance(shell_item, pyfwsi.network_location):
                                print ("       Network Location ITEM(Location): " + shell_item.get_location())
                            elif isinstance(shell_item, pyfwsi.volume):
                                print ("       volume ITEM(Volume Name): " + str(shell_item.get_name()))                            
                            #elif isinstance(shell_item, pyfwsi.root_folder):
                            #    print ("       Root Folder ITEM")
        
        
        
    
