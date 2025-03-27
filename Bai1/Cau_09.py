def ktsont(n):
    if n<=1:
        return False
    for i in range(2,int (n**0.5)+1):
        if n%i==0:
            return False
    return True
num = int(input("Nhập vào số cần ktra: "))
if ktsont(num):
    print(num,"là số nguyên tố.")
else:
    print(num,"ko phải là số nguyên tố")