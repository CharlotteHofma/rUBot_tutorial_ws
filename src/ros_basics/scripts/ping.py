#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node("ping")
rate = rospy.Rate(1)
pub = rospy.Publisher('ping', String, queue_size=1)

while not rospy.is_shutdown():
	msg = String()
	msg.data = "False"
	pub.publish(msg)
	rate.sleep()