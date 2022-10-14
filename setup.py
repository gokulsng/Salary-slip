from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in salary_slip/__init__.py
from salary_slip import __version__ as version

setup(
	name="salary_slip",
	version=version,
	description="Gita Press",
	author="Simpel",
	author_email="hello@simpel.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
