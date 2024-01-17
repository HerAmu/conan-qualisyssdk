cmake_minimum_required(VERSION 3.15)
project(test_package)

find_package(qualisys_cpp_sdk REQUIRED)

add_executable(test_pkg test_package.cpp)
target_link_libraries(test_pkg PRIVATE qualisys_cpp_sdk::qualisys_cpp_sdk)
