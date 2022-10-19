hehe_file = open("hehe", "r")
#all the contents are stored in hehe_file variable

#print(hehe_file.readable())
#the above funtions tell us weather file is readable(boolean)
print(hehe_file.read())

hehe_file.close()
#the above closes the files


# Types of mod
# r = read = only want to read the info
# w = Write = change or write new info in it
# a = append = add new info(but we cant modify it)
# r+ = read and write
