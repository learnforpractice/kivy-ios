import os
from toolchain import Recipe, shprint
from os.path import join
import sh
import fnmatch
from distutils.dir_util import copy_tree

class PyZBarRecipe(Recipe):

    version = '0.1.7'

    url = 'https://github.com/NaturalHistoryMuseum/pyzbar/archive/v{version}.tar.gz'  # noqa

    call_hostpython_via_targetpython = False

    depends = ['libzbar']

    def get_recipe_env(self, arch=None):
        env = super(PyZBarRecipe, self).get_recipe_env(arch)
        libzbar = self.get_recipe('libzbar', self.ctx)
        libzbar_dir = libzbar.get_build_dir(arch.arch)
        env['CFLAGS'] += ' -I' + join(libzbar_dir, 'include')
        env['LDFLAGS'] += ' -L' + join(libzbar_dir, 'zbar', '.libs')
        env['LIBS'] = env.get('LIBS', '') + ' -lzbar'
        return env

    def install(self):
        arch = list(self.filtered_archs)[0]
        build_dir = join(self.get_build_dir(arch.arch),'pyzbar')
        dist_dir  = join(self.ctx.dist_dir,'root','python3','lib','python3.7','site-packages','pyzbar')
        copy_tree(build_dir, dist_dir)

recipe = PyZBarRecipe()
