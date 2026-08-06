add_compile_options(-std=c++17)

find_package(catkin REQUIRED COMPONENTS
  )

catkin_package(
  CFG_EXTRAS model_convert.cmake #https://answers.ros.org/question/243016/add_definitions-package-exportation/
)
