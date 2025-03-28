# Given an array of distinct elements and a number x, find if there is a pair with product equal to x.

def pair_multi_check(arr: list, target: int) -> list:
    result = []
    mapper = {}
    
    for _,num in enumerate(arr):
        if result:
            break
        if target//num in arr:
            result.extend([num, target//num])
        mapper[num] = 1
    print(result)
    return result

# Test cases
pair_multi_check([10, 20, 9, 40], 400)
pair_multi_check([1,2,3,4,5,6,7,8,9], 10)
pair_multi_check([1,2,3,4,5,6,7,8,9], 12)
    

    