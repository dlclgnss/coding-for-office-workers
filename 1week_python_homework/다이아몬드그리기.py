
# 10000
# 11000
# 11100
# 11110
# 11111

# for i in range(1,6):
#     print("1" *i + "0" * (5-i)) 


# 00100
# 01110
# 11111
# 01110
# 00100

for i in range(1,6):
    i = i-3
    if i < 0 :
        i = -i
    print("0"*i + "1"*(5-i*2) + "0" * i)