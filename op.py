#!/usr/bin/env python
# This program publishes randomly-generated velocity
# messages for turtlesim.
import rospy
import numpy as np # For random numbers
 
 
from std_msgs.msg import String
from turtlesim import msg # we need to import hte turtlesim msgs in order to use them
f = open("tkmc.txt", "w")

 
#Create callback. This is what happens when a new message is received
def sub_cal(msg):
    rospy.loginfo("position=%s", msg)
    print(msg.data)
    f.write(msg.data)
    f.close()
    
 
#Initialize publisher
rospy.Subscriber('/visp_auto_tracker/code_message', String, sub_cal, queue_size=1000)
 
# Initialize node
rospy.init_node('location_listner')
rospy.spin()
rospy.loginfo()
