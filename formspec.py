# https://docs.python.org/3/library/string.html#formatspec

text = "hello world"

# Center text:
print(f"{text:^15}")
# '  hello world  '

print(f"{text:*^15}")
# '**hello world**'

f"{text:*<15}"
# '*hello world****'

big_num = 1234567890
# Set separator
print(f"{number:_}")
# '1_234_567_890'
print(f"{number:,}")
# '1,234,567,890'

float_num = 2343552.6516251625
print(f'{float_num:,.3f}')
# '2,343,552.652'


0.4342105263157895
f'{p:%}'
# '43.421053%'
f'{p:.2%}'
# '43.42%'



number = 123
# Add leading zeros
print(f"{number:08}")
# 00000123


f"{some_obj!r}" 
#- __repr__
