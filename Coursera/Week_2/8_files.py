# f = open('filename')
# text_modes = ['r', 'w', 'a', 'r+']
# binary_modes = ['br', 'bw', 'ba', 'br+']
#=====================================================================================================================
# f = open('filename', 'w') # Open fiel with writting mode
# f.write('The world is changed. \n I taste it in the water. \n')
# f.close() # obligatory action after openning a file
#
# f = open('filename', 'r+')
# f.read()
#
# f.tell()    # >>> 47 - we have read the file and our pointer in the end of file
#=====================================================================================================================
# f.seek(0)
# f.tell() # >>> 0 - we ave just returned to the begining of our file
# print(f.read())
# f.close()
#=====================================================================================================================
f = open('filename', 'r+')
f.readline() # reading of one line only
f.close()

f = open('filename', 'r+')
f.readlines() # >>> ['The world is changed. \n', 'I taste it in the water. \n']

with open('filename', 'r+') as f:
    print(f.read())










