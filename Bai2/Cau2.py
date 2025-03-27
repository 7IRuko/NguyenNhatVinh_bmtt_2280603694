def daolist(lst):
    return lst[::-1]
inputlist = input("Nhap danh sach cac so, cach nhau bang dau phay : ")
n = list(map(int,inputlist.split(',')))
listdao = daolist(n)
print("List sau khi dao nguoc: ",listdao)