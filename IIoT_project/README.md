# IIoT_project
## Goals of the project
The goal of this project is to create a simulation of different scenario:
* Mission for 2 drones in a not empty world
* Drone backflip 
* Offboard control
* See traffic with Wireshark
## Prerequisites
* ROS2 Humble
* PX4 Autopilot
* Micro XRCE-DDS Agent
* px4_msgs
* Ubuntu 22.04
* Python 3.10
## Setup
### Install PX4 Autopilot
To [Install PX4](https://docs.px4.io/main/en/dev_setup/dev_env_linux_ubuntu.html#simulation-and-nuttx-pixhawk-targets) run this code 
```
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
```

Run this script in a bash shell to install everything

```
bash ./PX4-Autopilot/Tools/setup/ubuntu.sh
```
Before continue, reboot your pc.

### Install ROS2 Humble
To install ROS2 Humble: [here](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)

### Install Dependencies

Install Python dependencies with this code

```
pip3 install --user -U empy pyros-genmsg setuptools
```

And:

```
pip3 install kconfiglib
pip install --user jsonschema
pip install --user jinja2
```

### Build Micro DDS
Follow this [PX4 Docs](https://docs.px4.io/main/en/ros/ros2_comm.html#setup-micro-xrce-dds-agent-client) in order to build MicroDDS on your machine

```
git clone https://github.com/eProsima/Micro-XRCE-DDS-Agent.git
cd Micro-XRCE-DDS-Agent
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig /usr/local/lib/
```
### Install Gazebo Classic
To install Gazebo Classic run this:
```
sudo apt remove gz-garden
sudo apt install aptitude
sudo aptitude install gazebo libgazebo11 libgazebo-dev
```
### Create Folder
First of all we need to create a folder in the home directory:
```
mkdir -p ~/(name)/src
```
After this, go in src folder and clone the px4_msgs repo:
```
git clone https://github.com/PX4/px4_msgs.git
```
Once again in the src folder create a folder:
```
mkdir IIoT_project
```
inside the new folder clone this repo:
```
git clone "https://github.com/GioTKD/IIoT_project"
```
### Wireshark Setup
To seup wireshark we need to create a plugin, in order to do this click [here](https://mavlink.io/en/guide/wireshark.html)
### Build
Before building source ROS2 installation, copy this into .bashrc:
```
source /opt/ros/humble/setup.bash
```
Then go in the home directory, 
```
cd (name folder)
```
and run
```
colcon build
```
once done, we will face a warning about setup.py, but it works.
Then:
```
source install/setup.bash
```
### Run project
Once all is done launch the project:
```
ros2 launch IIoT_project run_project.launch.py
```
