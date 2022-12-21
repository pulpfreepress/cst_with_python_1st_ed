"""Implements the Robot Rat Application."""

class RobotRatApp():
    """A Remote-Controlled Robot Rat Application."""

    def __init__(self):
        print('I am Robot Rat! I am alive!')

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

