import threading
import subprocess
from time import sleep

subprocess.run(["cd","wvkbd-mobintl"])
sleep(5)
subprocess.run(["cd","killall wvkbd-mobintl"])