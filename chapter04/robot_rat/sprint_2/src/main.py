"""Serves as the point of entry to the Robot Rat Application."""

from robotrat_app import RobotRatApp

def main():
    robot_rat_app = RobotRatApp()
    robot_rat_app.display_menu()


if __name__ == '__main__':
    main()