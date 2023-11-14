from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='1.0.0',
    packages=find_packages(exclude=['config', 'notebooks']),  # Add 'aihao' as the parameter
    package_dir={'': 'aihao'},  # Specify the 'src' directory
    # other setup parameters...
)
