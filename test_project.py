from project import colors,style,option
import pytest



def main():
   test_color()
   test_style()
   test_option
   
def test_color():
   assert colors(1) == "red"
   assert colors(2) == "grey"
   
def test_style():
   assert style(1) == "acrobatic"
   assert style(2) == "alligator"
   
def test_option(): 
   with pytest.raises(SystemExit):
        option(3)
   
   
   
   
if __name__ =='__main__':
   main()