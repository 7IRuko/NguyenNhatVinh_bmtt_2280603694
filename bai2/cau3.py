def tao_tuple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhap danh sach cac so: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("list: ", numbers)
print("tuple tuwf list: ", my_tuple)