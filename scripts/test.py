import rospy
import os
import VL53L0X
from ctypes import *
if __name__ == '__main__':
    try:
        root = os.getcwd()
        tof_lib = CDLL(os.path.join(os.getcwd(),"devel","lib","libvl53l0x_ros.so"))
    except rospy.ROSInterruptException:
        pass