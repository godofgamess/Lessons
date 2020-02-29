from school import get_int
from sys import exit

num = get_int('Enter number: ', force=True)

digits = ['zero', 'one', 'two', 'three', 'four', 'five',
          'six', 'seven', 'eight', 'nine']

teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
         'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['ten', 'twenty', 'thirty', 'fourty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety']


if 0 <= num <= 9:
    print(digits[num])

elif 11 <= num <= 19:
    print(teens[num-11])

elif 10 <= num <= 90 and num % 10 == 0:
    print(tens[num // 10 - 1])

elif 100 <= num <= 900 and num % 100 == 0:
    print(digits[num // 100], 'hundred')

elif 20 < num < 100:
    first, second = int(str(num)[0]), int(str(num)[1])
    print(tens[first-1], digits[second])

elif 100 < num < 1000:
    first, second, third = int(str(num)[0]), int(str(num)[1]), int(str(num)[2])
    if 11 <= int(str(second) + str(third)) <= 19:
        print(digits[first], 'hundred', teens[int(str(second) + str(third)) - 11])
    elif second != 0:
        print(digits[first], 'hundred', tens[second-1], digits[third])
    else:
        print(digits[first], 'hundred', digits[third])
