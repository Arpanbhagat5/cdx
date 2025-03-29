# You are given an array of integers.
# Return an array of the same size where
# the element at each index is the product of all the elements in the original array
# except for the element at that index. For example, an input of [1, 2, 3, 4, 5]
# should return [120, 60, 40, 30, 24].
# You cannot use division in this problem.

def func(arr: list) -> list:
    arr_len = len(arr)
    
    left_multi = [1]*arr_len
    right_multi = [1]*arr_len
    result = [1]*arr_len
    
    for i in range(arr_len):
        if i == 0:
            pass
        else:
            left= i
            right = arr_len-left-1

            left_multi[left] = left_multi[left-1]*arr[left-1]
            right_multi[right] = right_multi[right+1]*arr[right+1]

    for i in range(arr_len):
        result[i] = left_multi[i]*right_multi[i]
    return result

print(func([1,2,3,4,5]))