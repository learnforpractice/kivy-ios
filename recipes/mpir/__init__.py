import os
from multiprocessing import cpu_count
from toolchain import Recipe, shprint
import sh

class MpirRecipe(Recipe):
    version = '0.5'
    url = 'https://github.com/chfast/mpir/archive/cmake.tar.gz'
    depends = []
    libraries = ["build/libmpir.a"]
    include_dir = [
        ("build/gmp.h", ""),
        ("build/mpir.h", "")
        ]

    def prebuild_arch(self, arch):
        # common to all archs
        if  self.has_marker("patched"):
            return
        self.apply_patch("CMakeLists.txt.patch")

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
                    os.path.join(self.ctx.root_dir, '..', 'ios-cmake/ios.toolchain.cmake')),
                "-DMPIR_GMP=On",
                '-DCMAKE_BUILD_TYPE=Release',
                '-DBUILD_SHARED_LIBS=0',
                '..',
                )
        shprint(sh.make, '-j' + str(cpu_count()))

recipe = MpirRecipe()
