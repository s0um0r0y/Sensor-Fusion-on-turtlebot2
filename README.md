# Camera-and-LIDAR-Fusion
I am working in the G.D Naidu Robotics Lab in VIT Vellore on creating an autonomous navigation stack for turtlebot 2 combined with sensor fusion technology to combine the data coming from `2D RP LIDAR` and `RGBD camera` to create a 3-D map with depth information.

## Introduction

### Turtlebot 2

This project is done in Linux operationg system version `20.04 LTS` , and implemented on `Turtlebot2 robot`, ROS which is a middleware operating system in astra version.Our Turtlebot2, equipped with a `RP LIDAR A1M8` and an `Orbec astra camera` for depth sensing.

### Dependencies
-  Hector_SLAM
-  Gmapping
-  RTAB Mapping
-  PCL_conversion
-  Actionlib

### Hectorslam on RPlidar

We implemented the [hectorslam](https://github.com/tu-darmstadt-ros-pkg/hector_slam) to get a 2D map of the robotics lab in VIT. This map lacks 3D depth information of the environment so we plan to use a depth camera(Orbec astra) to get the depth information of the environment.

### Point cloud data from Orbec Astra depth camera

Here we are able to visualise the point cloud data from the Orbec astra depth camera. We plan to combine this information with the data coming from the RPlidar .

### RTAB Mapping

We made a dataset using RTAB Mapping with the features of the environment

