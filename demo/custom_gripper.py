import os
import time
import sys
from pymycobot.mycobot import MyCobot

sys.path.append(os.path.dirname(__file__))
from port_setup import setup


def gripper_test(mc):
    print("Opening the gripper")    
    mc.open_custom_gripper(50)
    
    time.sleep(10)
    print("Closing the gripper")
    mc.close_custom_gripper(150)
    print("detaching from servo")

if __name__ == "__main__":
    mycobot = setup()
    gripper_test(mycobot)
