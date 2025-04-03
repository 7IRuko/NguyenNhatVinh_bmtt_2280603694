def xoapt(dictionary,key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
mydic = {'a':1, 'b':2, 'c':3, 'd':4}
keytodel ='b'
result = xoapt (mydic,keytodel)
if result:
    print("Phan tu da duoc xoa tu Dictionary: ",mydic)
else:
    print("Ko tim thay pt can xoa trong dictionary: ")