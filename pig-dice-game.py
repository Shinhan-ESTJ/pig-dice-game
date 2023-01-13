#변수명 변경 
#currentscore - > current_score
#roll_num -> current_dice

class Player():

  def __init__(self,total_score,current_score):
    self.current_score = current_score
    self.total_score = total_score
    
  def roll(self): #주사위 돌리기 
    current_dice = int(randint(1,6)) #주사위 1부터 6까지 랜덤으로 뽑기 
    return current_dice   #돌렸을 때 나온 주사위 수를 반환 

  def roll_and_back(self,current_dice): ##변경사항!!
    self.current_score = 0 #현재 판의 점수 
    choice = "y"  #게임을 계속 하겠다
    while choice == 'y':#플레이어의 선택이 게임을 계속하겠다고하면
       

      if current_dice == 1 :#주사위가 1이 나오면
        print('숫자 1이 나왔습니다.')
        self.current_score = 0 #현재 판의 점수는  0이 됨'
        self.total_score += self.current_score
        choice = "n" #이번판 끝 

      else: #주사위 수가 1이 아닐때
        print(f'숫자는 {current_dice} 입니다.') #주사위 돌렸을 때 어떤 숫자 나왔는지 알려줌
        self.current_score += current_dice  #현재 점수에 주사위 나온 숫자를 더함 
        print(f'이번 판 점수는 현재  {self.current_score} 입니다.')
        self.total_score += self.current_score
        print(input('게임을 계속 하시겠습니까? y or n : ')) #게임을 계속 할건지 물어봄
    return self.current_score

  


