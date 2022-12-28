"""Implements the Robot Rat Application."""
import sys

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

    def __init__(self, rows, cols):
       """Initialize RobotRatApp object."""
       self._rows = rows
       self._cols = cols
       self._floor = [[ False for i in range(rows)] for j in range(cols)]
       self._initialize_test_patern()

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

    def set_pen_down(self):
        if __debug__:
            print('set_pen_down() method called')

    def turn_left(self):
        if __debug__:
            print('turn_left() method called...')

    def turn_right(self):
        if __debug__:
            print('turn_right() method called...')

    def move_forward(self):
        if __debug__:
            print('move_forward() method called...')

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

