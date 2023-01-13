class Computer:

  def __init__(self, total_score, current_score):
    self.computer_input = randint(0,1)
    self.total_score = total_score
    self.current_score = current_score

  def roll_and_back(self):
    current_dice = randint(1,6)
    if current_dice !=1:
      self.current_score += current_dice
      print(f"점수는 {current_dice}, 현재까지 당신의 점수는 {self.current_score}입니다.")  
    else:
      self.current_score = 0
      print(f"1이 나왔습니다.")  

    return self.current_score
    
computer_total_score = 0
computer_current_score = 0 
player_total_score = 0
player_current_score = 0 
player1_info = [computer,0]
player2_info = [player,0]

while (computer_total_score < 50) & (player_total_score < 50):
  computer = Computer(computer_total_score, computer_current_score)
  while computer.computer_input == 0 :
    computer.current_score = roll_and_back(computer.current_score)
    if computer.current_score != 0:
      computer.computer_input = randint(0,1)
    else:
      computer.total_score += computer.current_score
      print(f"1이 나와서 중단합니다. 당신의 점수는 {computer.total_score} 입니다. 이제 상대방의 차례입니다.")
      break
  if computer.current_score ==0:
    print("")
  else:
    computer.total_score += computer.current_score
    print(f"bank를 선택하셔서 이번판은 중단합니다. 당신의 점수는 {computer.total_score}입니다.")
    
    computer_total_score = computer.total_score
    player1_info[1] = computer_total_score

    
print(f"누가이겼습니")


