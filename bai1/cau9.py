def kt_SNT(n):
    if n <= 1:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % 1 == 0:
            return 0
        return 1
number = int(input("nhap vao so can kiem tra: "))
if kt_SNT(number):
    print(number, "la SNT")
else:
    print(number, "Khong phai la SNT.")
