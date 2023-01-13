from random import randint

def roll(): #주사위 돌리기 
    current_dice = int(randint(1,6)) #주사위 1부터 6까지 랜덤으로 뽑기 
    return current_dice   #돌렸을 때 나온 주사위 수를 반환 



def player():

  currentscore = 0 #현재 판의 점수
  choice = "y"  #게임을 계속 하겠다
  while choice == 'y':#플레이어의 선택이 게임을 계속하겠다고하면
    roll_num = roll() #주사위를 돌림

    if roll_num == 1 :#주사위가 1이 나오면
      print('숫자 1이 나왔습니다.')
      currentscore = 0 #현재 판의 점수는  0이 됨
      choice = "n" #이번판 끝

    else: #주사위 수가 1이 아닐때
      print(f'숫자는 {roll_num} 입니다.') #주사위 돌렸을 때 어떤 숫자 나왔는지 알려줌
      currentscore += roll_num  #현재 점수에 주사위 나온 숫자를 더함
      print(f'이번 판 점수는 현재  {currentscore} 입니다.')
      print(input('게임을 계속 하시겠습니까? y or n')) #게임을 계속 할건지 물어봄
  return currentscore


