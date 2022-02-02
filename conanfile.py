from conans import ConanFile, CMake, tools
from conans.model.version import Version


class QualisysCppSDKConan(ConanFile):
    name = "qualisys_cpp_sdk"
    version = "1.23"
    license = "MIT"
    author = "SINTEF Ocean"
    url = "https://github.com/qualisys/qualisys_cpp_sdk"
    homepage = "https://www.qualisys.com/"
    description = "C++ library to interface with Qualisys motion capture systen in real-time"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "cmake_find_package"

    scm = {
        "type": "git",
        "url": "https://github.com/qualisys/qualisys_cpp_sdk",
        "revision": "rt_protocol_{}".format(version),
        }

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def source(self):
        tools.replace_in_file("Network.h",
                            "#ifdef _WIN32",
                            '''#ifdef _WIN32
// BEGIN CONAN PATCH
#pragma comment(lib, "Ws2_32.lib")
// END CONAN PATCH''')



    def package_info(self):
        self.cpp_info.name = 'qualisys_cpp_sdk'
        self.cpp_info.libs = ["qualisys_cpp_sdk"]
        self.cpp_info.includedirs.extend(["include/qualisys_cpp_sdk"])