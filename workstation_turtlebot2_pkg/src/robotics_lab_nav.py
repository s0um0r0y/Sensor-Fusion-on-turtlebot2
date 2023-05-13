#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point,Twist
from kobuki_msgs.msg import Sound
import roslib
import sys

class map_navigation():
    def __init__(self):
        #to play sounds at each waypoint
        roslib.load_manifest("kobuki_testsuite")
        rospy.init_node("test_kobuki_Sound")
        pub=rospy.Publisher('/mobile_base/commands/sound',Sound,queue_size=1)
        rate=rospy.Rate(10.0)
        while not self.pub.get_num_connections():
            rate.sleep()
        self.msg=Sound()
        
        #giving fixed coordinates
        self.x1=6.461
        self.y1=4.240
        self.x2=6.188
        self.y2=1.320
        self.x3=1.735
        self.y3=1.043
        self.x0=1.689
        self.y0=4.264
        self.xCenter=3.792
        self.yCenter=2.683
        self.goalReached=False

        #initialize
        choice=0

        if (choice==0):#go to the next waypoint
            self.msg.value=Sound.ON
            pub.publish(self.msg)
            self.goalReached=self.moveToGoal(self.x1,self.y1)
            choice+=1

        if (choice==1):
            self.msg.value=Sound.ON
            pub.publish(self.msg)
            self.goalReached=self.moveToGoal(self.x2,self.y2)
            choice+=1

        if (choice==2):
            self.msg.value=Sound.ON
            pub.publish(self.msg)
            self.goalReached=self.moveToGoal(self.x3,self.y3)
            choice+=1
        
        if (choice==3):
            self.msg.value=Sound.ON
            pub.publish(self.msg)
            self.goalReached=self.moveToGoal(self.x0,self.y0)
            choice+=1

        if (choice==4):
            self.msg.value=Sound.CLEANINGEND
            pub.publish(self.msg)
            self.shutdown()

        if (self.goalReached):
            rospy.loginfo("goal reached")

    def shutdown(self):
        rospy.loginfo("Exit program")
        sys.exit()

    def rotate(self):
        for i in range(16):
            self.msg2.angular.z=1.0
            self.pub2.publish(self.msg2)
            rospy.sleep(0.5)

    def makeSound(self,soundName):
        self.msg.value=soundName
        self.pub.publish(self.msg)

    def moveToGoal(self,xGoal,yGoal):
        #define a client to send goal requests to the move_base server through a SimpleActionClient
        ac=actionlib.SimpleActionClient("move_base",MoveBaseAction)

        #wait for the action server to come up
        while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
            rospy.loginfo("Waiting for the move_base action server to come up")

        goal=MoveBaseGoal()

        #set up the frame parameters
        goal.target_pose.header.frame_id="map"
        goal.target_pose.header.stamp=rospy.Time.now()

        #moving towards the goal
        goal.target_pose.pose.position=Point(xGoal,yGoal,0)
        goal.target_pose.pose.orientation.x=0.0
        goal.target_pose.pose.orientation.y=0.0
        goal.target_pose.pose.orientation.z=0.0
        goal.target_pose.pose.orientation.w=1.0

        rospy.loginfo("Sending goal location")
        ac.send_goal(goal)

        ac.wait_for_result(rospy.Duration(60)) 

        if (ac.get_state()==GoalStatus.SUCCEEDED):
            rospy.loginfo("reached destination")
            return True

        else:
            rospy.loginfo("the turtlebot2 failed to reach the destination")
            self.msg.value=Sound.ERROR
            pub=rospy.Publisher('/mobile_base/commands/sound',Sound,queue_size=1)
            pub.publish(self.msg)
            return False

if __name__=='__main__':
    try:
        rospy.loginfo("the destination has been reached")
        map_navigation()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("map_navigation node terminated")	