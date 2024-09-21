class Player:
    def __init__(self) -> None:
        self.name=''
        self.symbol=''
    
    def choose_name(self):
        while True:
            name=input("enter your name: ")
            if name.isalpha():
                self.name=name
                break
            else :
                print('use only letter please ')
    
    def choose_symbol(self):
        while True:
            symbol=input(f"{self.name} shoose your symbol ")
            if symbol.isalpha() and len(symbol)==1:
                self.symbol=symbol.upper()
                break
            else :
                print('invalid symbol , please symbol of length of 1')
                
class Menu:
    def display_main_menu(self):
        print("wellcome to x & o game ")
        print('1. start game')
        print('2. quit game')
        choice=input(' enter your choice 1 or 2')
        return choice
    
    def display_endgame_menu(self):
        menu_text="""
        Game over 
        1. restart game
        2. quit game 
        enter your choice 
        """   
        choice=input(menu_text)
        return choice

        
        
        