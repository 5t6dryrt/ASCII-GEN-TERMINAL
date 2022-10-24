
import sys
import os


from pyfiglet import Figlet,figlet_format 
from colorama import init
init(strip=not sys.stdout.isatty()) #for window
from termcolor import cprint 


def main():
  
   figlet = Figlet(font="standard")
   print(figlet.renderText("THIS IS CS50P FINAL PROJECT"))  
   cprint(figlet_format('HAVARD',font='starwars'),'red','on_red')
   input("Press Enter to continue...")
   os.system('cls')
   print(("""
   SELECT OPTION
               1.ASCII GENERATOR
               2.SELF INTRODUCTION
               3.EXIT
                  """))
   ans = int(input("TYPE HERE : "))
   option(ans)
   

def option(a):
   match a:
      case 1:
         art()
      case 2:
         intro()
      case 3:
         sys.exit()
      case _:
         sys.exit()


def art():
   words= str(input("WORDS : "))
   color= int(input("""COLOR
                  1.red
                  2.grey
                  3.green
                  4.yellow
                  5.blue
                  6.margenta
                  7.cyan
                  8.white
                  ANS : """))
   styles = int(input("""STYLE
                     1.acrobatic
                     2.alligator
                     3.alphabet
                     4.bell
                     5.broadway
                     6.bubble
                     7.doom
                     8.isometric1
                     9.starwars        
                     ANS : """))
   rc=colors(color)
   rs=style(styles)
   os.system('cls')
   cprint(figlet_format(f'{words}',font=f'{rs}'),f'{rc}',attrs=["bold"])
   
   
   
   
def colors(c):
   switch={1:'red',2:'grey',3:'green',4:'yellow',5:'blue',6:'margenta',7:'cyan',8:'white'}
   return switch.get(c)

def style(s):
   switch={1:'acrobatic',2:'alligator',3:'alphabet',4:'bell',5:'broadway',6:'bubble',7:'doom',8:'isometric1',9:'starwars'}
   return switch.get(s)
   
def intro():
   os.system('cls')
   print(" ")
   figlet = Figlet(font="standard")
   print(figlet.renderText("THIS IS CS50P FINAL PROJECT"))   
   print("""         My name is Nuttapat Pitayapongporn , I was born and raised in Sriracha chonburi.
   Chonburi it is a part of thailand .There are so many tourist spot like pattaya it isn't
   far from my home . We have the on of the best night walking street in the world .
   Whatever Whatever, thanks to David J. Malan and team.that has been issued teaching 
   The greatest course in the world in various fields and help develop knowledge 
   and ability for learners All races, nationalities, and different religions join the cs50. 
            
            
            """)
   sys.exit("                       BECAUSE THIS IS CS50")

if __name__ =="__main__":
   main()