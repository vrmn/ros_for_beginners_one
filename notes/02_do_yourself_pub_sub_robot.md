principal is the same no matter the robot

in t1 type roscore

in t2 type
rosrun turtlesim turtlesim_node

you'll use these to help buld your assignmnt_pub_self_.py and assingmet_sub_self

#subscriber for the topic that will hwo the location fo the robot

#publisher to the topic that will make the robot move

#what is the topic fo the position

#what is the topic that makes the robot move

# -- to do this use rostopic list and you'll see the list of all the topics available

# then when writing you can get the type of message using rostopic info

# this dictates what you type on top
### from geometry_msgs.msg import Twist

# the twist message contains infomrmation about the speed linear and angular

now what if we want to look at its content of the Twist message
 welp type rosmsg show geometry_msgs/Twist to see
this is what you need to learn how to use in your python code in order to define the veloxity


# underneath the hiwle
# twist = Twist()
# twist.linear.x = 1.0
