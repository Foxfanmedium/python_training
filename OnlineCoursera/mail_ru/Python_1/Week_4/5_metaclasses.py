# def dummy_factory():
#     class Class:
#         pass
#
#     return Class
#
# Dummy = dummy_factory()
#
# print(Dummy() is Dummy())

#===============================================

class Meta(type):
    def __new__(cls, name, parents, attrs):
        print('Creating {}'.format(name))

        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()

        return super().__new__(cls. name, parents, attrs)

class A(metaclass=Meta):
    pass





