#******************************************************************************************************************************************
import pyttsx3
import random
engine = pyttsx3.init()
engine.say("Welcome To Tic Tac Toe Game")
engine.runAndWait()
print("Welcome to Tic-Tac-Toe Game!\n")


print(" X  |  O   | O  ")
print("--------------")
print("  O  |  X  |   ")
print("--------------")
print("  O  |  O  | X \n")

print("X wins!")

print("\n Enter 0 to quit anytime")
engine.say("Enter 0 to quit anytime")
engine.say("If you want to play with computer enter 1 if you want play with your friend enter 2")
engine.runAndWait()


#******************************************************************************************************************************************

user_choice = int(input("\nIf you want to play with computer enter (1) if you want to play \
with your friend enter (2) : "))

#******************************************************************************************************************************************

if user_choice == 2:

  class Board:
    
    engine.say("Can I know your name player 1: ")
    engine.runAndWait()
    
    name1 = input("\nPlayer 1 What is your name: ")
    engine.say("Can I know your name player 2")
    engine.runAndWait()             
    name2 = input("\nPlayer 2 What is your name: ")
    

#******************************************************************************************************************************************
    def __init__(self):
      self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]

#******************************************************************************************************************************************

    def display(self):
        print("\n%s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print("----------")
        print("%s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("----------")
        print("%s | %s | %s \n" % (self.cells[7], self.cells[8], self.cells[9]))


#******************************************************************************************************************************************
    def print_header(self):
      print(f"\nWelcome to Tic-Tac-Toe Game {self.name1}\n")
      engine.say("Welcome to tic tac toe game")
      engine.say(self.name1)
      engine.runAndWait()
      
 #******************************************************************************************************************************************
   
      print(f"Welcome to Tic-Tac-Toe Game {self.name2}\n")
      engine.say("Welcome to tic tac toe game")
      engine.say(self.name2)
      engine.runAndWait()
      
      
#******************************************************************************************************************************************     
#******************************************************************************************************************************************

    def winner_123(self, player):
      if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
        print(f"\n{player} wins!")

        play_again = input(f"\n Did you want to play again {self.name2} and {self.name1} (yes/no) ?: ")
        if play_again == 'no':
          print(f"Thanks for playing {self.name1} and {self.name2}")
          return False
        elif play_again == "yes":
          print("\nResetting the board....")
          self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]

 #******************************************************************************************************************************************
    def Winner_456(self, player):
        if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
          print(f"\n{player} wins!")
          play_again = input(f"\n Did you want to play again {self.name2} and {self.name1} (yes/no) ?: ")
          if play_again == 'no':
            print(f"Thanks for playing {self.name1} and {self.name2}")
            return False
          elif play_again == "yes":
            print("\nResetting the board....")
            self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]

#******************************************************************************************************************************************
    def winner_789(self, player):
        if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
          print(f"\n{player} wins!")
          play_again = input(f"\n Did you want to play again {self.name2} and {self.name1} (yes/no) ?: ")
          if play_again == 'no':
            print(f"Thanks for playing {self.name1} and {self.name2}")
            return False
          elif play_again == "yes":
            print("\nResetting the board....")
            self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]

#******************************************************************************************************************************************
    def winner_147(self, player):
        if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
          print(f"\n{player} wins!")
          play_again = input(f"\n Did you want to play again {self.name2} and {self.name1} (yes/no) ?: ")
          if play_again == 'no':
            print(f"Thanks for playing {self.name1} and {self.name2}")
            return False
          elif play_again == "yes":
            print("\nResetting the board....")
            self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]


#******************************************************************************************************************************************

    def winner_258(self, player):
        if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
          print(f"\n{player} wins!")
          play_again = input(f"\n Did you want to play again {self.name2} and {self.name1} (yes/no) ?: ")
          if play_again == 'no':
            print(f"Thanks for playing {self.name1} and {self.name2}")
            return False
          elif play_again == "yes":
            print("\nResetting the board....")
            self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]

#******************************************************************************************************************************************

    def winner_369(self, player):
        if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
          print(f"\n{player} wins!")
          play_again = input(f"\n Did you want to play again {self.name2} and {self.name1} (yes/no) ?: ")
          if play_again == 'no':
            print(f"Thanks for playing {self.name1} and {self.name2}")
            return False
          elif play_again == "yes":
            print("\nResetting the board....")
            self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]

