"""Serves as the point of entry to the Robot Rat Application.

Date: 31 December 2022
Project: Robot Rat
Student: Rick Miller
Class: IT-566: Computer Scripting Techniques
"""

from robotrat_app import RobotRatApp

def main():
    robot_rat_app = RobotRatApp(20, 20)
    robot_rat_app.start_application()


if __name__ == '__main__':
    main()