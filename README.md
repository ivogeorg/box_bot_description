### box_bot_description

#### box_bot_gazebo

These repos go together. [`box_bot_gazebo`](https://github.com/ivogeorg/box_bot_gazebo) uses this package to populate the robot in Gazebo.

#### Notes
1. The wheels are rotated in the link, not the joint.
2. Each wheel is rotated around two axes to avoid the differential drive moving the robot opposite the sign of the linear velocity component.
3. Same with the caster-wheel cylindrical components.

#### Frames

`ros2 run rqt_tf_tree rqt_tf_tree`  

![Box bot frame diagram](assets/frames.png)  

#### Rviz2

##### 1. Geometric
![Geometric bot](assets/box_bot_geometric.png)  

##### 2. Mesh
![Mesh bot](assets/box_bot_mesh.png)  

