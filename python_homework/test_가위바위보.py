# 몇판 승부로 하실 건가요?
# (가위바위보) 중에서 선택해 주세요 
# 사용자 : xx 컴퓨터: xx
# xx가 이겼습니다.!
# 현재 전적은 x승x무x패 입니다.

# 컴퓨터와 대결에서 x승x무x패로 '결과' 하였습니다.

import random

while True:
    try:
        WIN_NUM = int(input('몇판 승부로 하실 건가요?'))
        break;
    except:
        print('숫자를 넣어 주세요!')
  
print('')
print('좋아요 승부를 시작합니다.')
print('')

result = ""
player_win = 0
computer_win = 0
draw = 0

while True:
    player = input('(가위 바위 보)중에 하나를 선택 해 주세요: ')
    number = random.randint(0,2)

    if number == 0:
        computer = '가위'
    elif number ==1:
        computer ='바위'
    else:
        computer = '보'
    
    print('사용자: ',player,'computer: ',computer)
    print('')

    if player == computer:
        print('비겼네요!')
        draw = draw+1

    if player == '가위':
        if computer == '보':
            print('당신이 이겼습니다!!')
            player_win = player_win+1
        elif computer == '바위':
            print('안타까워요! 컴퓨터가 이겼습니다!')
            computer_win = computer_win+1
    
    if player == '바위':
        if computer == '가위':
            print('당신이 이겼습니다!!')
            player_win = player_win+1
        elif computer == '보':
            print('으악! 컴퓨터가 이겼어요!')
            computer_win = computer_win+1

    
    if player == '보':
        if computer == '바위':
            print('당신이 이겼습니다!!')
            player_win = player_win+1
        elif computer == '가위':
            print('흑흑! 컴퓨터가 이겨버렸네요!')
            computer_win = computer_win+1

    print('')
    print('현재 전적은 {}승{}무{}패 중 입니다.'.format(player_win,draw,computer_win))    
    print('') 

    if player_win == WIN_NUM :
        result ='승리'
    elif computer_win == WIN_NUM:
        result ='패배'
    
    if player_win is WIN_NUM or computer_win is WIN_NUM:
        print('')
        print('컴퓨터와의 대결에서 {}승{}무{}패로 {} 하였습니다.'.format(player_win,draw,computer_win,result))
        break;




