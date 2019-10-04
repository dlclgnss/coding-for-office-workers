# # 구현 내용

# # 사용자에게 가위, 바위, 보 중 하나를 물어봅니다.
# # 사용자가 가위, 바위, 보를 고르면, 컴퓨터도 같이 가위, 바위, 보를 내고 승패를 가릅니다.
# # 다합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝이 납니다.
# # 힌트

# # 리스트를 한 개를 사용하고 사용자의 입력을 받아야 합니다.
# # 앞서 사용했던 임의 뽑기를 다시 사용합니다. 검색 키워드 : random, randint, shuffle
# # 컴퓨터에게 가위, 바위, 보의 승패를 가르쳐줘야 합니다.
# # 마감시간

# # 필수 과제가 아닙니다.


import random 

while True:
    try:
        MAX_NUM = int(input('몇승 승부로 할 것인가요?'))
        break;
    except:
        print('숫자로 입력해주세요')

draw = 0
player_win = 0
computer_win = 0
result = ""

while True:
    player = input("\n(가위, 바위, 보) 중에서 하나를 선택하세요: ")
    number = random.randint(0,2)
    
    if number == 0:
        computer = "가위";
    elif number == 1:
        computer = "바위";
    else:
        computer = "보";

    print('플레이어: ',player ,'컴퓨터: ',computer)

    try:
        if player == computer:
            print('비겼네요!')
            draw = draw+1
        
        if player == "가위":
            if computer =="보":
                print('플레이어 이겼음!')
                player_win = player_win+1
            elif computer == "바위":
                print('컴퓨터 이겼음!')
                computer_win = computer_win+1
        
        if player == "바위":
            if computer =="가위":
                print('플레이어 이겼음!')
                player_win = player_win+1
            elif computer == "보":
                print('컴퓨터 이겼음!')
                computer_win = computer_win+1

        
        if player == "보":
            if computer =="바위":
                print('플레이어 이겼음!')
                player_win = player_win+1
            elif computer == "가위":
                print('컴퓨터 이겼음!')
                computer_win = computer_win+1

    except:
        print('올바른 형식으로 입력해 주세요')
    if player_win is MAX_NUM or computer_win is MAX_NUM :
        break;
    print('전적은 {}승{}패 {}무 입니다.'.format(player_win,computer_win,draw,))
    
if player_win is MAX_NUM :
    result = '승리'
else :
    result = '패배'

print('컴퓨터와 대결에서 {}승{}무{}패로{}하셨습니다.'.format(player_win,draw,computer_win,result))