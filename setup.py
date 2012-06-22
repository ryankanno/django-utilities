import os
from distutils.core import setup


def find_packages(package_dir):
    packages, package_data = [], {}

    root_dir = os.path.dirname(__file__)
    if root_dir:
        os.chdir(root_dir)

    for dirpath, dirnames, filenames in sorted(os.walk(package_dir)):
        for i, dirname in enumerate(dirnames):
            if dirname.startswith('.'): 
                del dirnames[i]

        if '__init__.py' in filenames:
            pkg = dirpath.replace(os.path.sep, '.')
            if os.path.altsep:
                pkg = pkg.replace(os.path.altsep, '.')
            packages.append(pkg)

        elif filenames:
            curr_pack = packages[0] 
            if curr_pack not in package_data:
                package_data[curr_pack] = []
            package_dir = "/".join(curr_pack.split(".")) + "/"
            for f in filenames:
                package_data[curr_pack].append(os.path.join(dirpath.replace(package_dir, ""), f))

    return packages, package_data 


packages, package_data = find_packages('utilities')

setup(name='django-utilities',
      version='0.1.0',
      description='A set of utilities for use within Django apps',
      author='Ryan Kanno',
      author_email='ryankanno@localkinegrinds.com',
      packages=packages,
      package_data=package_data,
      long_description=open('README.txt').read(),
      install_requires=[
        "Django >= 1.4.0"
      ]
)
