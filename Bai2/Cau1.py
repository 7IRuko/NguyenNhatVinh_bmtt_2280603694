def tongchan(lst):
    tong = 0
    for n in lst:
        if n % 2 ==0:
            tong += n
    return tong
inputlist = input("Nhập danh sách các só, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, inputlist.split(',')))
tongsochan = tongchan(numbers)
print("Tong cac so chan trong list la : ",tongsochan)