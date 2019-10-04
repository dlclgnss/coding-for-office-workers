# 구현 내용

# 앞서 중간 점검 때 공부했던 구구단이 사용자가 어떤 다른 값을 넣더라도 에러가 나지 않도록 처리해 봅시다.
# (추가 과제에서 2~9라는 숫자 외에는 구구단이 출력하지 않도록 처리했습니다.)
# 예를 들어, 현재 숫자가 아닌 "1단"이라는 문자를 넣으면 구구단이 실행되지 않고 종료됩니다.
# 잘못된 값을 입력한 경우, "2에서 9사이의 숫자만 입력해주세요."이라는 문구와 함께 다시 구구단이 실행되도록 합시다.
# 힌트

# 에러 처리를 이용합니다.
# 함수 안에 동일한 함수를 다시 호출할 수 있습니다. 검색 키워드: 재귀 함수



# while True:
#     try:
#         num = int(input('몇 단을 출력 하시겠습니까'))
#         if num >1 and num < 10:
#             for i in range(2,10):
#                 print('{}x{}={}'.format(num,i,num*i))
#         else :
#             print('2에서 9사이의 숫자만 입력해주세요')
#     except:
#         print('숫자를 입력해주세요')
#         break;


    
def gugudan():
    try:
        num = int(input('몇 단을 출력 하시겠습니까'))
        if num >1 and num < 10:
            for i in range(2,10):
                print('{}x{}={}'.format(num,i,num*i))
        else :
                print('2에서 9사이의 숫자만 입력해주세요')
                gugudan()
    except:
        print('숫자를 입력해주세요')
        gugudan()


gugudan()