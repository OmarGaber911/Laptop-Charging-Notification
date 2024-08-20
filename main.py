import psutil
import time
from playsound import playsound

# Absolute path to the sound file
sound_file = "D:\projects\charge_sound\mixkit-fast-car-drive-by-1538.wav"

# Log file path
log_file = "D:\projects\charge_sound\log.txt"

def is_charging():
    battery = psutil.sensors_battery()
    return battery.power_plugged

def log_message(message):
    with open(log_file, "a") as log:
        log.write(f"{time.ctime()}: {message}\n")

def main():
    was_charging = is_charging()
    log_message(f"Initial charging status: {'Charging' if was_charging else 'Not charging'}")

    while True:
        time.sleep(1)  # Check every 10 seconds
        now_charging = is_charging()
        
        if now_charging and not was_charging:
            log_message("Started charging. Playing sound...")
            playsound(sound_file)
        elif not now_charging and was_charging:
            log_message("Stopped charging.")
        
        was_charging = now_charging

if __name__ == "__main__":
    main()
