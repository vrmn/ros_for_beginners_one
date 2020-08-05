#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "turtlesim/Pose.h"
#include <sstream>

// so cin and cout works without std::cout std::cin
using namespace std;


//global variables
//this publisher needs to initialized in the main function
ros::Publisher velocity_publisher;
ros::Subscriber pose_subscriber;
turtlesim::Pose turtlesim_pose;

const double x_min = 0.0;
const double y_min = 0.0;
const double x_max = 11.0;
const double y_max = 11.0;

const double PI = 3.14159265359;



// mehtod to move the robot straight, rotate and change degrees in radians
void move(double speed, double distance, bool isForward);
void rotate(double angular_speed, double angle, bool clockwise);
double degrees2radians(double angle_in_degrees);

// lets assume that you want to put the robot in a certain absolute orientation not relative orientation
// for this you need two additional nodes. when its called its going to put robot in a certain absolute orientation
double setDesiredOrientation (double desired_angle_radians);
void poseCallback(const turtlesim::Pose::ConstPtr & pose_message);

int main(int argc, char **argv)
{
      // initiale new rose NODE
        ros::init(argc, argv, "robot_cleaner");
        ros::NodeHandle n;

        //define variables in this function since they are not universal
        double speed, angular_speed;
        double distance, angle;
        bool isForward, clockwise;

      // initliaze publisher NodeHandle.advertise<type of message>("nameoftopic", buffer)
        velocity_publisher = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);
        pose_subscriber = n.subscribe("/turtle1/pose", 10, poseCallback);

        // // asing for user input
        // cout<<"enter speed: ";
        // cin>>speed;
        // cout<<"enter distance: ";
        // cin>>distance;
        // cout<<"forward?: ";
        // cin>>isForward;
        // move(speed, distance, isForward);
        // // if hard coded it would look like this
        // // move (2.0, 5.0, 1);
        //
        // cout<<"enter angular velocity degree/sec: ";
        // cin>>angular_speed;
        // cout<<"enter desired angle (degrees): ";
        // cin>>angle;
        // cout<<"clockwise?: ";
        // cin>>clockwise;
        // rotate(degrees2radians(angular_speed), degrees2radians(angle), clockwise);

        setDesiredOrientation(degrees2radians(120));
        ros::Rate loop_rate(0.5);
        loop_rate.sleep();
        setDesiredOrientation(degrees2radians(-60));
        loop_rate.sleep();
        setDesiredOrientation(degrees2radians(0));

        ros::spin();
        return 0;
}

// makes the robot move with a certain linear velocity for a certain distance in a froward or backward stragith direction
void move(double speed, double distance, bool isForward)
{
      //ask yourself what message to publish and how
      // hint use rostopic list, rostopic info, and rosmsg show to have an idea what the code is going to need

      // create teist mseesage      // as well as create a publisher for the velocity command
      geometry_msgs::Twist vel_msg;

      //distance = speed * time

      //set a random linear velocity in the x axis
      if (isForward)
        vel_msg.linear.x = abs(speed);
      else
        vel_msg.linear.x = -abs(speed);

      // then y and z velocity needs to be set to 0 because were not going to move either left or right
      vel_msg.linear.y = 0;
      vel_msg.linear.z = 0;

      //set a random angular velxoity in the y axis
      vel_msg.angular.x = 0;
      vel_msg.angular.y = 0;
      vel_msg.angular.z = 0;

      //t0: current Time
      //loop
      //publish the velocity_publisher
      //estimate the current_distcne = speed * (t1-t0)
      //current_distance_movded_by robot <= distance

      //t0: current time
      double t0 = ros::Time::now().toSec();
      double current_distance = 0;

      // to make more accurate increase the loop rate
      ros::Rate loop_rate(10);

      //loop do while

      do{
        velocity_publisher.publish(vel_msg);
        double t1 = ros::Time::now().toSec();
        current_distance = speed * (t1-t0);
        //need ros::spinOnce()
        ros::spinOnce();
        loop_rate.sleep();
      }while (current_distance < distance);
      // set velocity equal to zero when out of the loop to force robot to stop immediately.
      vel_msg.linear.x = 0;
      velocity_publisher.publish(vel_msg);
}


void rotate (double angular_speed, double relative_angle, bool clockwise)
{

      geometry_msgs::Twist vel_msg;
      // set  a random linear velocity in the x axis
      vel_msg.linear.x = 0;
      vel_msg.linear.y = 0;
      vel_msg.linear.z = 0;

      // set a random angular velocity in the y axis
      vel_msg.angular.x = 0;
      vel_msg.angular.y = 0;

      if (clockwise)
            vel_msg.angular.z = -abs(angular_speed);
      else
            vel_msg.angular.z = abs(angular_speed);

      double t0 = ros::Time::now().toSec();
      double current_angle = 0.0;
      ros::Rate loop_rate(10);
      do{
        velocity_publisher.publish(vel_msg);
        double t1 = ros::Time::now().toSec();
        current_angle = angular_speed * (t1-t0);
        ros::spinOnce();
        loop_rate.sleep();
      }while(current_angle<relative_angle);

      vel_msg.angular.z = 0;
      velocity_publisher.publish(vel_msg);
}

double degrees2radians(double angle_in_degrees)
{
  return angle_in_degrees*PI /180.0;
}

double setDesiredOrientation(double desired_angle_radians)
{
  double relative_angle_radians = desired_angle_radians - turtlesim_pose.theta;
  bool clockwise = ((relative_angle_radians<0)?true:false);
  cout<<desired_angle_radians<<","<<turtlesim_pose.theta<<","<<relative_angle_radians<<","<<clockwise<<endl;
  rotate (abs(relative_angle_radians), abs(relative_angle_radians), clockwise);
}

void poseCallback(const turtlesim::Pose::ConstPtr & pose_message)
{
  turtlesim_pose.x = pose_message->x;
  turtlesim_pose.y = pose_message->y;
  turtlesim_pose.theta = pose_message->theta;
}
