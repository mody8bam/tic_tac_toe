import os

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
    

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
        print("wellcome to X & O game ")
        print('1. start game')
        print('2. quit game')
        choice=input(' enter your choice 1 or 2 : ')
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


class Board:
    def __init__(self) -> None:
        self.board=[str(i) for i in range(1,10)]
    
    def display_board(self):
        for i in range(0,9,3):
            print('|'.join(self.board[i:i+3]))
            if i<6:
                print('-'*5)
    
    def update_board(self,choice,symbol):
        if self.is_valid_move(choice):
            self.board[choice-1]=symbol
            return True
        return False   
    
    def is_valid_move(self,choice):
        if self.board[choice-1].isdigit():
            return True
        return False           
    
    def reset_board(self):
        self.board=[str(i) for i in range(1,10)]

     
     
class Game:
    def __init__(self) -> None:
        self.players=[Player(),Player()]
        self.board=Board()
        self.menu=Menu()
        self.current_player_index=0
        
    def start_game(self):
        choice=self.menu.display_main_menu()
        if choice=='1':
            self.setup_players()
            self.play_game()
            
        else :
            self.quit_game()
    
    def setup_players(self):
        for index, player in enumerate(self.players,start=1):
            print(f"player {index} ",end='')
            player.choose_name()
            print(f"player {index} ",end='')
            player.choose_symbol()
            # clear_screen()
            
    
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice=self.menu.display_endgame_menu()
                if choice=='1':
                    self.restart_game()
                else:
                    self.quit_game()
                    break
    def check_win(self):
        win_comb=[
            [0,1,2],
            [3,4,5],
            [6,7,8],
            
            [0,3,6],
            [1,4,7],
            [2,5,8],
            
            [0,4,8],
            [2,4,6]
        ]
        for combo in win_comb:
            if self.board.board[combo[0]] == self.board.board[combo[1]] ==self.board.board[combo[2]]:
                print(f"{self.players[self.current_player_index].name} wins!")
                return True
        return False
                
            
        
        
        
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board) #generator expresion
    
    def restart_game(self):
        self.board.reset_board()
        self.play_game()
        
    def play_turn(self):
        player=self.players[self.current_player_index]
        self.board.display_board()
        print(f" {player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice=int(input('choose cell [1-9]: '))
                if 1<= cell_choice <= 9 and self.board.update_board(cell_choice,player.symbol):
                    break
                else :
                    print('invalid move, try again ')
            except ValueError:
                print('please enter a number between 1-9')
        if self.check_win():
            print(f'{player.name} has won the game ....')
            self.board.reset_board()
        self.switch_player()
        
    def switch_player(self):
          self.current_player_index = 1-self.current_player_index      
        
    
    
    
    def quit_game(self):
        print("Thanks for you for playing")

        
game=Game()
game.start_game()
