# Robot Rat Project


## Objectives:
Demonstrate your ability to utilize the following language features in a Python program:
- Classes
- Methods
- Two-Dimensional Lists
- Instance Variables
- Local Method Variables
- Program Control-Flow Statements
- Console Input & Output

## Task:
You are in command of a robot rat! Write a Python console application that will allow you to control the rat’s movements around a 20 x 20 grid floor.
The robot rat is equipped with a pen. The pen has two possible positions: UP or DOWN. When the pen is in the UP position the robot rat can move around the floor without leaving a mark. If the pen is in the DOWN position, the robot rat leaves a mark on visited floor grid positions. Moving the robot rat about the floor with the pen UP or DOWN at various locations results in a pattern written upon the floor.

## Hints:
- The robot rat can move in four directions: NORTH, SOUTH, EAST, and WEST. Implement diagonal movement if you desire.
- Implement the floor as a two-dimensional list of boolean objects
- Use the built-in functions input() and print() to read text from and write text to the console.

## User Interface:
At minimum, provide a text-based command menu with the following or similar command choices:

```
	1. Pen Up
	2. Pen Down
	3. Turn Right
	4. Turn Left
	5. Move Forward
	6. Print Floor
	7. Exit
```

When menu choice 6 is selected to print the floor, the result might look something like this, assuming you chose a hyphen `'-'` to represent a marked area of the floor and a zero `'0'` to represent an unmarked area. You may use other pattern areas if desired.

```
	-----000000000000000
	00000000000000000000
	00000000000000000000
	00000000000000000000
	00000000000000000000
	00000000000000000000
	00000000000000000000
	00000000000000000000
	00000000000000000000
	00000000000000000000
	00000000000000000000
	00000000000000000000
	00000000000000000000
	00000000000000000000
	00000000000000000000
```

In this example, the robot rat moved from the upper-left corner of the floor five spaced to the EAST with the pen DOWN.
