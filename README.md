### `box_bot_description`

#### `box_bot_gazebo`

These repos go together. [`box_bot_gazebo`](https://github.com/ivogeorg/box_bot_gazebo) uses this package to populate the robot in Gazebo.

#### Notes
1. The wheels are rotated in the link, not the joint.
2. Each wheel is rotated around two axes to avoid the differential drive moving the robot opposite the sign of the linear velocity component.
3. Same with the caster-wheel cylindrical components.

#### Frames

`ros2 run rqt_tf_tree rqt_tf_tree`  

![Box bot frame diagram](assets/frames.png)  

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

