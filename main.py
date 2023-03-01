def print_tourney(player1, player2, winner):
  print(player1)
  print("---------- " + winner)
  space = ""
  difference = 10 - len(player2)
  for i in range(difference):
    space += " "
  print(player2 + space + "|----------")
  print("----------")


list = ["AJ", "Kyle", "Ryan", "Sam", "Justin", "Brandon", "Dan", "Elmer", "Laiken"]
print_tourney(list[0], list[1], "")
print("Who wins this round?")
flag = False
while not flag:
  winner = input(f"({list[0]}) or ({list[1]}): ")
  if winner.upper() == list[0].upper():
    flag = True
  if winner.upper() == list[1].upper():
    flag = True
flag = False
print("")
if winner.upper() == list[0].upper():
  print(list[0] + " Wins!")
  print_tourney(list[0], list[1], list[0])
else:
  print(list[1] + " Wins!")
  print_tourney(list[0], list[1], list[1])
