def int_to_roman(num):
    numerical = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] 
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"] 
    i = 0
    while num > 0:
        for j in range(num // numerical[i]): 
            roman_num += romans[i] 
            num -= numerical[i]
        i += 1 
    return roman_num 

while True:
    n = int(input("Enter number: "))
    print("Roman form is, ", int_to_roman(n))
