"""Implements the Robot Rat Application.

Date: 31 December 2022
Project: Robot Rat
Student: Rick Miller
Class: IT-566: Computer Scripting Techniques
"""

import sys
from enum import Enum

class RobotRatApp():
	"""A Remote-Controlled Robot Rat Application."""

	# Menu Choice Constants
	_PEN_UP = '1'
	_PEN_DOWN = '2'
	_TURN_RIGHT = '3'
	_TURN_LEFT = '4'
	_MOVE_FORWARD = '5'
	_PRINT_FLOOR = '6'
	_EXIT = '7'

	# Enumerated Types
	class PenPositions(Enum):
		"""Valid Pen Position States"""
		UP = 0
		DOWN = 1


	class Directions(Enum):
		"""Valid Directions"""
		NORTH = 0
		EAST = 1
		SOUTH = 2
		WEST = 3


	def __init__(self, rows, cols):
		"""Initialize RobotRatApp object."""
		self._rows = rows
		self._cols = cols
		self._floor = [[False for i in range(cols)] for j in range(rows)]
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
		"""Process menu commands."""
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


	def set_pen_up(self):
		"""Changes pen state to UP."""
		if __debug__:
			print('set_pen_up() method called...')
		self._pen_position = self.PenPositions.UP
		print(f'Pen is {self._pen_position}')


	def set_pen_down(self):
		"""Changes pen state to DOWN."""
		if __debug__:
			print('set_pen_down() method called')
		self._pen_position = self.PenPositions.DOWN
		print(f'Pen is {self._pen_position}')


	def turn_right(self):
		"""Turns Robot Rat to the left."""
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


	def turn_left(self):
		"""Turns Robot Rat to the right."""
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


	def move_forward(self):
		""" Moves Robot Rat forward by indicated number of spaces.
		    If the pen is UP the Robot Rat does not leave a mark on
		    the floor. If the pen is DOWN the Robot Rat leaves a mark
		    on the floor.
		"""
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
						while (self._current_row > -1) and (spaces_to_move > 0):
							self._floor[self._current_row][self._current_col] = True
							if self._current_row > 0:
								self._current_row -= 1
							else:
								break
							spaces_to_move -= 1
					case self.Directions.EAST:
						while (self._current_col < self._cols) and (spaces_to_move > 0):
							self._floor[self._current_row][self._current_col] = True
							if self._current_col < (self._cols - 1):
								self._current_col += 1
							else:
								break
							spaces_to_move -= 1
					case self.Directions.SOUTH:
						while (self._current_row < self._rows) and (spaces_to_move > 0):
							self._floor[self._current_row][self._current_col] = True
							if self._current_row < (self._rows - 1):
								self._current_row += 1
							else:
								break
							spaces_to_move -= 1
					case self.Directions.WEST:
						while (self._current_col > -1) and (spaces_to_move > 0):
							self._floor[self._current_row][self._current_col] = True
							if self._current_col > 0:
								self._current_col -= 1
							else:
								break
							spaces_to_move -= 1

		
	def print_floor(self):
		""" Prints the floor pattern."""
		if __debug__:
			print('print_floor() method called')
		for rindx, row in enumerate(self._floor):
			print('\t', end='')
			for cindx, col in enumerate(row):
				if((rindx == self._current_row) and (cindx == self._current_col)):
					print('X ', end='')
				elif col:
					print('- ', end='')
				else:
					print('0 ', end='')

				

			print()


	def print_status(self):
		"""Displays Robot Rat current position, direction, and pen position."""
		print(f'\n\tRobot Rat at [{self._current_row}][{self._current_col}] \
facing {self._direction} {self._pen_position}')


	def print_error_message(self, menu_choice):
		"""Warns of an invalid command entry."""
		print(f'WARNING: {menu_choice} is an invalid command!')


	def start_application(self):
		"""Start application processing loop."""
		while True:
			self.display_menu()
			self.print_status()
			self.process_menu_choice()
