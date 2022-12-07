from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in customer_feedback/__init__.py
from customer_feedback import __version__ as version

setup(
	name="customer_feedback",
	version=version,
	description="Customer Feedback Form",
	author="Geoffrey Karani",
	author_email="geoffrey.kamundi@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
