def demso(l):
    countdict = {}
    for i in l:
        if i in countdict:
            countdict[i] +=1
        else:
            countdict[i] = 1
    return countdict
inputstring = input("Nhap danh sach cac tu, cach nhau bang dau cach: ")
listtu = inputstring.split()
solan = demso(listtu)
print("So lan xuat hien cua cac phan tu", solan)
