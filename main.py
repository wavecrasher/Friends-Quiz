# result dictionary
Characters = {
    "AAAAAAA" : "You are Chandler!",
    "AAAAAAB" : "You are Rachel!",
    "AAAAABB" : "You are Monica!",
    "AAAABBB" : "You are Chandler!",
    "AAABBBB" : "You are Ross!",
    "AABBBBB" : "You are Pheobe!",
    "ABBBBBB" : "You are Pheobe!",
    "ABABABA" : "You are Monica!",
    "BBBBBBB" : "You are Rachel!",
    "BAAAAAA" : "You are Joey!",
    "BBAAAAA" : "You are Rachel!",
    "BBBAAAA" : "You are Chandler!",
    "BBBBAAA" : "You are Pheobe! ",
    "BBBBBAA" : "You are Monica!",
    "BBBBBBA" : "You are Ross!",
    "BABABAB" : "You are Ross!"
}


print("Hello there, welcome to 'What is your Friends character?' quiz!")

name = input("What is your name? ")
print(f"Hi {name} are you ready to play? Y or N ? ")
print()
if answer.upper() == "Y":
  print("play game")
  q1 = input("What job better suits you? (Choose A or B) \nA) An office job \nB) Acting ")

  q2 = input("Are you messing or clean? (Choose A or B) \nA) I'm a slob! \nB) Super clean! ")

  q3 = input("Choose a hobby: (Choose A or B) \nA) Playing guitar in a coffe shop \nB) Dinasours ")

  q4 = input("Would you rather: (Choose A or B) \nA) Have Monica be your fitness trainer or \nA) Study Unagi ")

  q5 = input("Smelly Cats or Cooking? (Choose A or B) \nA) Smelly Cats! \nB) Cooking's my life!  ")

  q6 = input("Shopping or Eating? (Choose A or B) \nA) Shopping! \nB) Eating! ")

  q7 = input("Are you and only child or do you have siblings? (Choose A or B) \nA) Imma only! \n Siblings!  ")

  choice = q1 + q2 + q3 + q4 + q5 + q6 + q7

  wait = input("Would you like to know your Friends Character?:  ")

  if wait.upper() == "Y":
    print("Your Marvel Character is " + Characters[choice.upper()]) 
  else:
    print("Well that was a waste...")


else:
    print("Awe okay, maybe another time!")