def divide_by(first, second):
    try:
        return first / second
    # except:
    except ZeroDivisionError:
        return "0으로는 시스템상 나눌 수 없습니다."

print(divide_by(4,2))
print(divide_by(4,0))


#상속받기
class EvenNumberDevisionError(Exception):
    pass

def divide_by_odd_number(first, second):
    if second % 2 == 0:
        raise EvenNumberDevisionError 
    else:
        return first / second

print(divide_by_odd_number(6,3))
print(divide_by_odd_number(6,2))