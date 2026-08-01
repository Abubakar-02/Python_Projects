import time
import winsound
from datetime import datetime

def set_alarm(alarm_time):
    print(f"⏰ Alarm set for {alarm_time}")

    while True:
        current_time = datetime.now().strftime("%I:%M %p")
        if current_time == alarm_time:
            print("🔔 Time to wake up!")
            for i in range(8):
                winsound.Beep(1000, 500)
            break
        time.sleep(30)

print("╔══════════════════════════════════╗")
print("║       ⏰ ALARM CLOCK ⏰          ║")
print("╚══════════════════════════════════╝")

alarm_time = input("Enter the alarm time (HH:MM AM/PM): ").upper()
set_alarm(alarm_time)