
def sum_array(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum


numeros = list(range(1, 6))
print(sum_array(numeros))
