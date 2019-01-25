# _*_ coding:utf-8 _*_

# use install to copy the package to site-package
# use develop to create the link between the python and the package
# register and upload ???

# Installed d:\pythonproject\mywinpy
# Processing dependencies for PKpkg==1.0
# Finished processing dependencies for PKpkg==1.0
# so we should uninstall by command: pip uninstall PKpkg

# pip uninstall PKpkg
from setuptools import setup, find_packages

setup(
    name="PKpkg",
    version="1.0",
    # keywords=("test", "xxx"),
    description="PermanentK's own packages.",
    long_description="None",
    license="MIT Licence",

    url="about:blank",
    author="PermanentK",
    author_email="nhcyk@163.com",

    # packages=find_packages(),  # 自动找
    # packages=['myfileprocessing', 'myweb', 'PKpkg'],  # 自己指定
    # packages=['PKpkg', 'PKpkg.myfileprocessing', 'PKpkg.myweb'],  # 自己指定
    packages=find_packages(),
    namespace_packages=['PKpkg'],
    include_package_data=True,
    platforms="windows",
    # install_requires = ['docutils>=0.3']
    install_requires=['pytube'],
    zip_safe=False,

    # scripts=[],
    # entry_points={
    #     'console_scripts': [
    #         'test = test.help:main'
    #     ]
    # }
)