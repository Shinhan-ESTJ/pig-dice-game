from random import randint
computer_input = randint(0,1)

def roll_and_bank(currentscore):
  roll_num = randint(1,6)
  if roll_num !=1:
    currentscore += roll_num
    print(f"점수는 {roll_num}, 현재까지 당신의 점수는 {currentscore}입니다.")  
  else:
    currentscore = 0
    print(f"1이 나왔습니다.")  

  return currentscore
  

# 사용자 입력이 0이면 roll, 1이면 bank
total_score = 30 # 총합점수
currentscore = 0 # 임시점수
computer_input = 0

while computer_input == 0 :
  currentscore = roll_and_bank(currentscore)
  if currentscore != 0:
    computer_input = randint(0,1)
  else:
    total_score += currentscore
    print(f"1이 나와서 중단합니다. 당신의 점수는 {total_score} 입니다. 이제 상대방의 차례입니다.")
    break
  
if currentscore ==0:
  print("")
else:
  total_score += currentscore
  print(f"bank를 선택하셔서 이번판은 중단합니다. 당신의 점수는 {total_score}입니다.")


