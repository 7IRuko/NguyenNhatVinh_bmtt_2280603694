def phantu (tupdata):
    f_ele = tupdata[0]
    l_ele = tupdata[-1]
    return f_ele, l_ele
inputtup = eval(input("Nhap tuple, vd (1,2,3): "))
first, last = phantu(inputtup)
print("Phan tu dau tien: " , first)
print ("Phan tu cuoi cung: ",last)