import json
s = {'hostpython': 'hostpython2', 'python': 'python2', 'hostlibffi.archive_root': 'libffi-3.2.1', 'hostlibffi.download': True, 'hostlibffi.download.at': '2018-12-21 08:47:34.740921', 'hostlibffi.extract': True, 'hostlibffi.extract.at': '2018-12-21 08:47:34.867069', 'hostlibffi.build.x86_64': True, 'hostlibffi.build.x86_64.at': '2018-12-21 08:47:47.438259', 'libffi.archive_root': 'libffi-3.2.1', 'libffi.download': True, 'libffi.download.at': '2018-12-21 08:48:01.372101', 'libffi.extract': True, 'libffi.extract.at': '2018-12-21 08:48:01.746250', 'libffi.build.x86_64': True, 'libffi.build.x86_64.at': '2018-12-21 08:48:47.113276', 'libffi.build.armv7': True, 'libffi.build.armv7.at': '2018-12-21 08:49:31.087879', 'libffi.build.arm64': True, 'libffi.build.arm64.at': '2018-12-21 08:50:15.937770', 'libffi.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libffi.a': True, 'libffi.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libffi.a.at': '2018-12-21 08:50:15.987278', 'libffi.install_include': True, 'libffi.install_include.at': '2018-12-21 08:50:15.994127', 'libffi.install_frameworks': True, 'libffi.install_frameworks.at': '2018-12-21 08:50:15.994745', 'libffi.install_sources': True, 'libffi.install_sources.at': '2018-12-21 08:50:15.995467', 'libffi.install': True, 'libffi.install.at': '2018-12-21 08:50:15.995998', 'libffi.build_all': True, 'libffi.build_all.at': '2018-12-21 08:50:15.996553', 'hostpython2.archive_root': 'Python-2.7.1', 'hostpython2.download': True, 'hostpython2.download.at': '2018-12-21 08:51:02.651233', 'hostpython2.extract': True, 'hostpython2.extract.at': '2018-12-21 08:51:06.012493', 'hostpython2.build.x86_64': True, 'hostpython2.build.x86_64.at': '2018-12-21 08:51:38.189821', 'hostpython2.install_include': True, 'hostpython2.install_include.at': '2018-12-21 08:51:38.190650', 'hostpython2.install_frameworks': True, 'hostpython2.install_frameworks.at': '2018-12-21 08:51:38.191420', 'hostpython2.install_sources': True, 'hostpython2.install_sources.at': '2018-12-21 08:51:38.192228', 'hostpython2.build_all': True, 'hostpython2.build_all.at': '2018-12-21 08:51:53.148663', 'freetype.archive_root': 'freetype-2.5.5', 'freetype.download': True, 'freetype.download.at': '2018-12-21 08:57:46.866899', 'freetype.extract': True, 'freetype.extract.at': '2018-12-21 08:57:47.521592', 'freetype.build.arm64': True, 'freetype.build.arm64.at': '2018-12-21 08:57:59.246215', 'freetype.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libfreetype.a': True, 'freetype.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libfreetype.a.at': '2018-12-21 08:57:59.300931', 'freetype.install_include': True, 'freetype.install_include.at': '2018-12-21 08:57:59.345650', 'freetype.install_frameworks': True, 'freetype.install_frameworks.at': '2018-12-21 08:57:59.346767', 'freetype.install_sources': True, 'freetype.install_sources.at': '2018-12-21 08:57:59.347960', 'freetype.install': True, 'freetype.install.at': '2018-12-21 08:57:59.349481', 'freetype.build_all': True, 'freetype.build_all.at': '2018-12-21 08:57:59.350689', 'libjpeg.archive_root': 'jpeg-9a', 'libjpeg.download': True, 'libjpeg.download.at': '2018-12-21 08:58:03.221606', 'libjpeg.extract': True, 'libjpeg.extract.at': '2018-12-21 08:58:03.317741', 'libjpeg.build.arm64': True, 'libjpeg.build.arm64.at': '2018-12-21 08:58:10.338065', 'libjpeg.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libjpeg.a': True, 'libjpeg.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libjpeg.a.at': '2018-12-21 08:58:10.380521', 'libjpeg.install_include': True, 'libjpeg.install_include.at': '2018-12-21 08:58:10.383802', 'libjpeg.install_frameworks': True, 'libjpeg.install_frameworks.at': '2018-12-21 08:58:10.384786', 'libjpeg.install_sources': True, 'libjpeg.install_sources.at': '2018-12-21 08:58:10.385673', 'libjpeg.install': True, 'libjpeg.install.at': '2018-12-21 08:58:10.386521', 'libjpeg.build_all': True, 'libjpeg.build_all.at': '2018-12-21 08:58:10.387494', 'sdl2.archive_root': 'SDL2-2.0.8', 'sdl2.download': True, 'sdl2.download.at': '2018-12-21 08:59:13.060642', 'sdl2.extract': True, 'sdl2.extract.at': '2018-12-21 08:59:13.630964', 'sdl2.build.arm64': True, 'sdl2.build.arm64.at': '2018-12-21 08:59:16.721069', 'sdl2.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libsdl2.a': True, 'sdl2.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libsdl2.a.at': '2018-12-21 08:59:16.786223', 'sdl2.install_include': True, 'sdl2.install_include.at': '2018-12-21 08:59:16.821069', 'sdl2.install_frameworks': True, 'sdl2.install_frameworks.at': '2018-12-21 08:59:16.822360', 'sdl2.install_sources': True, 'sdl2.install_sources.at': '2018-12-21 08:59:16.823662', 'sdl2.install': True, 'sdl2.install.at': '2018-12-21 08:59:16.824757', 'sdl2.build_all': True, 'sdl2.build_all.at': '2018-12-21 08:59:16.825733', 'sdl2_image.archive_root': 'SDL2_image-2.0.0', 'sdl2_image.download': True, 'sdl2_image.download.at': '2018-12-21 09:00:04.968547', 'sdl2_image.extract': True, 'sdl2_image.extract.at': '2018-12-21 09:00:05.556440', 'sdl2_image.build.arm64': True, 'sdl2_image.build.arm64.at': '2018-12-21 09:00:07.972730', 'sdl2_image.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libsdl2_image.a': True, 'sdl2_image.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libsdl2_image.a.at': '2018-12-21 09:00:08.013716', 'sdl2_image.install_include': True, 'sdl2_image.install_include.at': '2018-12-21 09:00:08.015598', 'sdl2_image.install_frameworks': True, 'sdl2_image.install_frameworks.at': '2018-12-21 09:00:08.016746', 'sdl2_image.install_sources': True, 'sdl2_image.install_sources.at': '2018-12-21 09:00:08.017781', 'sdl2_image.install': True, 'sdl2_image.install.at': '2018-12-21 09:00:08.019057', 'sdl2_image.build_all': True, 'sdl2_image.build_all.at': '2018-12-21 09:00:08.020112', 'sdl2_mixer.archive_root': 'SDL2_mixer-2.0.0', 'sdl2_mixer.download': True, 'sdl2_mixer.download.at': '2018-12-21 09:00:58.522497', 'sdl2_mixer.extract': True, 'sdl2_mixer.extract.at': '2018-12-21 09:00:59.278803', 'sdl2_mixer.build.arm64': True, 'sdl2_mixer.build.arm64.at': '2018-12-21 09:01:04.637571', 'sdl2_mixer.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libsdl2_mixer.a': True, 'sdl2_mixer.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libsdl2_mixer.a.at': '2018-12-21 09:01:04.689340', 'sdl2_mixer.install_include': True, 'sdl2_mixer.install_include.at': '2018-12-21 09:01:04.691859', 'sdl2_mixer.install_frameworks': True, 'sdl2_mixer.install_frameworks.at': '2018-12-21 09:01:04.693255', 'sdl2_mixer.install_sources': True, 'sdl2_mixer.install_sources.at': '2018-12-21 09:01:04.694659', 'sdl2_mixer.install': True, 'sdl2_mixer.install.at': '2018-12-21 09:01:04.696128', 'sdl2_mixer.build_all': True, 'sdl2_mixer.build_all.at': '2018-12-21 09:01:04.697442', 'sdl2_ttf.archive_root': 'SDL2_ttf-2.0.12', 'sdl2_ttf.download': True, 'sdl2_ttf.download.at': '2018-12-21 09:01:29.949200', 'sdl2_ttf.extract': True, 'sdl2_ttf.extract.at': '2018-12-21 09:01:30.336802', 'sdl2_ttf.build.arm64': True, 'sdl2_ttf.build.arm64.at': '2018-12-21 09:01:30.593798', 'sdl2_ttf.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libsdl2_ttf.a': True, 'sdl2_ttf.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libsdl2_ttf.a.at': '2018-12-21 09:01:30.634907', 'sdl2_ttf.install_include': True, 'sdl2_ttf.install_include.at': '2018-12-21 09:01:30.637377', 'sdl2_ttf.install_frameworks': True, 'sdl2_ttf.install_frameworks.at': '2018-12-21 09:01:30.638748', 'sdl2_ttf.install_sources': True, 'sdl2_ttf.install_sources.at': '2018-12-21 09:01:30.640568', 'sdl2_ttf.build_all': True, 'sdl2_ttf.build_all.at': '2018-12-21 09:01:30.642439', 'host_setuptools.archive_root': 'setuptools', 'host_setuptools.download': True, 'host_setuptools.download.at': '2018-12-21 09:01:30.644449', 'host_setuptools.extract': True, 'host_setuptools.extract.at': '2018-12-21 09:01:30.645568', 'host_setuptools.install_include': True, 'host_setuptools.install_include.at': '2018-12-21 09:01:30.646886', 'host_setuptools.install_frameworks': True, 'host_setuptools.install_frameworks.at': '2018-12-21 09:01:30.648045', 'host_setuptools.install_sources': True, 'host_setuptools.install_sources.at': '2018-12-21 09:01:30.649221', 'host_setuptools.install': True, 'host_setuptools.install.at': '2018-12-21 09:01:30.650356', 'host_setuptools.build_all': True, 'host_setuptools.build_all.at': '2018-12-21 09:01:30.651494', 'libzbar.archive_root': 'ZBar-0.10', 'libzbar.download': True, 'libzbar.download.at': '2018-12-21 09:01:35.702069', 'libzbar.extract': True, 'libzbar.extract.at': '2018-12-21 09:01:35.819143', 'libzbar.build.arm64': True, 'libzbar.build.arm64.at': '2018-12-21 09:02:00.270853', 'libzbar.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libzbar.a': True, 'libzbar.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libzbar.a.at': '2018-12-21 09:02:00.311401', 'libzbar.install_include': True, 'libzbar.install_include.at': '2018-12-21 09:02:00.320446', 'libzbar.install_frameworks': True, 'libzbar.install_frameworks.at': '2018-12-21 09:02:00.321735', 'libzbar.install_sources': True, 'libzbar.install_sources.at': '2018-12-21 09:02:00.322875', 'libzbar.install': True, 'libzbar.install.at': '2018-12-21 09:02:00.324039', 'libzbar.build_all': True, 'libzbar.build_all.at': '2018-12-21 09:02:00.325201', 'ios.archive_root': 'src', 'ios.download': True, 'ios.download.at': '2018-12-21 09:02:00.327053', 'ios.extract': True, 'ios.extract.at': '2018-12-21 09:02:00.332524', 'ios.build.arm64': True, 'ios.build.arm64.at': '2018-12-21 09:02:02.938289', 'ios.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libios.a': True, 'ios.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libios.a.at': '2018-12-21 09:02:02.979805', 'ios.install_include': True, 'ios.install_include.at': '2018-12-21 09:02:02.981807', 'ios.install_frameworks': True, 'ios.install_frameworks.at': '2018-12-21 09:02:02.983683', 'ios.install_sources': True, 'ios.install_sources.at': '2018-12-21 09:02:02.985096', 'ios.build_all': True, 'ios.build_all.at': '2018-12-21 09:02:03.228453', 'pkgresources.archive_root': '', 'pkgresources.download': True, 'pkgresources.download.at': '2018-12-21 09:02:03.231294', 'pkgresources.extract': True, 'pkgresources.extract.at': '2018-12-21 09:02:03.232616', 'pkgresources.install_include': True, 'pkgresources.install_include.at': '2018-12-21 09:02:03.234071', 'pkgresources.install_frameworks': True, 'pkgresources.install_frameworks.at': '2018-12-21 09:02:03.235536', 'pkgresources.install_sources': True, 'pkgresources.install_sources.at': '2018-12-21 09:02:03.236969', 'pkgresources.install': True, 'pkgresources.install.at': '2018-12-21 09:02:03.238363', 'pkgresources.build_all': True, 'pkgresources.build_all.at': '2018-12-21 09:02:03.239762', 'pycrypto.archive_root': 'pycrypto-2.6.1', 'pycrypto.download': True, 'pycrypto.download.at': '2018-12-21 09:02:07.908510', 'pycrypto.extract': True, 'pycrypto.extract.at': '2018-12-21 09:02:08.025898', 'pycrypto.build.arm64': True, 'pycrypto.build.arm64.at': '2018-12-21 09:02:13.587139', 'pycrypto.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libpycrypto.a': True, 'pycrypto.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libpycrypto.a.at': '2018-12-21 09:02:13.626792', 'pycrypto.install_include': True, 'pycrypto.install_include.at': '2018-12-21 09:02:13.628407', 'pycrypto.install_frameworks': True, 'pycrypto.install_frameworks.at': '2018-12-21 09:02:13.630524', 'pycrypto.install_sources': True, 'pycrypto.install_sources.at': '2018-12-21 09:02:13.632659', 'pycrypto.build_all': True, 'pycrypto.build_all.at': '2018-12-21 09:02:14.171174', 'pyobjus.archive_root': 'pyobjus-master', 'pyobjus.download': True, 'pyobjus.download.at': '2018-12-21 09:02:17.116817', 'pyobjus.extract': True, 'pyobjus.extract.at': '2018-12-21 09:02:17.180521', 'pyobjus.build.arm64': True, 'pyobjus.build.arm64.at': '2018-12-21 09:02:34.914982', 'pyobjus.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libpyobjus.a': True, 'pyobjus.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libpyobjus.a.at': '2018-12-21 09:02:34.969391', 'pyobjus.install_include': True, 'pyobjus.install_include.at': '2018-12-21 09:02:34.972897', 'pyobjus.install_frameworks': True, 'pyobjus.install_frameworks.at': '2018-12-21 09:02:34.974780', 'pyobjus.install_sources': True, 'pyobjus.install_sources.at': '2018-12-21 09:02:34.976520', 'pyobjus.install': True, 'pyobjus.install.at': '2018-12-21 09:02:35.494857', 'pyobjus.build_all': True, 'pyobjus.build_all.at': '2018-12-21 09:02:35.496335', 'kivy.archive_root': 'kivy-1.10.1', 'kivy.download': True, 'kivy.download.at': '2018-12-21 09:06:35.450900', 'kivy.extract': True, 'kivy.extract.at': '2018-12-21 09:06:36.114410', 'kivy.build.arm64': True, 'kivy.build.arm64.at': '2018-12-21 09:08:48.212637', 'kivy.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libkivy.a': True, 'kivy.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libkivy.a.at': '2018-12-21 09:08:48.319731', 'kivy.install_include': True, 'kivy.install_include.at': '2018-12-21 09:08:48.322869', 'kivy.install_frameworks': True, 'kivy.install_frameworks.at': '2018-12-21 09:08:48.324954', 'kivy.install_sources': True, 'kivy.install_sources.at': '2018-12-21 09:08:48.326807', 'kivy.install': True, 'kivy.install.at': '2018-12-21 09:08:51.157649', 'kivy.build_all': True, 'kivy.build_all.at': '2018-12-21 09:08:51.159132', 'pil.archive_root': 'Pillow-2.8.2', 'pil.download': True, 'pil.download.at': '2018-12-21 09:09:24.448924', 'pil.extract': True, 'pil.extract.at': '2018-12-21 09:09:24.706470', 'pil.build.arm64': True, 'pil.build.arm64.at': '2018-12-21 09:09:26.789803', 'pil.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libpil.a': True, 'pil.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libpil.a.at': '2018-12-21 09:09:26.831751', 'pil.install_include': True, 'pil.install_include.at': '2018-12-21 09:09:26.833969', 'pil.install_frameworks': True, 'pil.install_frameworks.at': '2018-12-21 09:09:26.835711', 'pil.install_sources': True, 'pil.install_sources.at': '2018-12-21 09:09:26.837724', 'pil.build_all': True, 'pil.build_all.at': '2018-12-21 09:09:28.590128', 'openssl.archive_root': 'openssl-1.0.2k', 'openssl.download': True, 'openssl.download.at': '2018-12-21 09:57:43.911215', 'openssl.extract': True, 'openssl.extract.at': '2018-12-21 09:57:45.848968', 'openssl.build.x86_64': True, 'openssl.build.x86_64.at': '2018-12-21 09:58:20.908431', 'openssl.build.armv7': True, 'openssl.build.armv7.at': '2018-12-21 09:58:43.959179', 'openssl.build.arm64': True, 'openssl.build.arm64.at': '2018-12-21 09:58:56.299687', 'openssl.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libssl.a.libssl.a': True, 'openssl.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libssl.a.libssl.a.at': '2018-12-21 09:58:56.355414', 'openssl.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libcrypto.a.libcrypto.a': True, 'openssl.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libcrypto.a.libcrypto.a.at': '2018-12-21 09:58:56.463651', 'openssl.install_include': True, 'openssl.install_include.at': '2018-12-21 09:58:56.571327', 'openssl.install_frameworks': True, 'openssl.install_frameworks.at': '2018-12-21 09:58:56.572827', 'openssl.install_sources': True, 'openssl.install_sources.at': '2018-12-21 09:58:56.574337', 'openssl.install': True, 'openssl.install.at': '2018-12-21 09:58:56.575842', 'openssl.build_all': True, 'openssl.build_all.at': '2018-12-21 09:58:56.577367', 'libiconv.archive_root': 'libiconv-1.15', 'libiconv.download': True, 'libiconv.download.at': '2018-12-24 03:00:51.635871', 'libiconv.extract': True, 'libiconv.extract.at': '2018-12-24 03:00:51.965465', 'libiconv.build.arm64': True, 'libiconv.build.arm64.at': '2018-12-24 03:01:42.245493', 'libiconv.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libiconv.a': True, 'libiconv.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libiconv.a.at': '2018-12-24 03:01:42.290809', 'libiconv.install_include': True, 'libiconv.install_include.at': '2018-12-24 03:01:42.293349', 'libiconv.install_frameworks': True, 'libiconv.install_frameworks.at': '2018-12-24 03:01:42.296215', 'libiconv.install_sources': True, 'libiconv.install_sources.at': '2018-12-24 03:01:42.298368', 'libiconv.install': True, 'libiconv.install.at': '2018-12-24 03:01:42.300422', 'libiconv.build_all': True, 'libiconv.build_all.at': '2018-12-24 03:01:42.302120', 'python2.archive_root': 'Python-2.7.1', 'python2.download': True, 'python2.download.at': '2018-12-24 03:02:45.274103', 'python2.extract': True, 'python2.extract.at': '2018-12-24 03:02:49.183092', 'python2.build.arm64': True, 'python2.build.arm64.at': '2018-12-24 03:03:38.722031', 'python2.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libpython2.a': True, 'python2.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libpython2.a.at': '2018-12-24 03:03:38.824796', 'python2.install_include': True, 'python2.install_include.at': '2018-12-24 03:03:38.827119', 'python2.install_frameworks': True, 'python2.install_frameworks.at': '2018-12-24 03:03:38.828805', 'python2.install_sources': True, 'python2.install_sources.at': '2018-12-24 03:03:38.830583', 'python2.build_all': True, 'python2.build_all.at': '2018-12-24 03:04:04.535620', 'zbarlight.archive_root': 'zbarlight-1.2', 'zbarlight.download': True, 'zbarlight.download.at': '2018-12-24 04:34:43.327913', 'zbarlight.extract': True, 'zbarlight.extract.at': '2018-12-24 04:34:43.443885', 'zbarlight.build.arm64': True, 'zbarlight.build.arm64.at': '2018-12-24 04:47:44.269688', 'zbarlight.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libzbarlight.a': True, 'zbarlight.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libzbarlight.a.at': '2018-12-24 04:47:44.308234', 'zbarlight.install_include': True, 'zbarlight.install_include.at': '2018-12-24 04:47:44.311385', 'zbarlight.install_frameworks': True, 'zbarlight.install_frameworks.at': '2018-12-24 04:47:44.313728', 'zbarlight.install_sources': True, 'zbarlight.install_sources.at': '2018-12-24 04:47:44.315882', 'zbarlight.build_all': True, 'zbarlight.build_all.at': '2018-12-24 04:47:44.321770'}


#with open('dist/state.db', 'w') as f:
#	json.dump(s, f)

with open('dist/state.db', 'r') as f:
	state = json.load(f)
keys = ['sdl2.build.arm64',
'sdl2.build.arm64.at 2018-12-21 08:59:16.721069',
'sdl2.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libsdl2.a',
'sdl2.make_lipo./Users/newworld/dev/kivy/kivy-ios-python2/dist/lib/libsdl2.a.at',
'sdl2.install_include',
'sdl2.install_include.at',
'sdl2.install_frameworks',
'sdl2.install_frameworks.at',
'sdl2.install_sources',
'sdl2.install_sources.at',
'sdl2.install',
'sdl2.install.at',
'sdl2.build_all',
'sdl2.build_all.at',
'sdl2.build.arm64.at']
for key in keys:
	if key in state:
		del state[key]

for key in state:
	if key.startswith('sdl2.'):
		print(key, state[key])

with open('dist/state.db', 'w') as f:
	json.dump(state, f)


