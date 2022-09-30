#!/usr/bin/env python

#--------Include modules---------------
import rospy
import tf
from nav_msgs.msg import OccupancyGrid

# global parameter  ------------------------------
mapData              = OccupancyGrid()

# Subscribers' callbacks ------------------------------
def mapCallBack(data):
	global mapData
	mapData=data


# main node  ------------------------------
def node():
    global mapData
    rospy.init_node('map_listen', anonymous=False)

    map_Topic         = rospy.get_param('~map_Topic', '/map')   # map topic


    rospy.Subscriber(map_Topic, OccupancyGrid, mapCallBack)

    # function for waiting map
    while (len(mapData.data) < 1):
        rospy.loginfo('Waiting for the map')
        rospy.sleep(0.1)
        pass

    while not rospy.is_shutdown():
        print(mapData.header)
        print("There is map data")
        rospy.sleep(0.5)

# main function  ------------------------------
if __name__ == '__main__':
    try:
        node()
    except rospy.ROSInterruptException:
        pass
 