#******************************************************************************************************************************************

    def winner_159(self, player):
        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
          print(f"\n{player} wins!")
          play_again = input(f"\n Did you want to play again {self.name2} and {self.name1} (yes/no) ?: ")
          if play_again == 'no':
            print(f"Thanks for playing {self.name1} and {self.name2}")
            return False
          elif play_again == "yes":
            print("\nResetting the board....")
            self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]

#******************************************************************************************************************************************

    def winner_357(self, player):
        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
          print(f"\n{player} wins!")
          play_again = input(f"\n Did you want to play again {self.name2} and {self.name1} (yes/no) ?: ")
          if play_again == 'no':
            print(f"Thanks for playing {self.name1} and {self.name2}")
            return False
          elif play_again == "yes":
            print("\nResetting the board....")
            self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]


#******************************************************************************************************************************************


    def Tie_game(self):
      used_cells = 0
      for i in self.cells:
        if i != " ":
          used_cells += 1
      if used_cells == 9:
        print("We have a Tie\n")
        play_again = input(f"Did you want to want to play again {self.name1} and {self.name2} (yes/no) ?: ")
        if play_again == 'yes':
          self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]

        elif play_again == 'no':
          print(f"Thanks for playing {self.name1} and {self.name2}")
          return False



#******************************************************************************************************************************************
        if play_again == "yes":
          print("\nResetting the board....")
          self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]
        else:
          print(f"Thanks for playing our game {self.name1} and {self.name2}")
          print("Enter 0 to quit")

#******************************************************************************************************************************************

  board = Board()
  board.print_header()
  board.display()

#******************************************************************************************************************************************
  while True:
    while True:
        player1 = int(input("\nPlease Choose X  1-9: "))
        if player1 == 0:
          break
        
        elif board.cells[player1] != " ":
          
          print(f"\nYou can't go there {board.name1}")
          print(f"\n Please enter correct number {board.name1}")
          
        else:
          board.cells[player1] = "X"
          break
        
    board.display()
#******************************************************************************************************************************************
    win_123 = board.winner_123("X")
    if win_123 == False:
      break

#******************************************************************************************************************************************
    win_456 = board.Winner_456("X")
    if win_456 == False:
      break
#******************************************************************************************************************************************
    win_789 = board.winner_789("X")
    if win_789 == False:
      break
#******************************************************************************************************************************************
    win_147 = board.winner_147("X")
    if win_147 == False:
      break
#******************************************************************************************************************************************
    win_258 = board.winner_258("X")
    if win_258 == False:
      break
#******************************************************************************************************************************************
    winner_369 = board.winner_369("X")
    if winner_369 == False:
      break
#******************************************************************************************************************************************
    win_357 = board.winner_357("X")
    if win_357 == False:
      break
#******************************************************************************************************************************************
    win_159 = board.winner_159("X")
    if win_159 == False:
      break
#******************************************************************************************************************************************
    tie = board.Tie_game()
    if tie == False:
      break

#******************************************************************************************************************************************
    while True:
        player2 = int(input("\nPlease Choose X  1-9: "))
        if player2 == 0:
          break
        
        elif board.cells[player2] != " ":
          
          print(f"\nYou can't go there {board.name2}")
          print(f"\n Please enter correct number {board.name2}")
          
        else:
          board.cells[player1] = "O"
          break
        
    
    board.display()
#******************************************************************************************************************************************
    win_123 = board.winner_123("O")
    if win_123 == False:
      break
#******************************************************************************************************************************************
    win_456 = board.Winner_456("O")
    if win_456 == False:
      break
#******************************************************************************************************************************************
    win_789 = board.winner_789("O")
    if win_789 == False:
      break

#******************************************************************************************************************************************
    win_147 = board.winner_147("O")
    if win_147 == False:
      break
#******************************************************************************************************************************************
    win_258 = board.winner_258("O")
    if win_258 == False:
      break
#******************************************************************************************************************************************
    win_369 = board.winner_369("O")
    if win_369 == False:
      break
#******************************************************************************************************************************************
    win_357 = board.winner_357("O")
    if win_357 == False:
      break
#******************************************************************************************************************************************
    win_159 = board.winner_159("O")
    if win_159 == False:
      break
#******************************************************************************************************************************************
    tie = board.Tie_game()
    if tie == False:
      break

