### `box_bot_description`

#### `box_bot_gazebo`

These repos go together. [`box_bot_gazebo`](https://github.com/ivogeorg/box_bot_gazebo) uses this package to populate the robot in Gazebo.

#### Notes
1. The wheels are rotated in the link, not the joint.
2. Each wheel is rotated around two axes to avoid the differential drive moving the robot opposite the sign of the linear velocity component.
3. Same with the caster-wheel cylindrical components.

#### Frames

`ros2 run rqt_tf_tree rqt_tf_tree`  

![Box bot frame diagram](assets/box_bot_frames_wheels_and_casters.png)  

#### Rviz2

##### Starting Rviz2 and `joint_state_publisher_gui`

1. Expected [`rviz/urdf_vis.rviz`](rviz/urdf_vis.rviz) config file.
2. In a terminal:
   1. `cd ~/ros2_ws`
   2. `colcon build --packages-select box_bot_description`
   3. `source install/setup.bash`
   4. `ros2 launch box_bot_description urdf_visualize_geometric.launch.py`
3. In another terminal:
   1. `cd ~/ros2_ws`
   2. `source install/setup.bash`
   3. `ros2 launch joint_state_publisher_gui joint_state_publisher_gui`

##### 1. Geometric
![Geometric bot](assets/box_bot_geometric.png)  

##### 2. Mesh
![Mesh bot](assets/box_bot_mesh.png)  

#### Laser sensor link and joint tree

| Rviz1 | `rqt_tf_tree` |
| --- | --- |
| ![Laser sensor subtree (Rviz2)](assets/laser_sensor_subtree_rviz2.png) | ![Laser sensor subtree (rqt_tf_tree)](assets/laser_sensor_subtree_rqt_tf_tree.png) |

1. The laser sensor link and joint tree branches off the `chassis` link with a _prismatic_ joint, which moves up and down the z-axis and holds the rest of the subtree.
2. The `laser_scan_link` is a parent of two joints:
   1. The _fixed_ joint connects the `laser_scan_frame` link to it, and is used to attach the ROS ray sensor plugin, which implements the laser sensor simulation and visualization.
   1. The _continuous_ joint connects the laser sensor housing to it, and it can rotate around the z-axis at a given velocity.

