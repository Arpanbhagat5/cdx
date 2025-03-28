# Given a string ‘str’ of digits and an integer ‘n’,
# build the lowest possible number by removing ‘n’ digits from the string
# and not changing the order of input digits.


def build_lowest_number(num:str, n:int)->int:
    if n==0:
        return num
    if len(num)==0:
        return num
    if len(num)<=n:
        return num
    stak = []
    for i in num:
        # remove top n max elements from the stack
        while n and stak and stak[-1] > i:
            stak.pop()
            n-=1
        stak.append(i)
    # if n is still remaining
    while n:
        stak.pop()
        n-=1
    ans = ''.join(stak)
    print(ans)
    return ans

build_lowest_number("98763",2)
build_lowest_number("129863",2)
build_lowest_number("123456",3)
build_lowest_number("11111",3)
build_lowest_number("11111",8)