#******************************************************************************************************************************************
#******************************************************************************************************************************************

else:
    class Board:

  #******************************************************************************************************************************************
      def __init__(self):
        self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]
        self.name1 = input("\nPlayer1 What is your name: ")
        self.user_x_o = input("\nWhat is your choice X or O ? : ")
        if self.user_x_o == "X" or self.user_x_o == "x":
          self.comp = "O"
        else:
          self.comp = "X"

  #******************************************************************************************************************************************

      def display(self):
          print("\n%s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
          print("----------")
          print("%s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
          print("----------")
          print("%s | %s | %s \n" % (self.cells[7], self.cells[8], self.cells[9]))

  #******************************************************************************************************************************************

      def update_cell(self, cell_no, player_i):
          if self.cells[cell_no] == " ":
            self.cells[cell_no] = player_i


  #******************************************************************************************************************************************
      def print_header(self):
        print(f"\nWelcome to Tic-Tac-Toe Game {self.name1}\n")

  #******************************************************************************************************************************************

      def winner_123(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
          print(f"\n{player} wins!")

          play_again = input(f"\n Did you want to play again {self.name1} (yes/no) ?: ")
          if play_again == 'no':
            print(f"Thanks for playing {self.name1}")
            return False
          elif play_again == "yes":
            print("\nResetting the board....")
            self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]

  #******************************************************************************************************************************************
      def Winner_456(self, player):
          if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            print(f"\n{player} wins!")
            play_again = input(f"\n Did you want to play again {self.name1} (yes/no) ?: ")
            if play_again == 'no':
              print(f"Thanks for playing {self.name1}")
              return False
            elif play_again == "yes":
              print("\nResetting the board....")
              self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]

  #******************************************************************************************************************************************
      def winner_789(self, player):
          if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            print(f"\n{player} wins!")
            play_again = input(f"\n Did you want to play again {self.name1} (yes/no) ?: ")
            if play_again == 'no':
              print(f"Thanks for playing {self.name1}")
              return False
            elif play_again == "yes":
              print("\nResetting the board....")
              self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]

  #******************************************************************************************************************************************
      def winner_147(self, player):
          if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            print(f"\n{player} wins!")
            play_again = input(f"\n Did you want to play again {self.name1} (yes/no) ?: ")
            if play_again == 'no':
              print(f"Thanks for playing {self.name1}")
              return False
            elif play_again == "yes":
              print("\nResetting the board....")
              self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]


  #******************************************************************************************************************************************

      def winner_258(self, player):
          if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            print(f"\n{player} wins!")
            play_again = input(f"\n Did you want to play again {self.name1} (yes/no) ?: ")
            if play_again == 'no':
              print(f"Thanks for playing {self.name1}")
              return False
            elif play_again == "yes":
              print("\nResetting the board....")
              self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]

  #******************************************************************************************************************************************

      def winner_369(self, player):
          if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            print(f"\n{player} wins!")
            play_again = input(f"\n Did you want to play again {self.name1} (yes/no) ?: ")
            if play_again == 'no':
              print(f"Thanks for playing {self.name1}")
              return False
            elif play_again == "yes":
              print("\nResetting the board....")
              self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]

  #******************************************************************************************************************************************

      def winner_159(self, player):
          if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            print(f"\n{player} wins!")
            play_again = input(f"\n Did you want to play again {self.name1} (yes/no) ?: ")
            if play_again == 'no':
              print(f"Thanks for playing {self.name1}")
              return False
            elif play_again == "yes":
              print("\nResetting the board....")
              self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]

  #******************************************************************************************************************************************

      def winner_357(self, player):
          if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            print(f"\n{player} wins!")
            play_again = input(f"\n Did you want to play again {self.name1} (yes/no) ?: ")
            if play_again == 'no':
              print(f"Thanks for playing {self.name1}")
              return False
            elif play_again == "yes":
              print("\nResetting the board....")
              self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]


  #******************************************************************************************************************************************


      def Tie_game(self):
        used_cells = 0
        for i in self.cells:
          if i != " ":
            used_cells += 1
        if used_cells == 9:
          print("We have a Tie\n")
          play_again = input(f"Did you want to want to play again {self.name1} (yes/no) ?: ")

  #******************************************************************************************************************************************
          if play_again == "yes":
            print("\nResetting the board....")
            self.cells = [" ", " ", " "," "," "," "," "," "," ", " "]
          else:
            print(f"Thanks for playing our game {self.name1}")
            return False

  #******************************************************************************************************************************************

    board = Board()
    board.print_header()
    board.display()
    

  #******************************************************************************************************************************************
    while True:
      while True:
        player1 = int(input(f"\nPlease Choose {board.user_x_o} 1-9: "))
        if player1 == 0:
          break
        
        elif board.cells[player1] != " ":
          
          print("\nYou can't go there")
          print("\n Please enter correct number")
          
        else:
          board.cells[player1] = board.user_x_o
          break
          
      board.display()
  #******************************************************************************************************************************************
      win_123 = board.winner_123(board.user_x_o)
      if win_123 == False:
        break

  #******************************************************************************************************************************************
      win_456 = board.Winner_456(board.user_x_o)
      if win_456 == False:
        break
  #******************************************************************************************************************************************
      win_789 = board.winner_789(board.user_x_o)
      if win_789 == False:
        break
  #******************************************************************************************************************************************
      win_147 = board.winner_147(board.user_x_o)
      if win_147 == False:
        break
  #******************************************************************************************************************************************
      win_258 = board.winner_258(board.user_x_o)
      if win_258 == False:
        break
  #******************************************************************************************************************************************
      winner_369 = board.winner_369(board.user_x_o)
      if winner_369 == False:
        break
  #******************************************************************************************************************************************
      win_357 = board.winner_357(board.user_x_o)
      if win_357 == False:
        break
  #******************************************************************************************************************************************
      win_159 = board.winner_159(board.user_x_o)
      if win_159 == False:
        break
  #******************************************************************************************************************************************
      tie = board.Tie_game()
      if tie ==  False:
        break

  #******************************************************************************************************************************************
  #******************************************************************************************************************************************
      while True:
        if board.cells[3] == board.comp and board.cells[2] == board.comp:
          if board.cells[1] == " ":
            board.cells[1] = board.comp
            break
 #****************************************************************************************************************************************** 
        if board.cells[1] == board.comp and board.cells[2] == board.comp:
          if board.cells[3] == " ":
            board.cells[3] = board.comp
            break
  
 #****************************************************************************************************************************************** 
        if board.cells[1] == board.comp and board.cells[3] == board.comp:
          if board.cells[2] == " ":
            board.cells[2] = board.comp
            break
