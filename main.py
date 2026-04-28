
import sys
import time
import os
from colorama import Fore, Style, init
import random
#Main Boxes for Board
# list of combine boxes
board = [1,2,3,4,5,6,7,8,9]

#Player/computer chooses element
while True:  # X or O user selection
   print("Loading.")
   time.sleep(0.5)
   os.system('cls' if os.name == 'nt' else 'clear')
   print("Loading.")
   time.sleep(0.5)
   os.system('cls' if os.name == 'nt' else 'clear')
   print("Loading...")
   time.sleep(0.5)
   os.system('cls' if os.name == 'nt' else 'clear')
   print("Welcome to the Tic-Tak-Toe game")
   print("Pick a color for text")
   print("R: for red.")
   print("B: for blue.")
   print("M: for magenta.")
   color_pick = input("color selection:")
   if color_pick == "R" or color_pick == "r":
      print(Fore.RED+"Bloody >:[")
   if color_pick == "B" or color_pick == "b":
      print(Fore.BLUE+"Feeling blue :(")
   if color_pick == "M" or color_pick == "m":
      print(Fore.LIGHTMAGENTA_EX+"You use T-mobile?")
   else:
      print("Im assuming your basic or couldn't listen to basic instruction so here is basic white :|")
   os.system('cls' if os.name == 'nt' else 'clear')
   user_element = input("SELECT: X or O:")
   comp_element = ""  # empty
   global user_points
   global comp_points
   user_points = 0
   comp_points = 0

   if user_element == "X" or user_element == "x": #if user picks "x"
      user_element = "X"
      comp_element = "O"
      print("You selected: X")
      print("Computer is: O")
      user_input_Hist = []  # to save user inputs
      break
   if user_element == "O" or user_element == "o": #if user picks "o"
      user_element = "O"
      comp_element = "X"
      print("You selected: O")
      print("Computer is: X")
      user_input_Hist = []  # to save user inputs
      break
   else:  #if user picks neither, will loop
      print(" Pls Select X or O")

def clear_screen():
   os.system('cls' if os.name == 'nt' else 'clear')


def show_board(): # Shows board to user
   print(" Your Score:", user_points)
   print(" Play Score:", comp_points)
   for i in range(0, 3):
      print("[",board[i],"]", end="")
      if i == 2:
         print(sep="\n")
   for i in range(3, 6):
      print("[",board[i],"]", end="")
      if i == 5:
         print(sep="\n")
   for i in range(6, 9):
      print("[",board[i],"]", end="")
   print("\n")

def user_pick_position():
   while True:
      global user_input
      global quit_after_turn
      show_board()
      try:  # try for value error
         user_input = int(input(" Pick an interger 1-9 or 67 to quit:"))
      except ValueError:
         #clear_screen()
         print("Please enter an integer.")
         continue
      if user_input == 67:
         quit_after_turn = 1
         quit_game_loop()
      if user_input >= 1 and user_input <= 9:
         user_input -= 1  # matches user_input to irratable list
         if user_input in user_input_Hist:  # if in list user must choose another space
            clear_screen()
            print("That space is already occupied, pick another one.")
         else:
            user_input_Hist.append(user_input)
            board[user_input] = user_element
            # clear_screen()
            # print(board[user_input],end="\n")
            show_board()
            clear_screen()
            break


def comp_pick_position():
   global user_input
   while True:
      show_board()
      comp_input = random.randint(1, 9)
      if comp_input >= 1 and comp_input <= 9:
         comp_input -= 1
      if comp_input in user_input_Hist:
         clear_screen()
      else:
         # animations
         clear_screen()
         print("Computer is picking its position")
         time.sleep(1)
         clear_screen()
         print("Computer is picking its position.")
         time.sleep(1)
         clear_screen()
         print("Computer is picking its position..")
         time.sleep(1)
         clear_screen()
         print("Computer is picking its position...")
         time.sleep(1)
         clear_screen()
         user_input_Hist.append(comp_input)
         board[comp_input] = comp_element
         # clear_screen()
         # print(board[comp_],end="\n")
         show_board()
         time.sleep(1.5)
         clear_screen()
         break

def winn_los_tie():
   global check_string
   check_string = all(isinstance(char, str) for char in board)
   global quit_after_turn
   quit_after_turn = 0
   global user_points
   global comp_points
   while True:
      #Check hoz spaces
      if board[0] == board[1] == board[2]:
         if board[1] == "X":
            print("You win!")
            user_points += 1
            quit_after_turn = 1
         if board[1] != "X":
            print("Computer wins!")
            comp_points += 1
            quit_after_turn = 1
      if board[3] == board[4] == board[5]:
         if board[4] == "X":
            print("You win!")
            user_points += 1
            quit_after_turn = 1
         if board[4] != "X":
            print("Computer wins!")
            comp_points += 1
            quit_after_turn = 1
      if board[6] == board[7] == board[8]:
         if board[7] == "X":
            print("You win!")
            user_points += 1
            quit_after_turn = 1
         if board[7] != "X":
            print("Computer wins!")
            comp_points += 1
            quit_after_turn = 1
      #Check vert spaces
      if board[0] == board[3] == board[6]:
         if board[3] == "X":
            print("You win!")
            user_points += 1
            quit_after_turn = 1
         if board[3] != "X":
            print("Computer wins!")
            comp_points += 1
            quit_after_turn = 1
      if board[1] == board[4] == board[7]:
         if board[4] == "X":
            print("You win!")
            user_points += 1
            quit_after_turn = 1
         if board[4] != "X":
            print("Computer wins!")
            comp_points += 1
            quit_after_turn = 1
      if board[2] == board[5] == board[8]:
         if board[5] == "X":
            print("You win!")
            user_points += 1
            quit_after_turn = 1
         if board[5] != "X":
            print("Computer wins!")
            comp_points += 1
            quit_after_turn = 1
      # Check diagonal
      if board[0] == board[4] == board[8]:
         if board[4] == "X":
            print("You win!")
            user_points += 1
            quit_after_turn = 1
         if board[4] != "X":
            print("Computer wins!")
            comp_points += 1
            quit_after_turn = 1
      if board[2] == board[4] == board[6]:
         if board[4] == "X":
            print("You win!")
            user_points += 1
            quit_after_turn = 1
         if board[4] != "X":
            print("Computer wins!")
            comp_points += 1
            quit_after_turn = 1
      if check_string == 1 and quit_after_turn == 0:
         print("Tie!")
      if quit_after_turn == 1:
         break
      else:
         break


def quit_game_loop():
   global board
   global check_string
   global quit_after_turn
   while True:
      if check_string == 1 or quit_after_turn == 1:
         user_quit_input = input("Want to quit? (y/n):")
         if user_quit_input == "y":
            sys.exit()
         if user_quit_input == "n":
            check_string = 0
            quit_after_turn = 0
            user_input_Hist.clear()
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            # restart animation
            clear_screen()
            print("restart.")
            time.sleep(0.5)
            clear_screen()
            print("restart..")
            time.sleep(0.5)
            clear_screen()
            print("restart...")
            time.sleep(0.5)
            clear_screen()
            user_pick_position()
      else:
         break




def main():
   while True:
      user_pick_position()
      winn_los_tie()
      quit_game_loop()
      comp_pick_position()
      winn_los_tie()
      quit_game_loop()
main()