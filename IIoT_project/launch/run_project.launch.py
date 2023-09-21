#!/usr/bin/env python
__author__ = "Giovanni"
__contact__ = ""

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    package_dir = get_package_share_directory('IIoT_project')
    return LaunchDescription([
        Node(
            package='IIoT_project',
            namespace='IIoT_project',
            executable='processes',
            name='processes',
            prefix='gnome-terminal --'
        ),
        Node(
            package='IIoT_project',
            namespace='IIoT_project',
            executable='control',
            name='control',
            prefix='gnome-terminal --',
        ),
        Node(
            package='IIoT_project',
            namespace='IIoT_project',
            executable='control2',
            name='control',
            prefix='gnome-terminal --',
        ),
        Node(
            package='IIoT_project',
            namespace='IIoT_project',
            executable='velocity_control',
            name='velocity'
        ),
        Node(
            package='IIoT_project',
            namespace='IIoT_project',
            executable='velocity2_control',
            name='velocity2'
        ),

    ])
