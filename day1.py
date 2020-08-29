


def find_pair_brute(list_num, num):
    for i in range(len(list_num)):
        for j in range(i, len(list_num)):
            if list_num[i]+ list_num[j] == num:
                print(list_num[i], list_num[j])
                return True
    return False


def find_pair_hash(list_num, num):
    dict_of_num = {}
    for i in list_num:
        if num-i in dict_of_num:
            print(i,num-i)
            return True
        else:
            dict_of_num[i]= True
    return False


def find_pair_sort(list_num, num):
    list_num.sort()
    left_ptr = 0
    right_ptr = len(list_num)-1
    while True:
        if left_ptr==right_ptr:
            break

        if list_num[left_ptr] + list_num[right_ptr] > num:
            right_ptr-=1

        elif list_num[left_ptr] + list_num[right_ptr] < num:
            left_ptr+=1

        else:
            # if list_num[left_ptr] + list_num[right_ptr] == num:
            print(list_num[left_ptr] , list_num[right_ptr])
            return True
    return False


list_num1 = [1,3,4,6,2,-1,5,6,14]
list_num2 = [1,9,6,2,-1,5,6,1,-9,15]
num = 13
dict_of_fun = {"find_pair_brute": find_pair_brute, "find_pair_hash": find_pair_hash, "find_pair_sort": find_pair_sort}

for fun in dict_of_fun:
    print('#####',fun,'#####')
    print("list_num1",list_num1)
    print(dict_of_fun[fun](list_num1, num))

    print("list_num2", list_num2)
    print(dict_of_fun[fun](list_num2, num))
    print("\n")
