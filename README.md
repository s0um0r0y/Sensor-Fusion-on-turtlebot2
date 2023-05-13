# Camera-and-LIDAR-Fusion
I am working in the G.D Naidu Robotics Lab in VIT Vellore on creating an autonomous navigation stack for turtlebot 2 combined with sensor fusion technology to combine the data coming from `2D RP LIDAR` and `RGBD camera` to create a 3-D map with depth information.

## Introduction

### Turtlebot 2

This project is done in Linux operationg system version `20.04 LTS` , and implemented on `Turtlebot2 robot`, ROS which is a middleware operating system in astra version.Our Turtlebot2, equipped with a `RP LIDAR A1M8` and an `Orbec astra camera` for depth sensing.

### Dependencies
-  [hectorslam](https://github.com/tu-darmstadt-ros-pkg/hector_slam)
-  [Gmapping](https://wiki.ros.org/slam_gmapping)
-  [RTAB Mapping](http://wiki.ros.org/rtabmap_ros)
-  [PCL_conversion](http://wiki.ros.org/pcl_conversions)
-  [Actionlib](https://wiki.ros.org/actionlib)
-  [turtlebot_viboot](https://github.com/roboticslab-fr/turtlebot_vibot)

## Packages

There are 3 packages here `onboard_turtlebot2_pkg` which has to be run on turtlebot's netbook , `sensor_fusion_1` which contains the static transforms and `workstation_turtlebot2_pkg` which the user has to run on the pc. 

### Installation and run

```bash
#packages installation
$ cd ~/Downloads
$ git clone https://github.com/s0um0r0y/Sensor-Fusion-on-turtlebot2.git
$ cd Sensor-Fusion-on-turtlebot2/

#on turtlebot netbook (each launch has to be on a seperate terminal)

#for mapping
$ cd Sensor-Fusion-on-turtlebot2/
$ roslaunch onboard_turtlebot2_pkg 3d-mapping-rtabmap.launch

#for navigation
$ cd Sensor-Fusion-on-turtlebot2/
$ roslaunch onboard_turtlebot2_pkg 3d-navigation-rtabmap.launch

#on system/pc (each launch has to be on a seperate terminal)

#for mapping
$ cd Sensor-Fusion-on-turtlebot2/
$ roslaunch rplidar_ros rplidar.launch
$ roslaunch astra_camera astra.launch
$ roslaunch sensor_fusion_1 static_tfs_astra_rplidar.launch
$ roslaunch sensor_fusion_1 run_astra_and_rplidar.launch
$ roslaunch workstation_turtlebot2_pkg view-rviz-rtabmap-mapping.launch

#for navigation
$ cd Sensor-Fusion-on-turtlebot2/
$ roslaunch workstation_turtlebot2_pkg view-rviz-rtabmap-navigation.launch

```

