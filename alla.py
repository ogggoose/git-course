numbers = [1,2,3,4,5,6,7,8,9,10]

def odd(list):
    for num in list:
        if num == 0:
            continue
        if num % 2 == 0:
            print(num)
odd([0,1,2,3,4,5])