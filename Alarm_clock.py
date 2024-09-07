import pygame
import datetime
import time

def play_alarm_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)  # Play the alarm sound indefinitely until stopped

def stop_alarm_sound():
    pygame.mixer.music.stop()

def set_alarm(alarm_time, sound_file):
    while True:
        current_time = datetime.datetime.now()
        if current_time >= alarm_time:
            print("Time to wake up!")
            play_alarm_sound(sound_file)
            snooze = input("Would you like to snooze? (yes/no): ")
            if snooze.lower() == "yes":
                alarm_time += datetime.timedelta(minutes=5)  # Snooze for 5 minutes
                print("Alarm snoozed for 5 minutes.")
                time.sleep(5 * 60)  # Sleep for 5 minutes
                stop_alarm_sound()
            else:
                print("Alarm dismissed.")
                break
        else:
            time_diff = alarm_time - current_time
            print(f"Alarm set for {alarm_time.strftime('%H:%M')} ({time_diff.seconds // 3600} hours and {(time_diff.seconds // 60) % 60} minutes remaining)")
            time.sleep(60)  # Check the time every minute

def main():
    print("Welcome to the Alarm Clock!")
    alarm_hour = int(input("Enter the hour (0-23): "))
    alarm_minute = int(input("Enter the minute (0-59): "))
    alarm_sound = input("Enter the path to the alarm sound file: ")

    current_time = datetime.datetime.now()
    alarm_time = datetime.datetime(current_time.year, current_time.month, current_time.day, alarm_hour, alarm_minute)

    if alarm_time < current_time:
        alarm_time += datetime.timedelta(days=1)  # If the alarm time is in the past, set it for tomorrow

    set_alarm(alarm_time, alarm_sound)

if __name__ == "__main__":
    main()