#******************************************************************************************************************************************  
          
        if board.cells[5] == board.comp and board.cells[6] == board.comp:
          if board.cells[4] == " ":
            board.cells[4] = board.comp
            break
  
#******************************************************************************************************************************************  
        if board.cells[4] == board.comp and board.cells[5] == board.comp:
          if board.cells[6] == " ":
            board.cells[6] = board.comp
            break
  
#******************************************************************************************************************************************

        if board.cells[4] == board.comp and board.cells[6] == board.comp:
          if board.cells[5] == " ":
           board.cells[5] = board.comp
           break
  
 #******************************************************************************************************************************************         
        if board.cells[8] == board.comp and board.cells[9] == board.comp:
          if board.cells[7] == " ":
            board.cells[7] = board.comp
            break
#******************************************************************************************************************************************
  
        if board.cells[7] == board.comp and board.cells[8] == board.comp:
          if board.cells[9] == " ":
            board.cells[9] = board.comp
            break
#******************************************************************************************************************************************
  
        if board.cells[7] == board.comp and board.cells[8] == board.comp:
          if board.cells[9] == " ":
            board.cells[9] = board.comp
            break

#******************************************************************************************************************************************
        
        if board.cells[4] == board.comp and board.cells[7] == board.comp:
          if board.cells[1] == " ":
            board.cells[1] = board.comp
            break
          
#******************************************************************************************************************************************
  
        if board.cells[1] == board.comp and board.cells[4] == board.comp:
          if board.cells[7] == " ":
            board.cells[7] = board.comp
            break
          
#****************************************************************************************************************************************** 
  
        if board.cells[1] == board.comp and board.cells[7] == board.comp:
          if board.cells[4] == " ":
            board.cells[4] = board.comp
            break
          
 #****************************************************************************************************************************************** 
  
        if board.cells[5] == board.comp and board.cells[8] == board.comp:
          if board.cells[2] == " ":
            board.cells[2] = board.comp
            break
  
 #******************************************************************************************************************************************         
        if board.cells[2] == board.comp and board.cells[5] == board.comp:
          if board.cells[8] == " ":
            board.cells[8] = board.comp
            break
