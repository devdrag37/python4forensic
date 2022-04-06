import pyregf

# Creating the object of pyregf.file
clsRegf = pyregf.file()

clsRegf.open(r"NTUSER.DAT")

# Key open from ROOT
key_console = clsRegf.get_key_by_path(r"Console")

# You will find class members of key_console by "help(class_variable)"

# Getting a number of VALUE
print ("VALUES #" + str(key_console.get_number_of_values()))

# Getting a number of sub-keys
print ("SUBKEY #" + str(key_console.get_number_of_sub_keys()))

# Getting value object of index 8
v0 = key_console.get_value(8)

# getting data from value object
#print "VALUE NAME: " + v0.get_name() + ", DATA: " + v0.get_data()

print ("VALUE NAME: " + v0.get_name())
print ("VALUE DATA: " + str(v0.get_data_as_integer()))

clsRegf.close()
