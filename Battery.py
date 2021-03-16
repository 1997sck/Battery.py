import psutil
from pynotifier import Notification
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent


print(percent)
if percent <= 30:
    Notification(
        title="Battery Low",
        description=str(percent) + "% Battery remain!!",
        duration=5,  # Duration in seconds
        urgency=Notification.URGENCY_CRITICAL,
    ).send()