#******************************************************************************************************************************************
  
        if board.cells[2] == board.comp and board.cells[8] == board.comp:
          if board.cells[5] == " ":
            board.cells[5] = board.comp
            break
  
#******************************************************************************************************************************************
        if board.cells[3] == board.comp and board.cells[6] == board.comp:
          if board.cells[9] == " ":
            board.cells[9] = board.comp
            break
  
#****************************************************************************************************************************************** 
        if board.cells[3] == board.comp and board.cells[9] == board.comp:
          if board.cells[6] == " ":
            board.cells[6] = board.comp
            break
#******************************************************************************************************************************************
          
        if board.cells[6] == board.comp and board.cells[9] == board.comp:
          if board.cells[3] == " ":
            board.cells[3] = board.comp
            break
#******************************************************************************************************************************************
          
        if board.cells[9] == board.comp and board.cells[5] == board.comp:
          if board.cells[1] == " ":
            board.cells[1] = board.comp
            break
  
 #******************************************************************************************************************************************         
        if board.cells[1] == board.comp and board.cells[5] == board.comp:
          if board.cells[9] == " ":
            board.cells[9] = board.comp
            break
  
#******************************************************************************************************************************************
        if board.cells[1] == board.comp and board.cells[9] == board.comp:
          if board.cells[5] == " ":
            board.cells[5] = board.comp
            break
          

#******************************************************************************************************************************************         
        if board.cells[3] == board.comp and board.cells[5] == board.comp:
          if board.cells[7] == " ":
            board.cells[7] = board.comp
            break
  
#******************************************************************************************************************************************
        
        if board.cells[3] == board.comp and board.cells[7] == board.comp:
          if board.cells[5] == " ":
            board.cells[5] = board.comp
            break
  
#******************************************************************************************************************************************

        if board.cells[7] == board.comp and board.cells[5] == board.comp:
          if board.cells[3] == " ":
            board.cells[3] = board.comp
            break
  
      
#******************************************************************************************************************************************
      
        if board.cells[1] == board.user_x_o and board.cells[2] == board.user_x_o:
          if board.cells[3] == " ":
            board.cells[3] = board.comp
            break
  
 #****************************************************************************************************************************************** 
        if board.cells[1] == board.user_x_o and board.cells[3] == board.user_x_o:
          if board.cells[2] == " ":
            board.cells[2] = board.comp
            break
  
 #******************************************************************************************************************************************
  
        if board.cells[3] == board.user_x_o and board.cells[2] == board.user_x_o:
          if board.cells[1] == " ":
            board.cells[1] = board.comp
            break
  
#******************************************************************************************************************************************

        if board.cells[4] == board.user_x_o and board.cells[5] == board.user_x_o:
          if board.cells[6] == " ":
            board.cells[6] = board.comp
            break
  
  
#****************************************************************************************************************************************** 
        if board.cells[4] == board.user_x_o and board.cells[6] == board.user_x_o:
          if board.cells[5] == " ":
            board.cells[5] = board.comp
            break
  
#******************************************************************************************************************************************

        if board.cells[5] == board.user_x_o and board.cells[6] == board.user_x_o:
          if board.cells[4] == " ":
            board.cells[4] = board.comp
            break
  
#******************************************************************************************************************************************         
        if board.cells[7] == board.user_x_o and board.cells[8] == board.user_x_o:
          if board.cells[9] == " ":
            board.cells[9] = board.comp
            break
  
#******************************************************************************************************************************************

        if board.cells[7] == board.user_x_o and board.cells[9] == board.user_x_o:
          if board.cells[8] == " ":
            board.cells[8] = board.comp
            break
#******************************************************************************************************************************************
  
        if board.cells[8] == board.user_x_o and board.cells[9] == board.user_x_o:
          if board.cells[7] == " ":
            board.cells[7] = board.comp
            break
  
#******************************************************************************************************************************************

        if board.cells[1] == board.user_x_o and board.cells[4] == board.user_x_o:
          if board.cells[7] == " ":
            board.cells[7] = board.comp
            break
  
  
