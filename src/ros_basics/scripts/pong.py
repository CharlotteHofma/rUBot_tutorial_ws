#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback_string(msg):
	global /pong
	/pong.data = msg.data
	new_msg = String()
	new_msg.data = "False"
	pub.publish(new_msg)
	rospy.loginfo("I Publish the counter value: %s", counter)


rospy.init_node("pong")
rate = rospy.Rate(1)
pub = rospy.Publisher('pong', String, queue_size=1)
sub = rospy.Subscriber('/ping', String, callback_string)
rospy.spin()