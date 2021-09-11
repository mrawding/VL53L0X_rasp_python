cmake_minimum_required(VERSION 3.0.2)
project(vl53l0x_ros)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages

#set(CMAKE_C_FLAGS -O2 -Wall -c)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES ${PROJECT_NAME}
  CATKIN_DEPENDS roscpp std_msgs rospy
  DEPENDS system_lib
)

catkin_install_python(PROGRAMS scripts/test.py scripts/VL53L0X.py scripts/VL53L0X_TCA9548A_example.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)



add_library(${PROJECT_NAME} src/python_lib/vl53l0x_python.c src/api/core/vl53l0x_api_core.c 
                    src/api/core/vl53l0x_api.c src/api/core/vl53l0x_api_ranging.c src/api/core/vl53l0x_api_strings.c
                    src/api/core/vl53l0x_api_calibration.c src/platform/vl53l0x_platform.c

)
target_link_libraries(${PROJECT_NAME} ${CATKIN_LIBRARIES})



#############
## Install ##
#############


 install(TARGETS ${PROJECT_NAME}
   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
 )