#******************************************************************************************************************************************
        if board.cells[1] == board.user_x_o and board.cells[7] == board.user_x_o:
          if board.cells[4] == " ":
            board.cells[4] = board.comp
            break
  
#******************************************************************************************************************************************
        if board.cells[4] == board.user_x_o and board.cells[7] == board.user_x_o:
          if board.cells[1] == " ":
            board.cells[1] = board.comp
            break
  
#******************************************************************************************************************************************       
        if board.cells[2] == board.user_x_o and board.cells[5] == board.user_x_o:
          if board.cells[8] == " ":
            board.cells[8] = board.comp
            break
  
  #******************************************************************************************************************************************
        if board.cells[2] == board.user_x_o and board.cells[8] == board.user_x_o:
          if board.cells[5] == " ":
            board.cells[5] = board.comp
            break
  
#******************************************************************************************************************************************
        if board.cells[5] == board.user_x_o and board.cells[8] == board.user_x_o:
          if board.cells[2] == " ":
            board.cells[2] = board.comp
            break
  
#******************************************************************************************************************************************
        if board.cells[3] == board.user_x_o and board.cells[6] == board.user_x_o:
          if board.cells[9] == " ":
            board.cells[9] = board.comp
            break
  
#******************************************************************************************************************************************
        if board.cells[3] == board.user_x_o and board.cells[9] == board.user_x_o:
          if board.cells[6] == " ":
            board.cells[6] = board.comp
            break
  
#******************************************************************************************************************************************
        if board.cells[6] == board.user_x_o and board.cells[9] == board.user_x_o:
          if board.cells[3] == " ":
            board.cells[3] = board.comp
            break
  
 #******************************************************************************************************************************************       
        if board.cells[1] == board.user_x_o and board.cells[5] == board.user_x_o:
          if board.cells[9] == " ":
            board.cells[9] = board.comp
            break
          
  #******************************************************************************************************************************************
  
        
        if board.cells[1] == board.user_x_o and board.cells[9] == board.user_x_o:
          if board.cells[5] == " ":
            board.cells[5] = board.comp
            break
  
#******************************************************************************************************************************************
        if board.cells[9] == board.user_x_o and board.cells[5] == board.user_x_o:
          if board.cells[1] == " ":
            board.cells[1] = board.comp
            break
  
#******************************************************************************************************************************************
        if board.cells[3] == board.user_x_o and board.cells[5] == board.user_x_o:
          if board.cells[7] == " ":
            board.cells[7] = board.comp
            break
  
  
#******************************************************************************************************************************************
        if board.cells[3] == board.user_x_o and board.cells[7] == board.user_x_o:
          if board.cells[1] == " ":
            board.cells[5] = board.comp
            break
  
#****************************************************************************************************************************************** 
        if board.cells[7] == board.user_x_o and board.cells[5] == board.user_x_o:
          if board.cells[1] == " ":
            board.cells[1] = board.comp
            break
  
#******************************************************************************************************************************************
        else:
          cell = 0
          while True:
            random_index = random.randint(1, 9)
            cell += 1
            if board.cells[random_index] == " ":
              board.cells[random_index] = board.comp
              break
            
            elif cell == 100:
              break
          break
  
#******************************************************************************************************************************************
#******************************************************************************************************************************************     
      
      board.display()
  #******************************************************************************************************************************************
      win_123 = board.winner_123(board.comp)
      if win_123 == False:
        break
  #******************************************************************************************************************************************
      win_456 = board.Winner_456(board.comp)
      if win_456 == False:
        break
  #******************************************************************************************************************************************
      win_789 = board.winner_789(board.comp)
      if win_789 == False:
        break

  #******************************************************************************************************************************************
      win_147 = board.winner_147(board.comp)
      if win_147 == False:
        break
  #******************************************************************************************************************************************
      win_258 = board.winner_258(board.comp)
      if win_258 == False:
        break
  #******************************************************************************************************************************************
      win_369 = board.winner_369(board.comp)
      if win_369 == False:
        break
  #******************************************************************************************************************************************
      win_357 = board.winner_357(board.comp)
      if win_357 == False:
        break
  #******************************************************************************************************************************************
      win_159 = board.winner_159(board.comp)
      if win_159 == False:
        break
  #******************************************************************************************************************************************
      tie = board.Tie_game()
      if tie == False:
        break

 #******************************************************************************************************************************************



