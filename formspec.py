# https://docs.python.org/3/library/string.html#formatspec
# https://strftime.org/
import datetime

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
print(f"{big_num:_}")
# '1_234_567_890'
print(f"{big_num:,}")
# '1,234,567,890'

big_float = 2343552.6516251625
print(f'{big_float:,.3f}')
# '2,343,552.652'

# Time
now = datetime.datetime.utcnow()
print(f'{now:%F}')
# 2022-08-16
print(f'{now:%T}')
# 19:52:00
print(f'{now:%X}')
# 19:50:26
print(f'{now:%x}')
# 08/16/22

# Float
p = 0.4342105263157895
print(f'{p:%}')
# '43.421053%'
print(f'{p:.2%}')
# '43.42%'


# Add leading zeros
number = 123
print(f"{number:08}")
# 00000123


# f"{some_obj!r}"
# - __repr__

