import os
from multiprocessing import cpu_count
from toolchain import Recipe, shprint
import sh

class PyeoskitRecipe(Recipe):
    version = '0.5'
    url = 'https://github.com/learnforpractice/pyeoskit-phone/archive/0.5.zip'
    depends = ['python3']
    libraries = [
        "build/main/lib_pyeoskit.a", 
        "build/deps/src/mpir-build/libmpir.a",
        "build/libraries/fc/secp256k1/libsecp256k1.a"
    ]
    def build_arch(self, arch):
        source_dir = self.get_build_dir(arch.arch)
        build_dir = os.path.join(self.get_build_dir(arch.arch), 'build')
#        shprint(sh.rm, '-rf', build_dir)
        shprint(sh.mkdir, '-p', build_dir)
        os.chdir(build_dir)
        shprint(sh.cmake, build_dir,
                "-DIOS_ARCH=arm64",
#                "-DIOS_PLATFORM=OS64",
                "-DENABLE_BITCODE=FALSE",
                '-DCMAKE_TOOLCHAIN_FILE={}'.format(
                    os.path.join(source_dir, 'ios-cmake/ios.toolchain.cmake')),
                '-DCMAKE_BUILD_TYPE=Release',
                '-DBUILD_SHARED_LIBS=0',
                '..',
                )
        shprint(sh.make, '-j' + str(cpu_count()))

recipe = PyeoskitRecipe()
