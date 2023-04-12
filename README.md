# Camera-and-LIDAR-Fusion
I am working in the G.D Naidu Robotics Lab in VIT Vellore on creating an autonomous navigation stack for turtlebot 2 combined with sensor fusion technology to combine the data coming from LIDAR and RGBD camera to create a 3-D map with depth information. I used ROS and RVIZ for the map implementation.

## Introduction

### Turtlebot 2

This project is done in Linux operationg system version 16.04.6 LTS, and implemented on Turtlebot2 robot, ROS which is a middleware operating system in Kinetic version. Find below a hardware description of our Turtlebot2, equipped with a 2D RP LIDAR and a Kinect for depth sensing.

![image](https://user-images.githubusercontent.com/75070782/215652428-9b217416-6f13-4685-a554-5035e962d97d.png)

### Hectorslam on RPlidar

We implemented the hectorslam with gmaping to get a 2D map of the robotics lab in VIT. This map lacks depth information of the environment so we plan to use a depth camera(Orbec astra) to get the depth information of the environment.

![Screenshot from 2023-03-19 14-19-28](https://user-images.githubusercontent.com/75070782/231346305-6b774692-023d-4563-b199-49e859eb7120.png)

### Point cloud data from Orbec Astra depth camera

Here we are able to visualise the point cloud data from the Orbec astra depth camera. We plan to combine this information with the data coming from the RPlidar .

![Screenshot from 2023-03-19 18-11-21](https://user-images.githubusercontent.com/75070782/231347174-9e63691f-fdde-496e-9467-2b7439a0289b.png)

### RTAB Mapping

We made a dataset using RTAB Mapping with the features of the environment

![Screenshot from 2023-03-23 18-07-24](https://user-images.githubusercontent.com/75070782/231347629-a1592ee7-50f2-49e9-ab40-01f501aa1db0.png)

We are still trying to fuse the data of the LIDAR and the depth camera and this is the progress as of now

![Screenshot from 2023-03-25 16-07-25 (copy)](https://user-images.githubusercontent.com/75070782/231347887-7c59e257-0c5a-4a10-9688-dc72910630ba.png)

