# pure-python package, this can be removed when we'll support any python package
from toolchain import PythonRecipe, shprint
from os.path import join
import sh, os

class IdnaRecipe(PythonRecipe):
    version = "v2.8"
    url = "https://github.com/kjd/idna/archive/{version}.zip"
    depends = ["python3"]
    def install(self):
        arch = list(self.filtered_archs)[0]
        build_dir = self.get_build_dir(arch.arch)
        os.chdir(build_dir)
        hostpython = sh.Command(self.ctx.hostpython)
        build_env = arch.get_env()
        dest_dir = join(self.ctx.dist_dir, "root", "python3")
        site_packages_path = join(dest_dir, 'lib', 'python3.7', 'site-packages')
        build_env['PYTHONPATH'] = site_packages_path
        shprint(hostpython, "setup.py", "install", "--prefix", dest_dir, _env=build_env)

recipe = IdnaRecipe()

