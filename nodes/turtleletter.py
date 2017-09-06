#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def talker():
	pub = rospy.Publisher('turtle1/cmd_vel',Twist, queue_size=10)
	rospy.init_node('talker',anonymous=True)
	rate = rospy.Rate(1) #3Hz
        Str1 = Twist()
	Str1.linear.x = 0.0
	Str1.linear.y = 0.0 
	Str1.linear.z =0.0
	Str1.angular.x = 0.0
	Str1.angular.y = 0.0
	Str1.angular.z = -4.5
	rospy.loginfo(Str1)
	pub.publish(Str1)
	rate.sleep()
	Str2 = Twist()
	Str2.linear.x = -4.5
	Str2.linear.y = 0.0
	Str2.linear.z = 0.0
	Str2.angular.x = 0.0
	Str2.angular.y = 0.0
	Str2.angular.z = 0.0
	rospy.loginfo(Str2)
        pub.publish(Str2)
        rate.sleep()
	Str3 = Twist()
	Str3.linear.x = 4.5
	Str3.linear.y = 0.0
	Str3.linear.z = 0.0
	Str3.angular.x = 0.0
	Str3.angular.y = 0.0
	Str3.angular.z = 0.0
	rospy.loginfo(Str3)
	pub.publish(Str3)
	rate.sleep()
	Str4 = Twist()
	Str4.linear.x = 0.0
	Str4.linear.y = 0.0
	Str4.linear.z = 0.0
	Str4.angular.x = 0.0
	Str4.angular.y = 0.0
	Str4.angular.z = -1.5
	rospy.loginfo(Str4)
        pub.publish(Str4)
        rate.sleep()
	Str5 = Twist()
	Str5.linear.x = 4.0
	Str5.linear.y = 0.0
	Str5.linear.z = 0.0
	Str5.angular.x = 0.0
	Str5.angular.y = 0.0
	Str5.angular.z = -3.12
		
	rospy.loginfo(Str5)
        pub.publish(Str5)
        rate.sleep()
	return

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
