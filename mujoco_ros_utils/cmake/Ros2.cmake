# ROS2 build of mujoco_ros_utils.
#
# The package is a model-conversion script plus the config it reads. Nothing is
# compiled; the ROS2 build installs the same files and exports the same
# mujoco_model_convert() macro through ament instead of catkin.

find_package(ament_cmake REQUIRED)

install(PROGRAMS
  scripts/mujoco_model_generator.py
  scripts/convert.py
  DESTINATION share/${PROJECT_NAME}/scripts)

install(DIRECTORY config
  DESTINATION share/${PROJECT_NAME})

# Also as package executables, so `ros2 run mujoco_ros_utils
# mujoco_model_generator.py` works the way `rosrun` did. convert.py goes with
# it: the generator imports it as a sibling module.
install(PROGRAMS
  scripts/mujoco_model_generator.py
  scripts/convert.py
  DESTINATION lib/${PROJECT_NAME})

# No cmake macro on this side, unlike catkin's model_convert.cmake. A robot's
# xacro says $(find <itself>), which under ROS2 resolves through the ament
# index and so needs the package installed - it cannot be generated during that
# package's own build. The generator runs as a separate step against a built
# workspace instead; see .ci/humble.sh in jsk_aerial_robot.
ament_package()
