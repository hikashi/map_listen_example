cmake_minimum_required(VERSION 2.8.3)
project(map-listen)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  nav_msgs
  roscpp
  rospy
  std_msgs
  tf
  visualization_msgs
  message_generation
)


generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
)


catkin_package( 

CATKIN_DEPENDS message_runtime
)
