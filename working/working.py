import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # I hate life
    pattern = r'(\d{1,2}(:\d{2})? (AM|PM)) to (\d{1,2}(:\d{2})? (AM|PM))'
    match = re.match(pattern, s.strip())

    if not match:
        raise ValueError("Invalid time format.")

    st = match.group(1)
    et = match.group(4)

    # Convert both start and end times
    start_24 = convert24(st)
    end_24 = convert24(et)

    return f"{start_24} to {end_24}"

def convert24(time_str):
    # Match time and period (AM/PM)
    match = re.match(r'(\d{1,2})(:(\d{2}))? (AM|PM)', time_str.strip())

    if not match:
        raise ValueError

    hour = int(match.group(1))
    minute = match.group(3)
    period = match.group(4)

    # Validate minutes
    if minute:
        minute = int(minute)
        if minute < 0 or minute > 59:  # Ensure minutes are in valid range
            raise ValueError
    else:
        minute = 0

    # Convert to 24-hour format
    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    if hour < 0 or hour > 23:  # This check isn't strictly necessary anymore
        raise ValueError

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
