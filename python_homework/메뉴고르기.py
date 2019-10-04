import random

# 구현 내용

# 처음 파이썬 파일을 실행 시키면, 한식, 중식, 일식 중 한 가지를 고르라는 내용이 나옵니다.
# 그 중에서 한 가지를 고르면 식당 이름을 하나 임의로 추천해 줍니다.
# 힌트

# 리스트를 여러 개 사용하고 사용자의 입력을 받아야 합니다.





korea_food = ['비빔밥','삼겹살','곱창']
japan_food = ['스시','오코노미야키','돈카츠']
china_food = ['짜장면','탕수육','짱뽕']


select = input("한국,일본,중국 중 하나를 고르세요 : ")

if select == "한국" :
    choice_result = random.choice(korea_food)
elif select == "일본" :
    choice_result = random.choice(japan_food)
elif select  == "중국":
    choice_result = random.choice(china_food)
else:
    print('한국,중국,일본 중에서만 골라주세요')
    

if choice_result:
    print('{}메뉴의 {}을 선택하였습니다.'.format(select,choice_result))


