def taotuple(l):
    return tuple(l)
inputlist =  input("Nhap danh sach cac so, cach nhau bang dau phay: ")
n = list(map(int, inputlist.split(',')))
mytup = taotuple (n)
print ("List: ",n)
print ("Tuple tu List: ", mytup)