
#!/usr/bin/env python3

import subprocess
import time

val = "0,1"

commands = [
    "MicroXRCEAgent udp4 -p 8888",

    "cd ~/PX4-Autopilot && Tools/simulation/gazebo-classic/sitl_multiple_run.sh -m iris -n 2"
]

for command in commands:
    subprocess.run(["gnome-terminal", "--tab", "--", "bash", "-c", command + "; exec bash"])
    
    time.sleep(1)
