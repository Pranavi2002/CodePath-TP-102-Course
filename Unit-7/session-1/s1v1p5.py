def power_of_four(n):
    def power(x, exp):
        if exp == 0:
            return 1
        else:
            return x * power(x, exp - 1)
        return power(n, 4)

    # if n >= 0:
    #     return power(n, 4)
    # else:
    #     return 1 / power(-n, 4)

print(power_of_four(2))  
print(power_of_four(-2))
print(power_of_four(-3))
