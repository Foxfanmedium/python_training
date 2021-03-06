# try:
#     with open('file.txt', 'r') as fh:
#         file_data = fh.read()
#     print(file_data)
# except FileNotFoundError:
#     print('The data file is missing.')
# except PermissionError:
#     print('This is not allowed.')
# except:
#     print('Some other error occurred')
# import sys
# try:
#     1/0
# except:
#     err = sys.exc_info()
#     for e in err:
#         print(e)


try:
    with open('file.txt', 'r') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing.')
except PermissionError:
    print('This is not allowed.')
except Exception as err:
    print('Some other error occurred', str(err))
