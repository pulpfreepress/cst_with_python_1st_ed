"""Serves as the point of entry to the Robot Rat Application."""

from robotrat_app import RobotRatApp

def main():
    robot_rat_app = RobotRatApp(20, 20)
    robot_rat_app.start_application()


if __name__ == '__main__':
    main()