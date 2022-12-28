"""Implements the Robot Rat Application."""
import sys
from enum import Enum

class RobotRatApp():
    """A Remote-Controlled Robot Rat Application."""

    # Menu Choice Constants
    _PEN_UP='1'
    _PEN_DOWN='2'
    _TURN_RIGHT='3'
    _TURN_LEFT='4'
    _MOVE_FORWARD='5'
    _PRINT_FLOOR='6'
    _EXIT='7'

    # Enumerated Types
    class PenPositions(Enum):
        UP = 0
        DOWN = 1

    class Directions(Enum):
        NORTH = 0
        EAST = 1
        SOUTH = 2
        WEST = 3


    def __init__(self, rows, cols):
       """Initialize RobotRatApp object."""
       self._rows = rows
       self._cols = cols
       self._floor = [[ False for i in range(rows)] for j in range(cols)]
       self._initialize_test_patern()
       self._pen_position = self.PenPositions.UP
       self._direction = self.Directions.EAST
       self._current_row = 0
       self._current_col = 0


    def display_menu(self):
        """Prints menu items to the console."""
        print('\n\t\tRobot Rat Control Menu\n')
        print('\t1. Pen Up')
        print('\t2. Pen Down')
        print('\t3. Turn Right')
        print('\t4. Turn Left')
        print('\t5. Move Forward')
        print('\t6. Print Floor')
        print('\t7. Exit')

    def process_menu_choice(self):
        # Prompt user for input
        # Assign input string to variable
        user_input = input('\n\tEnter Command Number: ')
        # Use first character of input as menu choice
        menu_choice = user_input[0]
        if __debug__: 
            print(f'You entered command number: {menu_choice}')
        # Is menu_choice valid command?
        # YES - Execute command
        # NO - Display error message and try again
        match menu_choice:
            case self._PEN_UP: self.set_pen_up()
            case self._PEN_DOWN: self.set_pen_down()
            case self._TURN_RIGHT: self.turn_right()
            case self._TURN_LEFT: self.turn_left()
            case self._MOVE_FORWARD: self.move_forward()
            case self._PRINT_FLOOR: self.print_floor()
            case self._EXIT: sys.exit()
            case _: self.print_error_message(menu_choice)
        

    def start_application(self):
        while True:
            self.display_menu()
            self.process_menu_choice()

    def set_pen_up(self):
        if __debug__:
            print('set_pen_up() method called...')
        self._pen_position = self.PenPositions.UP
        print(f'Pen is {self._pen_position}')

    def set_pen_down(self):
        if __debug__:
            print('set_pen_down() method called')
        self._pen_position = self.PenPositions.DOWN
        print(f'Pen is {self._pen_position}')

    def turn_left(self):
        if __debug__:
            print('turn_left() method called...')
        match(self._direction):
            case self.Directions.NORTH: 
                self._direction = self.Directions.WEST
            case self.Directions.WEST:
                self._direction = self.Directions.SOUTH
            case self.Directions.SOUTH: 
                self._direction = self.Directions.EAST
            case self.Directions.EAST:
                self._direction = self.Directions.NORTH
            case _: self._direction = self.Directions.EAST

        print(f'Robot Rat is facing {self._direction}')

    def turn_right(self):
        if __debug__:
            print('turn_right() method called...')
        match(self._direction):
            case self.Directions.NORTH: 
                self._direction = self.Directions.EAST
            case self.Directions.EAST:
                self._direction = self.Directions.SOUTH
            case self.Directions.SOUTH: 
                self._direction = self.Directions.WEST
            case self.Directions.WEST:
                self._direction = self.Directions.NORTH
            case _: self._direction = self.Directions.EAST

        print(f'Robot Rat is facing {self._direction}')

    def move_forward(self):
        if __debug__:
            print('move_forward() method called...')

        spaces_to_move = 0
        try:
            spaces_to_move = int(input("Enter spaces to move: "))

        except Exception as e:
            print('Invalid movment number. Setting to 1')
            spaces_to_move = 1
            
        match(self._pen_position):
            case self.PenPositions.UP:
                match(self._direction):
                    case self.Directions.NORTH:
                        self._current_row -= spaces_to_move
                        if self._current_row < 0:
                            self._current_row = 0
                    case self.Directions.EAST:
                        self._current_col += spaces_to_move
                        if self._current_col > (self._cols - 1):
                            self._current_col = (self._cols - 1)
                    case self.Directions.SOUTH:
                        self._current_row += spaces_to_move
                        if self._current_row > (self._rows - 1):
                            self._current_row = (self._rows - 1)
                    case self.Directions.WEST:
                        self._current_col -= spaces_to_move
                        if self._current_col < 0:
                            self._current_col = 0
            case self.PenPositions.DOWN:
                match(self._direction):
                    case self.Directions.NORTH:
                        while (self._current_row > 0) and (spaces_to_move > 0):
                            self._current_row -= 1
                            self._floor[self._current_row ][self._current_col] = True
                            spaces_to_move -= 1
                    case self.Directions.EAST:
                         while (self._current_col < self._cols) and (spaces_to_move > 0):
                            self._current_col += 1
                            self._floor[self._current_row ][self._current_col] = True
                            spaces_to_move -= 1
                    case self.Directions.SOUTH:
                        while (self._current_row < self._rows) and (spaces_to_move > 0):
                            self._current_row += 1
                            self._floor[self._current_row ][self._current_col] = True
                            spaces_to_move -= 1
                    case self.Directions.WEST:
                        while (self._current_col > 0) and (spaces_to_move > 0):
                            self._current_col -= 1
                            self._floor[self._current_row ][self._current_col] = True
                            spaces_to_move -= 1
       
        print(f'Robot Rat at [{self._current_row}][{self._current_col}] facing {self._direction} {self._pen_position}')
        


    def print_floor(self):
        if __debug__:
            print('print_floor() method called')
        for row in self._floor:
            print('\t', end='')
            for col in row:
                if col:
                    print('- ', end='')
                else:
                    print('0 ', end='')
            print()

    def _initialize_test_patern(self):
        self._floor[0][0] = True
        self._floor[0][1] = True
        self._floor[0][2] = True
        self._floor[0][3] = True
        self._floor[0][4] = True
        self._floor[1][4] = True
        self._floor[2][4] = True
        self._floor[3][4] = True

    def print_error_message(self, menu_choice):
        print(f'WARNING: {menu_choice} is an invalid command!')

