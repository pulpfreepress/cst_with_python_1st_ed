"""Serves as the point of entry to the Robot Rat Application.

Date: 31 December 2022
Project: Robot Rat
Student: Rick Miller
Class: IT-566: Computer Scripting Techniques
"""

from robotrat_app import RobotRatApp
import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Set floor dimensions from command-line.'
        )
    parser.add_argument('rows', metavar='N', type=int, help='Number of rows')
    parser.add_argument('cols', metavar='N', type=int, help='Number of columns')
    args = parser.parse_args()
    robot_rat_app = RobotRatApp(args.rows, args.cols)
    robot_rat_app.start_application()


if __name__ == '__main__':
    main()