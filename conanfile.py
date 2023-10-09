from os.path import join
from conan import ConanFile
from conan.tools.files import get, copy
from conan.tools.files import replace_in_file, rmdir
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.scm import Git
from conan.tools.env import Environment

required_conan_version = ">=1.53.0"


class QualisysCppSDKConan(ConanFile):
    name = "qualisys_cpp_sdk"
    license = "MIT"
    author = "SINTEF Ocean"
    url = "https://github.com/sintef-ocean/conan-qualisys-cpp-sdk"
    homepage = "https://github.com/qualisys/qualisys_cpp_sdk"
    description = "C++ library to interface with Qualisys motion capture systen in real-time"
    settings = "os", "compiler", "build_type", "arch"
    package_type = "static-library"
    generators = "CMakeToolchain"

    def layout(self):
        cmake_layout(self, src_folder="src")

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

        replace_in_file(self, join(self.source_folder, "CMakeLists.txt"),
                        "include(GNUInstallDirs)",
                        "project(qualisys_cpp_sdk CXX)")

        replace_in_file(self, join(self.source_folder, "CMakeLists.txt"),
                        "project(qualisys_cpp_sdk)",
                        "include(GNUInstallDirs)")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        lib = self.name
        if self.settings.build_type == "Debug":
            lib += "-d"
        self.cpp_info.libs = [lib]
        self.cpp_info.includedirs.extend([f"include/{self.name}"])
        if self.settings.os == "Windows":
            self.cpp_info.system_libs = ["ws2_32"]
