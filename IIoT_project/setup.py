import os
from glob import glob
from setuptools import setup

package_name = 'IIoT_project'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Giovanni',
    maintainer_email='giovanni.arlo99@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'offboard_control = IIoT_project.offboard_control:main',
                'velocity_control = IIoT_project.velocity_control:main',
                'velocity2_control = IIoT_project.velocity2_control:main',
                'control = IIoT_project.control:main',
                'control2 = IIoT_project.control2:main',
                'processes = IIoT_project.processes:main'
        ],
    },
)