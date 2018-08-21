# Доступ к объекту исключения

# try:
#     with open("/file/not/found") as f:
#         content = f.read()
#
# except OSError as err:
#     print(err.errno, err.strerror)

#===============================================

# Доступ к объекту исключения, атрибут args

# import os.path
#
# filename = "/file/not/found"
# try:
#     if not os.path.exist(filename):
#         raise ValueError("file doesn't exist", filename)
# except ValueError as err:
#     message, filename = err.args[0], err.args[1]
#     print(message, code)

#===============================================

# Доступ к traceback

# import traceback
#
# try:
#     with open("/file/not/found") as f:
#         content = f.read()
#
# except OSError as err:
#     trace = traceback.print_exc()
#     print(trace)

#===============================================

# Генерация исключения, инструкция raise

# try:
#     raw = input("insert number: ")
#     if not raw.isdigit():
#         raise ValueError
# except ValueError:
#     print("incorrect value")


# try:
#     raw = input("insert number: ")
#     if not raw.isdigit():
#         raise ValueError("bad number", raw)
# except ValueError as err:
#     print("incorrect value", err)

#===============================================

# Проброс исключений выше

# try:
#     raw = input("insert number: ")
#     if not raw.isdigit():
#         raise ValueError("bad number", raw)
# except ValueError as err:
#     print("incorrect value!", err)
#     # длкгирование обработки исключения - используем raise без параметров
#     raise

# Исключение через raise from Exception

# try:
#     raw = input("insert number: ")
#
#     if not raw.isdigit():
#         raise ValueError("bad number, raw")
# except ValueError as err:
#     print("error:", err.args[0], err.args[1])
#
#     raise TypeError("error") from err

# Инструкция assert

# assert True

# assert 1 == 0

# assert 1 == 0, '1 is not equal 0'

# Инструкция assert, флаг -O
#
# def get_user_by_id(id):
#     assert isinstance(id, int), "id has to be integer"
#
#     print("the search is made")
#
#
# if __name__ == "__name":
#     get_user_by_id("foo")


# Производительность исключений

# %% timeit
#
# my_dict = {"foo": 1}
# for _ in range(100):
#     try:
#         my_dict["bar"]
#     except KeyError:
#         pass

#
# my_dict = {"foo": 1}
# for _ in range(100):
#     if _ in range(100):
#         if "bar" in my_dict:
#             _ = my_dict["bar"]









